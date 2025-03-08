import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

import requests
from io import StringIO
import streamlit as st

def load_original_data():
    url = 'https://raw.githubusercontent.com/Clauelenar/ejemplo2/refs/heads/main/university_student_dashboard_data.csv'
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
        return None

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


