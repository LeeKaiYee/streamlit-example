import streamlit as st
import numpy as np
import pandas as pd

st.header("Iris")
st.write(pd.DataFrame({
    'Iris': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginaca']
}))

from PIL import Image
image = Image.open('Iris Setosa, Versicolor, Virginica.png')

st.image(image, caption='Iris')
