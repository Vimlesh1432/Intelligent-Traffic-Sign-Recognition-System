import streamlit as st
import pandas as pd

from database import (
    get_prediction_history,
    delete_prediction,
)

def history():
    # --- Header Section ---
    
    st.write("Browse, search, and manage your past traffic sign detections.")

    # ----------------------------
    # Load Data
    # ----------------------------
    data = get_prediction_history()

    if not data:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.info("No prediction history found. Start by detecting some traffic signs!")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # ----------------------------
    # Statistics (Glass Card)
    # ----------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 History Statistics")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Predictions", len(data))

    with col2:
        avg = (sum(row["confidence"] for row in data) / len(data)) * 100
        st.metric("Average Confidence", f"{avg:.2f}%")
    st.markdown('</div>', unsafe_allow_html=True)

    # ----------------------------
    # Data Processing
    # ----------------------------
    df = pd.DataFrame([dict(row) for row in data])

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

    # Process confidence for display
    df["Confidence_Raw"] = df["Confidence"] # Keep numeric for filtering if needed
    df["Confidence"] = (df["Confidence"] * 100).round(2).astype(str) + "%"

    # ----------------------------
    # Search & Table (Glass Card)
    # ----------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 Search & Records")

    search = st.text_input("Search Traffic Sign Name", placeholder="e.g. Stop, Speed Limit...")

    if search:
        df = df[df["Traffic Sign"].str.contains(search, case=False, na=False)]

    # Display Table
    st.dataframe(
        df[["ID", "Traffic Sign", "Confidence", "Prediction Time"]],
        use_container_width=True,
        hide_index=True,
    )

    # Download Button
    st.download_button(
        label="📥 Export to CSV",
        data=df.to_csv(index=False),
        file_name="traffic_sign_history.csv",
        mime="text/csv",
        use_container_width=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ----------------------------
    # Delete Prediction (Glass Card)
    # ----------------------------
    st.markdown('<div class="card" style="border-left: 5px solid #ef4444;">', unsafe_allow_html=True)
    st.subheader("🗑 Manage Records")
    st.write("Enter a Prediction ID to permanently remove it from history.")

    del_col1, del_col2 = st.columns([2, 1])

    with del_col1:
        prediction_id = st.number_input("Prediction ID", min_value=0, step=1, key="del_id")

    with del_col2:
        st.write("<br>", unsafe_allow_html=True) # Alignment
        if st.button("Delete Record", use_container_width=True):
            if prediction_id > 0:
                delete_prediction(prediction_id)
                st.success(f"ID {prediction_id} deleted!")
                st.rerun()
            else:
                st.warning("Please enter a valid ID.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div style="text-align:center; opacity:0.5; font-size:12px; margin-top:20px;">History Management System v1.0</div>', unsafe_allow_html=True)