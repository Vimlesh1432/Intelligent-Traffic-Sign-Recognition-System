import streamlit as st
from database import register_user


def register_page():

    st.subheader("📝 Create Account")

    username = st.text_input(
        "Username"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button(
        "Register",
        use_container_width=True
    ):

        if (
            username == ""
            or email == ""
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