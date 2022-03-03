import streamlit as st

st.write("""
# Hello, world!
Here is my *first* app
""")

v = st.slider("Awesomeness", min_value=0, max_value=120, step=5)
