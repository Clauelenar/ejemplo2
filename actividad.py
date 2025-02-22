import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Gráfico Simple con Streamlit")

# Cargar datos desde GitHub (IMPORTANTE: Usa el enlace 'Raw')
url = "https://raw.githubusercontent.com/giuliannaac/ejercicio/main/Credit.csv"
df = pd.read_csv(url)

# Graficar un histograma de la variable 'Balance'
st.write("### Distribución de la Variable Balance")
fig, ax = plt.subplots()
sns.histplot(df["Balance"], bins=30, kde=True, color="blue", ax=ax)
st.pyplot(fig)
