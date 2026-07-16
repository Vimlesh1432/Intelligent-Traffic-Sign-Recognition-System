import streamlit as st

st.set_page_config(
    page_title="Test",
    layout="wide"
)

st.sidebar.title("✅ Sidebar Test")
st.sidebar.write("Hello Vimlesh")

st.title("Main Page")
st.write("If sidebar is visible, Streamlit is working correctly.")