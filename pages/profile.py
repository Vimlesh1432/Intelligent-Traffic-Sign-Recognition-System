import streamlit as st
from datetime import datetime

from database import (
    get_total_predictions,
    get_today_predictions,
    get_average_confidence,
    get_best_prediction,
    get_top_signs
)


# ==========================================================
# Profile Page
# ==========================================================

def profile():

    st.title("👤 My Profile")

    user = st.session_state.user

    user_id = user["id"]

    total = get_total_predictions(user_id)

    today = get_today_predictions(user_id)

    accuracy = get_average_confidence(user_id)

    best = get_best_prediction(user_id)

    top = get_top_signs(user_id)

    st.markdown("""
    <style>

    .profile-card{
    background:#18181b;
    padding:30px;
    border-radius:18px;
    border:1px solid #30363d;
    transition:.3s;
    }

    .profile-card:hover{
    border:1px solid #5b5bd6;
    box-shadow:0 0 18px rgba(91,91,214,.30);
    }

    .profile-name{
    font-size:42px;
    font-weight:700;
    color:white;
    margin-bottom:5px;
    }

    .profile-email{
    font-size:16px;
    color:#b0b0b0;
    margin-bottom:18px;
    }

    .small-tag{
    display:inline-block;
    padding:5px 12px;
    background:#242424;
    border-radius:8px;
    font-size:13px;
    margin-right:8px;
    color:#d0d0d0;
    }

    .stat-card{

    background:#1f1f1f;

    padding:18px;

    border-radius:15px;

    text-align:center;

    border:1px solid #333;

    }

    .stat-number{

    font-size:38px;

    font-weight:bold;

    color:white;

    }

    .stat-title{

    font-size:14px;

    color:#9ca3af;

    letter-spacing:1px;

    }

    </style>
    """,unsafe_allow_html=True)


    # ==========================================================
    # User Information
    # ==========================================================

    left,right = st.columns([1,4])

    with left:

        st.image(

            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",

            width=170

        )

    with right:

        st.markdown(f"""

    <div class="profile-name">

    {user['username']}

    </div>

    <div class="profile-email">

    {user['email']}

    </div>

    <span class="small-tag">🤖 AI User</span>

    <span class="small-tag">🚦 Traffic Detection</span>

    <span class="small-tag">📅 Joined 2026</span>

    """,unsafe_allow_html=True)
        
        st.write("")

        c1,c2,c3,c4 = st.columns(4)

        with c1:

            st.markdown(f"""

        <div class="stat-card">

        <div class="stat-number">

        {total}

        </div>

        <div class="stat-title">

        TOTAL PREDICTIONS

        </div>

        </div>

        """,unsafe_allow_html=True)

        with c2:

            st.markdown(f"""

        <div class="stat-card">

        <div class="stat-number">

        {today}

        </div>

        <div class="stat-title">

        TODAY

        </div>

        </div>

        """,unsafe_allow_html=True)

        with c3:

            st.markdown(f"""

        <div class="stat-card">

        <div class="stat-number">

        {accuracy}%

        </div>

        <div class="stat-title">

        ACCURACY

        </div>

        </div>

        """,unsafe_allow_html=True)

        with c4:

            if best:

                value=f"{best['confidence']*100:.1f}%"

            else:

                value="0%"

            st.markdown(f"""

        <div class="stat-card">

        <div class="stat-number">

        {value}

        </div>

        <div class="stat-title">

        BEST SCORE

        </div>

        </div>

        """,unsafe_allow_html=True)

        st.divider()


        left, right = st.columns([2.3, 1])

        with left:

            st.subheader("📌 Recent Activity")

            if best:

                st.success(
                    f"""
        ### 🚦 Best Prediction

        **Traffic Sign:** {best['sign_name']}

        **Confidence:** {best['confidence']*100:.2f}%

        **Prediction Time:** {best['prediction_time']}
        """
                )

            else:

                st.info("No prediction available yet.")

        

            st.subheader("🏅 Achievements")

            col1, col2, col3 = st.columns(3)

            with col1:

                if total >= 10:
                    st.success("🥉 Beginner")
                else:
                    st.info("🥉 Beginner")

            with col2:

                if total >= 50:
                    st.success("🥈 Explorer")
                else:
                    st.info("🥈 Explorer")

            with col3:

                if total >= 100:
                    st.success("🥇 Expert")
                else:
                    st.info("🥇 Expert")

            if top:

                for i, row in enumerate(top, start=1):

                    st.markdown(
                        f"""
        ### #{i} {row['sign_name']}

        Detected **{row['count']}** times.
        """
                )

                st.progress(min(row["count"] / 10, 1.0))

            else:

                st.info("No prediction history available.")



            with right:

                st.subheader("🤖 AI Health")

                if accuracy >= 90:
                    st.success("🟢 Excellent")

                elif accuracy >= 75:
                    st.warning("🟡 Good")

                else:
                    st.error("🔴 Needs Improvement")

                st.write("")

                st.subheader("⚡ Quick Actions")

                if st.button(
                    "🚦 New Detection",
                    use_container_width=True
                ):
                    st.info("Open the Detection page from the sidebar.")

                if st.button(
                    "📜 Prediction History",
                    use_container_width=True
                ):
                    st.info("Open the History page from the sidebar.")