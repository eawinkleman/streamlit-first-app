import streamlit as st
import pandas as pd

st.title("🎈 Basic Concepts Streamlit app")
st.write(
    "This app will showcase some basic Streamlit concepts. \n\n"
    "Help: [docs.streamlit.io](https://docs.streamlit.io/)."
)

#------------------------------------------------------------
st.write("**First Dataframe:**")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
#------------------------------------------------------------
st.write("**First attempt at using data to create a table using st.write:**")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
#------------------------------------------------------------
st.write("**Importing and using Numpy to generate a random sample to display:**")

import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
#------------------------------------------------------------
st.write("**Highlight demonstration & utilization of Panda Styler Objects:**")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
#------------------------------------------------------------
st.write("**Static table generation using st.table:**")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)
#------------------------------------------------------------
st.write("**Line Chart Example:**")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
#------------------------------------------------------------
st.write("**Map Example:**")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
#------------------------------------------------------------
st.write("**Widgits!**")

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
#------------------------------------------------------------
st.write("**Unique Widgit Keys:**")

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
#------------------------------------------------------------
st.write("**Checkbox to enable dataframe:**")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
#------------------------------------------------------------
st.write("**Selectbox:**")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
#------------------------------------------------------------
st.write("**Sidebar for Layout (Making the app look good and organized):**")
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write("^")
st.write("|-- click the arrow button on the left hand side!")
#------------------------------------------------------------
st.write("**Columns and with block:**")
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
#------------------------------------------------------------
st.write("**Is it time?**")

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'