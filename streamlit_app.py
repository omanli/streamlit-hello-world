import streamlit as st
import pandas as pd

def cb():
  global df
  df.Col3[4] += 1


st.write("""
# Hello, world!
Here is my *first* app
""")

st.write("Here is a Dataframe")
df = pd.DataFrame({"Col1": [1, 2, 3, 4, 5], "Col2": [4, 5, 6, 7, 8], "Col3": [7, 8, 9, 0, 1]})
st.write(df)


A = st.slider("Awesomeness", value=80, min_value=0, max_value=120, step=5, format="%d", on_change=cb)
if A > 90:
  st.write("Awesome!")

SD = st.checkbox("SuperDuper", value=False, on_change=None)
if SD:
  st.write("Yes!")
else:
  st.write("Are you sure this is not Super Duper?")
