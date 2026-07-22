import streamlit as st

from database import (
    get_total_predictions,
    get_today_predictions,
    get_prediction_history,
    delete_prediction
)


# ==========================================================
# Settings Page
# ==========================================================

def settings():

    
    st.caption("Manage your account and application preferences.")

    user = st.session_state.user

    user_id = user["id"]

    total = get_total_predictions(user_id)
    today = get_today_predictions(user_id)

    # ==========================================================
    # Statistics
    # ==========================================================

    st.subheader("📊 Statistics")

    c1, c2 = st.columns(2)

    c1.metric(
        "Total Predictions",
        total
    )

    c2.metric(
        "Today's Predictions",
        today
    )

    st.divider()

    # ==========================================================
    # Appearance
    # ==========================================================

    st.subheader("🎨 Appearance")

    theme = st.selectbox(
        "Select Theme",
        [
            "Dark",
            "Light"
        ]
    )

    animation = st.toggle(
        "Enable Animations",
        value=True
    )

    st.info(
        f"Current Theme : {theme}"
    )

    st.divider()

    # ==========================================================
    # Notifications
    # ==========================================================

    st.subheader("🔔 Notifications")

    email_notification = st.toggle(
        "Email Notifications",
        value=True
    )

    prediction_notification = st.toggle(
        "Prediction Alerts",
        value=True
    )

    st.divider()

    # ==========================================================
    # AI Status
    # ==========================================================

    st.subheader("🤖 AI System")

    c1, c2, c3 = st.columns(3)

    c1.success("✅ AI Model Loaded")

    c2.success("✅ SQLite Connected")

    c3.success("✅ 43 Traffic Signs")

    st.divider()

    # ==========================================================
    # Data Management
    # ==========================================================

    st.subheader("📂 Data Management")

    history = get_prediction_history(user_id)

    c1, c2 = st.columns(2)

    with c1:

        if history:

            csv = "ID,Traffic Sign,Confidence,Image,Prediction Time\n"

            for row in history:

                csv += (
                    f"{row['id']},"
                    f"{row['sign_name']},"
                    f"{row['confidence']},"
                    f"{row['image_path']},"
                    f"{row['prediction_time']}\n"
                )

            st.download_button(
                "📥 Export History",
                csv,
                "prediction_history.csv",
                "text/csv",
                use_container_width=True
            )

        else:

            st.info("No prediction history.")

    with c2:

        if st.button(
            "🗑 Clear All History",
            use_container_width=True
        ):

            for row in history:

                delete_prediction(row["id"])

            st.success(
                "Prediction history cleared successfully."
            )

            st.rerun()

    st.divider()

    # ==========================================================
    # About Project
    # ==========================================================

    st.subheader("🚦 About Project")

    st.info(
        """
**Project Name**

Intelligent Traffic Sign Recognition System

**Version**

1.0.0

**Technology Stack**

• Python

• TensorFlow

• Streamlit

• SQLite

• OpenCV

• Plotly

**Supported Classes**

43 German Traffic Signs
"""
    )

    st.divider()

    # ==========================================================
    # Developer
    # ==========================================================

    st.subheader("👨‍💻 Developer")

    st.success(
        """
Developer

Vimlesh Yadav

Final Year CSE (Data Science)

JSS Academy of Technical Education, Noida
"""
    )

    st.divider()

    # ==========================================================
    # Logout
    # ==========================================================

    st.subheader("🚪 Logout")

    if st.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.user = None

        st.success(
            "Logged out successfully."
        )

        st.rerun()

    st.divider()

    st.caption(
        "Intelligent Traffic Sign Recognition System | Version 1.0 | Built using Streamlit, TensorFlow & SQLite"
    )