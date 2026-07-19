import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_sign_distribution
from database import get_recent_predictions

from database import (
    get_total_predictions,
    get_today_predictions,
    get_average_confidence,
)

def dashboard():

    st.success(
        f"👋 Welcome back, {st.session_state.user['username']}"
    )

    user_id = st.session_state.user["id"]

    total_predictions = get_total_predictions(user_id)

    today_predictions = get_today_predictions(user_id)

    average_confidence = get_average_confidence(user_id)

    st.write("")

    # ================= Metrics =================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
    "Predictions",
    total_predictions
    )

    c2.metric(
        "Average Confidence",
        f"{average_confidence}%"
    )

    c3.metric(
        "Today's Scan",
        today_predictions
    )

    c4.metric(
        "Traffic Signs",
        43
    )

    st.divider()

    # ================= Charts =================

    left, right = st.columns(2)

    with left:

        df = pd.DataFrame({

            "Day": [
                "Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
                "Sat",
                "Sun"
            ],

            "Predictions": [
                20,
                25,
                18,
                30,
                22,
                40,
                35
            ]

        })

        fig = px.bar(

            df,

            x="Day",

            y="Predictions",

            title="Weekly Predictions"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

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
                use_container_width=True
            )

        else:

            st.info("No prediction data available.")



        fig2 = px.pie(

            pie,

            names="Traffic Sign",

            values="Count",

            title="Traffic Sign Distribution"

        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.divider()

    # ================= Recent Activity =================

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

        st.dataframe(
        history,
        use_container_width=True
    )