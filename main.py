import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("#Assalomu alaykum")

df = pd.read_csv('world_smoking_history_1924_2023.csv')
st.line_chart(df)