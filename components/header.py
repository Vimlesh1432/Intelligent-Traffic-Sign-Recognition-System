import streamlit as st


def header():

    col1, col2 = st.columns([7, 3])

    with col1:
        st.markdown(
            """
            <h1 style='margin-bottom:0;color:white;'>
            🚦 Intelligent Traffic Sign Recognition System
            </h1>

            <p style='font-size:18px;color:#cbd5e1;margin-top:5px;'>
            AI Powered Traffic Sign Detection & Analytics
            </p>
            """,
            unsafe_allow_html=True
        )

    with col2:

        if st.session_state.get("logged_in"):

            st.markdown(
                f"""
                <div style="
                    text-align:right;
                    padding-top:20px;
                ">

                <h3 style="color:white;">
                    👤 {st.session_state.user["username"]}
                </h3>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()