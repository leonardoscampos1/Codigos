import streamlit as st
import pandas as pd
st.title('Dashboard BEES')
arquivo = pd.read_csv("Pedidos_Entregue_Rigarr.csv")
print(arquivo.head())