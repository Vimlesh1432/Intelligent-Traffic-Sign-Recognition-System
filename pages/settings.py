import streamlit as st
from database import (
    get_total_predictions,
    get_today_predictions,
    get_prediction_history,
    clear_all_history,
)

def settings():
    # --- Header Section ---
    
    st.write("Manage appearance, and data preferences.")

    # Fetch Stats
    total = get_total_predictions()
    today = get_today_predictions()

    # ================= 1. Statistics (Adaptive) =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Quick Stats")
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Total Predictions", total)
    with c2:
        st.metric("Today's Count", today)
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= 2. Appearance & Notifications =================
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎨 Appearance")
        theme = st.selectbox("Select Theme", ["Dark", "Light"])
        animation = st.toggle("Enable Animations", value=True)
        st.markdown(f'<p style="font-size:12px; opacity:0.6;">Current Theme: {theme}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🔔 Notifications")
        st.toggle("Email Notifications", value=True)
        st.toggle("Prediction Alerts", value=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ================= 3. AI System Status =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🤖 AI System Engine")
    a1, a2, a3 = st.columns(3)
    with a1:
        st.success("✅ Model Loaded")
    with a2:
        st.success("✅ SQLite Active")
    with a3:
        st.success("✅ 43 Classes")
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= 4. Data Management =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📂 Data Management")
    history = get_prediction_history()

    dm1, dm2 = st.columns(2)
    with dm1:
        if history:
            csv = "ID,Traffic Sign,Confidence,Image,Prediction Time\n"
            for row in history:
                csv += f"{row['id']},{row['sign_name']},{row['confidence']},{row['image_path']},{row['prediction_time']}\n"
            st.download_button("📥 Export History", csv, "history.csv", "text/csv", use_container_width=True)
        else:
            st.info("No records to export.")

    with dm2:
        if history:
            if st.button("🗑 Clear All History", use_container_width=True):
                clear_all_history()
                st.success("History cleared!")
                st.rerun()
        else:
            st.info("History is empty.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= 5. Project & Developer Info =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🫆 About Project")
    st.info("""
    **Project:** Intelligent Traffic Sign Recognition System  
    **Version:** 1.0.0  
    **Stack:** Python, TensorFlow, Streamlit, SQLite, OpenCV
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👨‍💻 Developer")
    st.success("""
    **Vimlesh Yadav**  
    Final Year CSE (Data Science)  
    JSS Academy of Technical Education, Noida
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= 6. Local Mode (auth hat gaya hai) =================
    st.markdown('<div class="card" style="border-left: 5px solid #22d3ee;">', unsafe_allow_html=True)
    st.subheader("🔒 Local Mode")
    st.info("No account required — all detection data is stored locally on this device.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Simple Footer
    st.markdown('<p style="text-align:center; opacity:0.3; font-size:11px;">Settings Build 2026.07.25</p>', unsafe_allow_html=True)