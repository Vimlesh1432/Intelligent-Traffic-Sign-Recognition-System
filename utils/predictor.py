import numpy as np

from utils.model_loader import load_model
from utils.image_processing import preprocess_image
from utils.traffic_info import TRAFFIC_SIGNS


def predict(image):
    """
    Predict traffic sign from image.

    Returns:
        sign_name
        confidence
        description
        category
        risk
        driver_action
        top_predictions
    """

    # Load trained model
    model = load_model()

    # Preprocess image
    processed = preprocess_image(image)

    # Prediction
    prediction = model.predict(processed, verbose=0)[0]

    # Best prediction
    class_id = int(np.argmax(prediction))
    confidence = float(prediction[class_id])

# ------------------------------
# Confidence Threshold
# ------------------------------
    THRESHOLD = 0.85

    if confidence < THRESHOLD:

        return (
            None,
            confidence,
            "This is not a valid traffic sign.",
            "",
            "",
            "",
            []
        )

    traffic_sign = TRAFFIC_SIGNS[class_id]

    sign_name = traffic_sign["name"]
    description = traffic_sign["description"]
    category = traffic_sign["category"]
    risk = traffic_sign["risk"]
    driver_action = traffic_sign["driver_action"]

    # ==========================
    # Top 3 Predictions
    # ==========================

    top_indices = np.argsort(prediction)[-3:][::-1]

    top_predictions = []

    for idx in top_indices:

        top_predictions.append({

            "name": TRAFFIC_SIGNS[idx]["name"],
            "confidence": float(prediction[idx])

        })

    # ==========================
    # Return
    # ==========================

    return (
        sign_name,
        confidence,
        description,
        category,
        risk,
        driver_action,
        top_predictions
    )