import streamlit as st
import pandas as pd

from database import get_prediction_history


def history():

    st.title("📜 Prediction History")

    data = get_prediction_history(
        st.session_state.user["id"]
    )

    if not data:

        st.info("No prediction history found.")

        return

    df = pd.DataFrame(data)

    df.columns = [
        "Traffic Sign",
        "Confidence",
        "Image",
        "Prediction Time"
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