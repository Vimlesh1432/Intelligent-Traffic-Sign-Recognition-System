import streamlit as st
import pandas as pd
import plotly.express as px


def dashboard():

    st.title("🚦 Intelligent Traffic Sign Recognition System")

    st.caption("AI Powered Traffic Sign Detection Dashboard")

    st.success(
        f"👋 Welcome back, {st.session_state.user['username']}"
    )

    st.write("")

    # ================= Metrics =================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Predictions", 125)
    c2.metric("Accuracy", "98.6%")
    c3.metric("Today's Scan", 12)
    c4.metric("Traffic Signs", 43)

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

        pie = pd.DataFrame({

            "Traffic Sign": [

                "Speed Limit",

                "Stop",

                "Yield",

                "No Entry",

                "Parking"

            ],

            "Count": [

                40,

                15,

                12,

                20,

                13

            ]

        })

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

    history = pd.DataFrame({

        "Image": [

            "img1.jpg",

            "img2.jpg",

            "img3.jpg"

        ],

        "Prediction": [

            "Stop",

            "Speed Limit",

            "Yield"

        ],

        "Confidence": [

            "99%",

            "98%",

            "96%"

        ]

    })

    st.dataframe(
        history,
        use_container_width=True
    )