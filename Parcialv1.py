import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/Clauelenar/ejemplo2/refs/heads/main/university_student_dashboard_data.csv"

# Cargar los datos desde GitHub
@st.cache_data
def load_data(url):
    return pd.read_csv(url)

# Cargar los datos
data = load_data(url)

# Mostrar los datos en Streamlit
st.title("📊 University Student Dashboard")

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


