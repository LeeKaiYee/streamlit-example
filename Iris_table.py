import streamlit as st
import numpy as np
import pandas as pd

st.header("Iris")
st.write(pd.DataFrame({
    'Iris': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginaca']
}))

from PIL import Image
st.image(https://miro.medium.com/max/700/1*uo6VfVH87jRjMZWVdwq3Vw.png, caption='Iris')
