import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Gráfico Simple con Dataset de Seaborn")

# Cargar un dataset incluido en Seaborn
df = sns.load_dataset("tips")

# Graficar un histograma de la columna 'total_bill'
st.write("### Distribución de Total Bill")
fig, ax = plt.subplots()
sns.histplot(df["total_bill"], bins=20, kde=True, color="blue", ax=ax)
st.pyplot(fig)
