import streamlit as st


def apply_theme():

    st.markdown("""
    <style>

    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    .stApp{

        background:linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #1d4ed8);

    }

    .block-container{

        padding-top:2rem;
        padding-left:3rem;
        padding-right:3rem;

    }

    div[data-testid="metric-container"]{

        background:white;

        padding:20px;

        border-radius:18px;

        border:none;

        box-shadow:0 8px 20px rgba(0,0,0,.20);

    }

    .stButton>button{

        border-radius:12px;

        height:45px;

        font-weight:bold;

        width:100%;

    }

    </style>
    """,
    unsafe_allow_html=True)