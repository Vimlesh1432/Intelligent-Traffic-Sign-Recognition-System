import cv2
import numpy as np


def preprocess_image(image):
    """
    Preprocess uploaded image before prediction.
    """

    # Resize to model input size
    image = cv2.resize(image, (32, 32))

    # Normalize
    image = image.astype(np.float32) / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    return image