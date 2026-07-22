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
    get_best_prediction
)


def dashboard():

    st.success(
        f"👋 Welcome back, {st.session_state.user['username']}"
    )

    user_id = st.session_state.user["id"]

    # ================= Database Data =================

    total_predictions = get_total_predictions(user_id)
    today_predictions = get_today_predictions(user_id)
    average_confidence = get_average_confidence(user_id)

    # ================= Metrics =================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Predictions", total_predictions)
    c2.metric("Average Confidence", f"{average_confidence}%")
    c3.metric("Today's Scan", today_predictions)
    c4.metric("Traffic Signs", 43)

    st.divider()

    # ================= Charts =================

    left, right = st.columns(2)

    # -------- Weekly Prediction Chart --------

    with left:

        weekly = get_weekly_predictions(user_id)

        if weekly:

            df = pd.DataFrame(
                weekly,
                columns=["Day", "Predictions"]
            )

            fig = px.bar(
                df,
                x="Day",
                y="Predictions",
                title="Weekly Predictions"
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                key="weekly_predictions_chart"
            )

        else:

            st.info("No weekly prediction data available.")

    # -------- Traffic Sign Distribution --------

    with right:

        distribution = get_sign_distribution(user_id)

        if distribution:

            pie = pd.DataFrame(
                distribution,
                columns=[
                    "Traffic Sign",
                    "Count"
                ]
            )

            fig2 = px.pie(
                pie,
                names="Traffic Sign",
                values="Count",
                title="Traffic Sign Distribution"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True,
                key="traffic_sign_distribution_chart"
            )

        else:

            st.info("No prediction data available.")

    st.divider()

    # ================= Highest Confidence =================

    st.subheader("🏆 Highest Confidence Prediction")

    best = get_best_prediction(user_id)

    if best:

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "🚦 Traffic Sign",
            best["sign_name"]
        )

        col2.metric(
            "📊 Confidence",
            f"{best['confidence']*100:.2f}%"
        )

        col3.metric(
            "🕒 Time",
            best["prediction_time"]
        )

    else:

        st.info("No prediction available.")

    st.divider()

    # ================= Top Traffic Signs =================

    st.subheader("🔥 Top 5 Detected Traffic Signs")

    top = get_top_signs(user_id)

    if top:

        top_df = pd.DataFrame(
            top,
            columns=[
                "Traffic Sign",
                "Count"
            ]
        )

        fig3 = px.bar(
            top_df,
            x="Count",
            y="Traffic Sign",
            orientation="h",
            title="Most Detected Traffic Signs"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True,
            key="top_signs_chart"
        )

    else:

        st.info("No prediction data available.")

    st.divider()

    # ================= Recent Predictions =================

    st.subheader("📜 Recent Predictions")

    recent = get_recent_predictions(user_id)

    if recent:

        history = pd.DataFrame(
            recent,
            columns=[
                "Traffic Sign",
                "Confidence",
                "Prediction Time"
            ]
        )

        history["Confidence"] = (
            history["Confidence"] * 100
        ).round(2).astype(str) + "%"

        st.dataframe(
            history,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No recent predictions.")
