import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
# Mostrar los datos en Streamlit
st.title("📊 University Student Dashboard")

file_path = "university_student_dashboard_data.csv"
data = pd.read_csv(file_path)

# Título de la app
st.title("Análisis de Admisiones.")

data_sorted = data.sort_values(by=['Year', 'Term'], ascending=[True, False])

# **Crear la columna 'Year-Term' asegurando el orden correcto**
data_sorted['Year-Term'] = data_sorted['Year'].astype(str) + " " + data_sorted['Term']

# **Convertir 'Year-Term' en un tipo categórico con el orden exacto**
data_sorted['Year-Term'] = pd.Categorical(data_sorted['Year-Term'], 
                                          categories=data_sorted['Year-Term'].unique(), 
                                          ordered=True)

# **Reestructurar el DataFrame para poder agrupar las categorías en barras**
data_melted = data_sorted.melt(id_vars=['Year-Term', 'Retention Rate (%)'], 
                               value_vars=['Applications', 'Admitted', 'Enrolled'], 
                               var_name='Category', value_name='Count')


