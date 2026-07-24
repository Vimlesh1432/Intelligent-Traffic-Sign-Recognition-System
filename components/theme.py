import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    /* 1. Branding hatayein */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* 2. background image (Wahi deep blue image jo aapne di thi) */
    .stApp {
        background-image: url("https://sc04.alicdn.com/kf/A33c85ce40251421493dbd9d0c8555dbbg.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
    }

    /* 3. Spacing fix */
    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    /* 4. Metrics ko Glassmorphism mein badla (White se Glass) */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    /* Metrics text color fix */
    [data-testid="stMetricLabel"], [data-testid="stMetricValue"] {
        color: white !important;
    }

    /* 5. Buttons ko modern aur glassy banaya */
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #2563eb) !important;
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
        box-shadow: 0 0 20px rgba(37, 99, 235, 0.5);
    }

    /* 6. Input fields styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.07) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True)