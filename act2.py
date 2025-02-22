import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Título de la app
st.title("Análisis de Datos con Gráficos")

# Cargar el dataset "tips" de Seaborn
df = sns.load_dataset("tips")

# Mostrar una tabla con los primeros datos
st.write("### Vista previa del dataset")
st.dataframe(df.head())

# 🔹 Gráfico 1: Histograma de Total Bill
st.write("### Distribución de Total Bill")
fig, ax = plt.subplots()
sns.histplot(df["total_bill"], bins=20, kde=True, color="blue", ax=ax)
st.pyplot(fig)

# 🔹 Gráfico 2: Boxplot de Total Bill por Día
st.write("### Total Bill por Día")
fig, ax = plt.subplots()
sns.boxplot(x=df["day"], y=df["total_bill"], palette="Set2", ax=ax)
st.pyplot(fig)

# 🔹 Gráfico 3: Relación entre Total Bill y Tip
st.write("### Relación entre Total Bill y Propina")
fig, ax = plt.subplots()
sns.scatterplot(x=df["total_bill"], y=df["tip"], hue=df["sex"], style=df["time"], ax=ax)
st.pyplot(fig)

# 🔹 Gráfico 4: Distribución de la Cuenta por Sexo
st.write("### Total Bill por Sexo")
fig, ax = plt.subplots()
sns.violinplot(x=df["sex"], y=df["total_bill"], palette="pastel", ax=ax)
st.pyplot(fig)
