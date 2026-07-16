import streamlit as st


def apply_theme():

    st.markdown(
        """
<style>

/* Hide Streamlit */

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

/* Main App */

.stApp{

background:linear-gradient(
135deg,
#0f172a,
#1e293b,
#1e3a8a);

}

/* Metric Cards */

[data-testid="metric-container"]{

background:white;

padding:20px;

border-radius:18px;

border:none;

box-shadow:0 10px 25px rgba(0,0,0,.2);

}

/* Buttons */

.stButton>button{

width:100%;

border-radius:12px;

height:45px;

font-weight:bold;

}



</style>

""",
        unsafe_allow_html=True,
    )