import streamlit as st
import numpy as np
import pandas as pd

st.header("Iris")
st.write(pd.DataFrame({
    'Iris': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginaca']
}))