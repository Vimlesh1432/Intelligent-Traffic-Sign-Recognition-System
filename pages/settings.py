import streamlit as st


def settings():

    st.title("⚙️ Settings")

    st.subheader("🎨 Appearance")

    theme = st.selectbox(
        "Theme",
        [
            "Dark",
            "Light"
        ]
    )

    st.info(
        f"Selected Theme: {theme}"
    )

    st.divider()

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

    st.subheader("ℹ️ About")

    st.write("Project Name: Intelligent Traffic Sign Recognition System")

    st.write("Version: 1.0.0")

    st.write("Developed using Python, TensorFlow, Streamlit and SQLite.")

    st.divider()

    if st.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.session_state.user = None

        st.rerun()