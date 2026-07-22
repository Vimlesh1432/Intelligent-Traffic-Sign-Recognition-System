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

            st.info(
                "Please upload a clear image containing a traffic sign."
            )

            return

    save_prediction(
        user_id=st.session_state.user["id"],
        sign_name=sign_name,
        confidence=confidence,
        image_path=file_name
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(
            image,
            caption="Traffic Sign",
            use_container_width=True
        )

    with col2:

        st.metric("🚦 Traffic Sign", sign_name)
        st.metric(
            "📊 Confidence",
            f"{confidence*100:.2f}%"
        )

        st.progress(confidence)
        st.info(description)

    st.success("✅ Prediction Completed Successfully!")

    prediction_id = str(uuid.uuid4())[:8]

    st.caption(
        f"Prediction Time : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

    st.code(f"Prediction ID : {prediction_id}")

    st.divider()

    st.subheader("🏆 Top 3 AI Predictions")

    for i, item in enumerate(top_predictions, start=1):

        st.write(f"**#{i}. {item['name']}**")

        st.progress(item["confidence"])

        st.caption(
            f"{item['confidence']*100:.2f}%"
        )

    st.subheader("📊 AI Confidence Score")

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=confidence * 100,
            title={"text": "AI Confidence"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 30], "color": "#ffcccc"},
                    {"range": [30, 70], "color": "#fff4cc"},
                    {"range": [70, 100], "color": "#ccffcc"},
                ],
            },
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key=f"gauge_{prediction_id}"
    )

    st.subheader("📋 Detection Summary")

    c1, c2 = st.columns(2)

    with c1:
        st.info(f"### 📂 Category\n\n{category}")

    with c2:

        if risk == "High":
            st.error(f"### ⚠️ Risk Level\n\n{risk}")

        elif risk == "Medium":
            st.warning(f"### ⚠️ Risk Level\n\n{risk}")

        else:
            st.success(f"### ⚠️ Risk Level\n\n{risk}")

    st.info(f"### ℹ️ Description\n\n{description}")

    st.success(f"### 🚗 Driver Action\n\n{driver_action}")


def detect():

    st.title("Choose Detection Method")
    option = st.radio(
        "",
        ["📁 Upload Image", "📷 Webcam"],
        horizontal=True
    )

    # ================= Upload =================

    if option == "📁 Upload Image":

        uploaded_file = st.file_uploader(
            "Choose an Image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:

            image = Image.open(uploaded_file).convert("RGB")

            if st.button(
                "🔍 Predict",
                use_container_width=True
            ):

                show_prediction(
                    image,
                    uploaded_file.name
                )

    # ================= Webcam =================

    else:

        camera_image = st.camera_input(
            "Capture Traffic Sign"
        )

        if camera_image is not None:

            image = Image.open(camera_image).convert("RGB")

        

            if st.button(
                "📷 Predict from Camera",
                use_container_width=True
            ):

                image_np = np.array(image)

                (
                    sign_name,
                    confidence,
                    description,
                    category,
                    risk,
                    driver_action,
                    top_predictions
                ) = predict(image_np)

                # -----------------------------
                # Validation
                # -----------------------------
                if sign_name is None:

                    st.error("❌ This is not a Traffic Sign.")

                    st.warning(
                        "Please capture a valid traffic sign image."
                    )

                    return

                # Same UI
                show_prediction(
                    image,
                    "webcam_capture.jpg"
                )