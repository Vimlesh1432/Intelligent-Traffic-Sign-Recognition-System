from pathlib import Path
import streamlit as st


def load_css(css_path):
    css_file = Path(css_path)

    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    else:
        st.warning(f"CSS file not found: {css_path}")