import numpy as np

from utils.model_loader import load_model
from utils.image_processing import preprocess_image
from utils.traffic_info import TRAFFIC_SIGNS


def predict(image):
    """
    Predict traffic sign from image.
    Returns:
        sign_name (str)
        confidence (float)
    """

    # Load trained model
    model = load_model()

    # Preprocess image
    processed = preprocess_image(image)

    # Prediction
    prediction = model.predict(processed, verbose=0)

    # Get class index
    class_id = int(np.argmax(prediction))

    # Get confidence
    confidence = float(np.max(prediction))

    # Get traffic sign name
    sign_name = TRAFFIC_SIGNS[class_id]

    description = TRAFFIC_SIGNS[class_id]["description"]

    return sign_name, confidence, description