import streamlit as st
import numpy as np
from PIL import Image
from datetime import datetime
import uuid
import plotly.graph_objects as go

from utils.predictor import predict
from database import save_prediction


def show_prediction(image, file_name):
    image_np = np.array(image)

    with st.spinner("🤖 AI is analyzing the image..."):
        (
            sign_name,
            confidence,
            description,
            category,
            risk,
            driver_action,
            top_predictions
        ) = predict(image_np)

        if sign_name is None:
            st.error("❌ This is not a traffic sign.")
            st.info("Please upload a clear image containing a traffic sign.")
            return

    # Save to DB (database.py ke hisab se: sirf sign_name, confidence, image_path)
    save_prediction(
        sign_name=sign_name,
        confidence=confidence,
        image_path=file_name
    )

    # ================= 1. Main Preview Card =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 Detection Result")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(image, caption="Uploaded Sign", use_container_width=True)

    with col2:
        st.metric("🚦 Traffic Sign", sign_name)
        st.metric("📊 Confidence", f"{confidence*100:.2f}%")
        st.progress(confidence)
        st.success("✅ Prediction Completed!")

        prediction_id = str(uuid.uuid4())[:8]
        st.markdown(f"""
            <div style="background:rgba(255,255,255,0.05); padding:10px; border-radius:10px; font-size:12px;">
                <b>ID:</b> {prediction_id}<br>
                <b>Time:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= 2. Gauge & Top Predictions =================
    left, right = st.columns([1.2, 1])

    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📊 AI Confidence Gauge")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=confidence * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': "white"},
                'bar': {'color': "#C9184A"},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 2,
                'bordercolor': "white",
                'steps': [
                    {'range': [0, 40], 'color': 'rgba(239, 68, 68, 0.3)'},
                    {'range': [40, 75], 'color': 'rgba(245, 158, 11, 0.3)'},
                    {'range': [75, 100], 'color': 'rgba(34, 197, 94, 0.3)'}
                ],
            }
        ))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white", height=300, margin=dict(t=30, b=0, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True, key=f"gauge_{prediction_id}")
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🏆 Top Alternatives")
        for i, item in enumerate(top_predictions, start=1):
            st.write(f"**#{i}. {item['name']}** ({item['confidence']*100:.1f}%)")
            st.progress(item["confidence"])
        st.markdown('</div>', unsafe_allow_html=True)

    # ================= 3. Summary Details =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 Detailed Summary")

    c1, c2 = st.columns(2)
    with c1:
        st.info(f"**📂 Category**\n\n{category}")
    with c2:
        if risk == "High":
            st.error(f"**⚠️ Risk Level**\n\n{risk}")
        elif risk == "Medium":
            st.warning(f"**⚠️ Risk Level**\n\n{risk}")
        else:
            st.success(f"**⚠️ Risk Level**\n\n{risk}")

    st.markdown(f"""
        <div style="background:rgba(255,255,255,0.03); padding:15px; border-radius:12px; border-left: 5px solid #C9184A; margin-top:10px;">
            <h4 style="margin:0;">🚗 Driver Action Required</h4>
            <p style="margin:5px 0 0 0;">{driver_action}</p>
        </div>
        <div style="margin-top:15px;">
            <p><b>ℹ️ Description:</b> {description}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def detect():
    st.title("Traffic Sign Detection")
    st.write("Choose your input method below to start AI recognition.")
    option = st.radio("", ["📁 Upload Image", "📷 Webcam"], horizontal=True)

    # --- Upload Logic ---
    if option == "📁 Upload Image":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose an Image (JPG, PNG)", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            
            if st.button("🔍 Run Prediction", use_container_width=True):
                show_prediction(image, uploaded_file.name)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Webcam Logic ---
    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        camera_image = st.camera_input("Focus on the Traffic Sign")
        if camera_image is not None:
            image = Image.open(camera_image).convert("RGB")
            if st.button("📷 Capture & Predict", use_container_width=True):
                show_prediction(image, "webcam_capture.jpg")
        st.markdown('</div>', unsafe_allow_html=True)