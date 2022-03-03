import streamlit as st

st.write("""
# Hello, world!
Here is my *first* app
""")

A = st.slider("Awesomeness", min_value=0, max_value=120, step=5, on_change=None)

SD = st.checkbox("SuperDuper", value=False, on_change=None)
