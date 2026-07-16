import tensorflow as tf
from functools import lru_cache
from config import MODEL_PATH


@lru_cache(maxsize=1)
def load_model():
    """
    Load the TensorFlow model only once.
    """
    return tf.keras.models.load_model(MODEL_PATH)