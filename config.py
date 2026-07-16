import os

# ==============================
# Project Paths
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_NAME = os.path.join(BASE_DIR, "traffic_system.db")

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "traffic_sign_model.h5"
)

LABELS_PATH = os.path.join(
    BASE_DIR,
    "models",
    "labels.csv"
)

# ==============================
# App Configuration
# ==============================

APP_NAME = "Intelligent Traffic Sign Recognition System"

PAGE_TITLE = "Traffic Sign Recognition"

PAGE_ICON = "🚦"

LAYOUT = "wide"