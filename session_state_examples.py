import streamlit as st

st.title('Counter Example')
if 'count_o' not in st.session_state:
    st.session_state.count_o = 0

increment = st.button('Increment')
if increment:
    st.session_state.count_o += 1

st.write('Count = ', st.session_state.count_o)

#------------------------------------------

st.title('Counter Example using Callbacks')
if 'count_c' not in st.session_state:
    st.session_state.count_c = 0

def increment_counter():
    st.session_state.count_c += 1

st.button('Increment using Callbacks', on_click=increment_counter)

st.write('Count = ', st.session_state.count_c)

#------------------------------------------

st.title('Counter Example using Callbacks with args')
if 'count_a' not in st.session_state:
    st.session_state.count_a = 0

increment_arg_value = st.number_input('Enter a value', value=0, step=1)

def increment_arg_counter(increment_arg_value):
    st.session_state.count_a += increment_arg_value

increment_a = st.button('Increment with args', on_click=increment_arg_counter,
    args=(increment_arg_value, ))

st.write('Count = ', st.session_state.count_a)

#------------------------------------------

st.title('Counter Example using Callbacks with kwargs')
if 'count_k' not in st.session_state:
    st.session_state.count_k = 0

def increment_kwargs_counter(increment_k_value=0):
    st.session_state.count_k += increment_k_value

def decrement_kwargs_counter(decrement_k_value=0):
    st.session_state.count_k -= decrement_k_value

st.button('Increment with Kwargs', on_click=increment_kwargs_counter,
	kwargs=dict(increment_k_value=5))

st.button('Decrement with Kwargs', on_click=decrement_kwargs_counter,
	kwargs=dict(decrement_k_value=1))

st.write('Count = ', st.session_state.count_k)

#------------------------------------------

import datetime

st.title('Counter with Date Example')
if 'count_d' not in st.session_state:
    st.session_state.count_d = 0
    st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.count_d += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time

with st.form(key='my_form'):
    st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
    st.number_input('Enter a value', value=0, step=1, key='increment_value')
    submit = st.form_submit_button(label='Update', on_click=update_counter)

st.write('Current Count = ', st.session_state.count_d)
st.write('Last Updated = ', st.session_state.last_updated)

#------------------------------------------

if "celsius" not in st.session_state:
    # set the initial default value of the slider widget
    st.session_state.celsius = 50.0

st.slider(
    "Temperature in Celsius",
    min_value=-100.0,
    max_value=100.0,
    key="celsius"
)

# This will get the value of the slider widget
st.write(st.session_state.celsius)
