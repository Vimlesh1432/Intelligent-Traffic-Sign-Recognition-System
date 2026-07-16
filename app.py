import streamlit as st

from config import (
    APP_NAME,
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT
)

from database import create_database
from auth.login import login_page
from auth.register import register_page

from components.sidebar import sidebar

from pages.dashboard import dashboard
from pages.detect import detect
from pages.history import history
from pages.profile import profile
from pages.settings import settings
from utils.helpers import load_css
from components.theme import apply_theme

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)
st.sidebar.write("✅ Sidebar Working")


#load_css("assets/css/style.css")

#apply_theme()

# ----------------------------
# Create Database
# ----------------------------

create_database()


# ----------------------------
# Session State
# ----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None




# ----------------------------
# Authentication
# ----------------------------

if not st.session_state.logged_in:

    st.sidebar.title(APP_NAME)

    menu = st.sidebar.radio(
        "Navigation",
        ["Login", "Register"]
    )

    if menu == "Login":
        login_page()
    else:
        register_page()

else:

    selected = sidebar()

    if selected == "Dashboard":
        dashboard()

    elif selected == "Detect":
        detect()

    elif selected == "History":
        history()

    elif selected == "Profile":
        profile()

    elif selected == "Settings":
        settings()

    elif selected == "Logout":
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()