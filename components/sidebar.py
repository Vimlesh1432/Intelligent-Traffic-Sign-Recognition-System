import streamlit as st

def sidebar():

    with st.sidebar:
        st.title("🚦 Navigation")

        selected = st.radio(
            "",
            [
                "Dashboard",
                "Detect",
                "History",
                "Profile",
                "Settings",
                "Logout"
            ]
        )

    return selected