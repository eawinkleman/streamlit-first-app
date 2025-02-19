import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 Advanced Concepts Streamlit app")
st.write(
    "This app will showcase some more advanced Streamlit concepts. \n\n"
    "Help: [docs.streamlit.io](https://docs.streamlit.io/)."
)

#------------------------------------------------------------
# Caching template example
"""
@st.cache_data
def long_running_function(param1, param2):
    return …
"""

st.write("**Session State:**")

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")
#------------------------------------------------------------
st.write("**Session State Randomization:**")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)
#------------------------------------------------------------
st.write("**Database queries (SQL):**")

conn = st.connection("my_database")
df = conn.query("select * from my_table")
st.dataframe(df)