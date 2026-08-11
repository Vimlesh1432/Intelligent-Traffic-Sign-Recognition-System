"""Dashboard page."""
import streamlit as st
import pandas as pd
import plotly.express as px

from database import (
    get_total_predictions,
    get_today_predictions,
    get_average_confidence,
    get_sign_distribution,
    get_recent_predictions,
    get_weekly_predictions,
    get_top_signs,
    get_best_prediction,
)


def dashboard():
    # --- Header Wrapper ---
    st.markdown('<div class="glass-panel" style="text-align:center;">', unsafe_allow_html=True)
    st.success("👋 Welcome back!")
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= Database Data =================
    total_predictions = get_total_predictions()
    today_predictions = get_today_predictions()
    average_confidence = get_average_confidence()

    # ================= Metrics (Adaptive Row) =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Predictions", total_predictions)
    with c2:
        st.metric("Average Confidence", f"{average_confidence}%")
    with c3:
        st.metric("Today's Scan", today_predictions)
    with c4:
        st.metric("Traffic Signs", 43)

    st.markdown("<br>", unsafe_allow_html=True)

    # Helper function for Plotly UI consistency (Transparency)
    def style_plotly(fig):
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color="white",
            margin=dict(t=40, b=0, l=0, r=0)
        )
        return fig

    # ================= Charts Section =================
    left, right = st.columns(2)

    # -------- Weekly Prediction Chart --------
    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        weekly = get_weekly_predictions()
        if weekly:
            df = pd.DataFrame(weekly, columns=["Day", "Predictions"])
            fig = px.bar(df, x="Day", y="Predictions", title="Weekly Predictions")
            st.plotly_chart(style_plotly(fig), use_container_width=True, key="weekly_predictions_chart")
        else:
            st.info("No weekly prediction data available.")
        st.markdown('</div>', unsafe_allow_html=True)

    # -------- Traffic Sign Distribution --------
    with right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        distribution = get_sign_distribution()
        if distribution:
            pie = pd.DataFrame(distribution, columns=["Traffic Sign", "Count"])
            fig2 = px.pie(pie, names="Traffic Sign", values="Count", title="Sign Distribution")
            st.plotly_chart(style_plotly(fig2), use_container_width=True, key="traffic_sign_distribution_chart")
        else:
            st.info("No prediction data available.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ================= Highest Confidence =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏆 Highest Confidence Prediction")
    best = get_best_prediction()
    if best:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🚦 Traffic Sign", best["sign_name"])
        with col2:
            st.metric("📊 Confidence", f"{best['confidence']*100:.2f}%")
        with col3:
            st.metric("🕒 Time", best["prediction_time"])
    else:
        st.info("No prediction available.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= Top Traffic Signs =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔥 Top 5 Detected Traffic Signs")
    top = get_top_signs()
    if top:
        top_df = pd.DataFrame(top, columns=["Traffic Sign", "Count"])
        fig3 = px.bar(top_df, x="Count", y="Traffic Sign", orientation="h", title="")
        st.plotly_chart(style_plotly(fig3), use_container_width=True, key="top_signs_chart")
    else:
        st.info("No prediction data available.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= Recent Predictions =================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📜 Recent Predictions")
    recent = get_recent_predictions()
    if recent:
        history = pd.DataFrame(recent, columns=["Traffic Sign", "Confidence", "Prediction Time"])
        history["Confidence"] = (history["Confidence"] * 100).round(2).astype(str) + "%"
        st.dataframe(history, use_container_width=True, hide_index=True)
    else:
        st.info("No recent predictions.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= Footer =================
    st.markdown("""
        <div style="text-align:center; padding: 20px; opacity: 0.6; font-size: 14px;">
            <p>Intelligent Traffic Sign Recognition System | Version 1.0</p>
            <p>Built with ❤️ by Vimlesh !</p>
            <p>© 2026 - All Rights Reserved.</p>
        </div>
    """, unsafe_allow_html=True)