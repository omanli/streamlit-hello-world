import streamlit as st

st.write("""
# Hello, world!
Here is my *first* app
""")

A = st.slider("Awesomeness", value=80, min_value=0, max_value=120, step=5, format="d%", on_change=None)
if A > 90:
  st.write("Awesome!")

SD = st.checkbox("SuperDuper", value=False, on_change=None)
if SD:
  st.write("Yes!")
else:
  st.write("Are you sure this is not Super Duper?")
