import streamlit as st
import pandas as pd

from database import get_prediction_history


def history():

    st.title("📜 Prediction History")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Predictions",
            len(data)
        )

    with col2:

        avg = (
            sum(row["confidence"] for row in data)
            / len(data)
        ) * 100

        st.metric(
            "Average Confidence",
            f"{avg:.2f}%"
        )

    st.divider()


    data = get_prediction_history(
        st.session_state.user["id"]
    )

    if not data:

        st.info("No prediction history found.")

        return

    df = pd.DataFrame(
        [dict(row) for row in data]
    )


    df.rename(
        columns={
            "id": "ID",
            "sign_name": "Traffic Sign",
            "confidence": "Confidence",
            "image_path": "Image",
            "prediction_time": "Prediction Time",
        },
        inplace=True,
    )

    # ----------------------------
    # Search
    # ----------------------------

    search = st.text_input(
        "🔍 Search Traffic Sign"
    )

    if search:

        df = df[
            df["Traffic Sign"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    df["Confidence"] = (
        df["Confidence"] * 100
    ).round(2)

    df["Confidence"] = (
        df["Confidence"].astype(str) + "%"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.download_button(
        label="📥 Download History (CSV)",
        data=df.to_csv(index=False),
        file_name="prediction_history.csv",
        mime="text/csv"
    )