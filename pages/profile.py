import streamlit as st
from database import (
    get_total_predictions,
    get_today_predictions,
    get_average_confidence
)


def profile():

    st.title("👤 My Profile")

    user = st.session_state.user

    total = get_total_predictions(user["id"])
    today = get_today_predictions(user["id"])
    accuracy = get_average_confidence(user["id"])

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            width=180
        )

    with col2:

        st.subheader(user["username"])

        st.write(f"**📧 Email:** {user['email']}")

        st.write("**🎓 Role:** AI System User")

        st.write("**🚦 Project:** Intelligent Traffic Sign Recognition System")

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Predictions",
        total
    )

    c2.metric(
        "Today's Predictions",
        today
    )

    c3.metric(
        "Average Confidence",
        f"{accuracy}%"
    )

    st.divider()

    st.success("✅ Account Active")