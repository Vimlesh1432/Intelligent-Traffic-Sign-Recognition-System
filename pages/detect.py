import streamlit as st
import numpy as np

from PIL import Image

from utils.predictor import predict
from database import save_prediction


def detect():

    st.title("🚦 AI Traffic Sign Detection")

    st.write("Upload a traffic sign image and let AI detect it.")

    uploaded_file = st.file_uploader(
        "Choose an Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button("🔍 Predict"):

            # AI Prediction
            sign_name, confidence, description = predict(image)

            # Save Prediction
            save_prediction(
                user_id=st.session_state.user["id"],
                sign_name=sign_name,
                confidence=confidence,
                image_path=uploaded_file.name
            )

            st.success("✅ Prediction Completed Successfully!")

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "🚦 Traffic Sign",
                    sign_name
                )

                st.info(description)

            with col2:

                st.metric(
                    "📊 Confidence",
                    f"{confidence * 100:.2f}%"
                )

                st.progress(confidence)
