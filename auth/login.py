import streamlit as st
from database import login_user


def login_page():

    st.subheader("🔐 Login")

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        if email == "" or password == "":
            st.error("Please fill all fields.")
            return

        success, response = login_user(
            email,
            password
        )

        if success:

            st.session_state.logged_in = True

            st.session_state.user = response

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error(response)