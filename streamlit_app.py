import streamlit as st
import pandas as pd
from numpy.random import randint

@st.cache(allow_output_mutation=True)
def load_data():
  D = pd.DataFrame({"Col1": [1, 2, 3, 4, 5], "Col2": [4, 5, 6, 7, 8], "Col3": [7, 8, 9, 0, randint(0,10)]})
  return D


def cb(d):
  global df, dfo, A
  df.Col1[0] = A
  df.Col3[4] += int(d)
  with dfo:
    st.write(df)


df = load_data()
dfo = None


st.write("""
# Hello, world!
Here is my *first* app
""")

st.write("Here is a Dataframe")
dfo = st.empty()
with dfo:
  st.write(df)

A = st.slider("Awesomeness", value=80, min_value=0, max_value=120, step=5, format="%d")
cb(0)
if A > 90:
  st.write("Awesome!")
else:
  st.write("meh..")

SD = st.checkbox("SuperDuper", value=False, on_change=None)
if SD:
  st.write("Yes!")
else:
  st.write("Are you sure this is not Super Duper?")

delta = st.radio("Col3[-1] delta change:",
                 ('-5', '-1', '+1', '+5'))

if st.button('Call cb'):
  cb(delta)

