import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

    @st.cache_data(hash_funcs={"__main__.MyCustomClass": lambda x: hash(x.my_score)})
    def multiply_score(self, multiplier: int) -> int:
        return self.my_score * multiplier

initial_score = st.number_input("Enter initial score", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(score.multiply_score(multiplier))

#------------------------------------------

from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_data(hash_funcs={Person: lambda p: p.name})
def identity(person: Person):
    return person

person = identity(Person(name="Lee"))
st.write(f"The person is {person.name}")

#------------------------------------------

import streamlit as st
import tensorflow as tf

@st.cache_resource
def load_base_model(option):
    if option == 1:
        return tf.keras.applications.ResNet50(include_top=False, weights="imagenet")
    else:
        return tf.keras.applications.MobileNetV2(include_top=False, weights="imagenet")

@st.cache_resource
def load_layers(base_model):
    return [layer.name for layer in base_model.layers]

option = st.radio("Model 1 or 2", [1, 2])

base_model = load_base_model(option)

layers = load_layers(base_model)

st.write(layers)

#------------------------------------------

from datetime import datetime

import pytz
import streamlit as st

tz = pytz.timezone("Europe/Berlin")

@st.cache_data(hash_funcs={datetime: lambda x: x.strftime("%a %d %b %Y, %I:%M%p")})
def load_data(dt):
    return dt

now = datetime.now()
st.text(load_data(dt=now))

now_tz = tz.localize(datetime.now())
st.text(load_data(dt=now_tz))

#------------------------------------------

import time
import numpy as np
import pandas as pd

@st.cache_data
def get_data():
    df = pd.DataFrame({"num": [112, 112, 2, 3], "str": ["be", "a", "be", "c"]})
    return df

@st.cache_data(hash_funcs={np.ndarray: str})
def show_data(data):
    time.sleep(2)  # This makes the function take 2s to run
    return data

df = get_data()
data = df["str"].unique()

st.dataframe(show_data(data))
st.button("Re-run")

#------------------------------------------

@st.cache_resource
def create_list():
    l = [1, 2, 3]
    return l

l = create_list()
first_list_value = l[0]
l[0] = first_list_value + 1

st.write("l[0] is:", l[0])

#------------------------------------------