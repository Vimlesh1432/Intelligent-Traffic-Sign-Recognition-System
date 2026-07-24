import streamlit as st

def header():
    # Wrap the entire header in a glass card
    
    # Ab hum sirf ek column use karenge taaki title left mein rahe aur right side khali ho jaye
    st.markdown(
        """
        <div style="text-align: left;">
            <h1 style='margin: 0; font-size: 28px; font-weight: 800; color: white; line-height: 1.2;'>
                Intelligent Traffic Sign Recognition System
            </h1>
            <p style='font-size: 16px; color: rgba(255, 255, 255, 0.7); margin-top: 8px;'>
                AI Powered Traffic Sign Detection & Analytics
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)