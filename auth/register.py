import streamlit as st
from database import register_user


def register_page():

    st.subheader("📝 Create Account")

    username = st.text_input(
        "Username",
        key="register_username"
    )

    email = st.text_input(
        "Email",
        key="register_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="register_password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        key="register_confirm_password"
    )

    if st.button(
        "Register",
        key="register_button"
    ):

        if (
            username.strip() == ""
            or email.strip() == ""
            or password == ""
            or confirm_password == ""
        ):
            st.error("Please fill all fields.")
            return

        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        success, message = register_user(
            username,
            email,
            password
        )

        if success:
            st.success(message)
        else:
            st.error(message)