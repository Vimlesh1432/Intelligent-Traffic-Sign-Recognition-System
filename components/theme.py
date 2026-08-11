import streamlit as st


def apply_theme():
    st.markdown("""
    <style>
    /* 1. Branding hatayein */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* 2. background image + burgundy tint (Wahi deep blue image jo aapne di thi) */
    .stApp {
        background-image:
            linear-gradient(160deg, rgba(58, 12, 26, 0.72), rgba(16, 10, 18, 0.85)),
            url("https://sc04.alicdn.com/kf/A33c85ce40251421493dbd9d0c8555dbbg.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
    }

    /* 3. Spacing fix - FLUID padding (window resize par content squeeze na ho) */
    .block-container {
        padding-top: clamp(1rem, 2vw, 2rem);
        padding-left: clamp(1rem, 3vw, 3rem);
        padding-right: clamp(1rem, 3vw, 3rem);
        padding-bottom: clamp(1rem, 2vw, 2rem);
        max-width: 100% !important;
    }

    /* 4. Metrics ko Glassmorphism mein badla (Burgundy glass) */
    div[data-testid="metric-container"] {
        background: rgba(201, 24, 74, 0.07) !important;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 18px;
        border: 1px solid rgba(201, 24, 74, 0.2);
        box-shadow: 0 8px 32px 0 rgba(128, 0, 32, 0.3);
    }

    /* Metrics text color fix */
    [data-testid="stMetricLabel"], [data-testid="stMetricValue"] {
        color: white !important;
    }

    /* 5. Buttons — burgundy gradient */
    .stButton>button {
        background: linear-gradient(90deg, #C9184A, #800020) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px;
        height: 45px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(201, 24, 74, 0.55);
    }

    /* 6. Input fields styling (burgundy border) */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.07) !important;
        color: white !important;
        border: 1px solid rgba(201, 24, 74, 0.4) !important;
        border-radius: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True)