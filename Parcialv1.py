import streamlit as st
import seaborn as sns
import plotly.express as px

import pandas as pd
# Mostrar los datos en Streamlit
st.title("University Student Dashboard")

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

fig = px.bar(
    data_melted, 
    x="Year-Term", 
    y="Count", 
    color="Category", 
    barmode="group",
    title="Número de Aplicaciones, Admitidos y Matriculados por Año-Term",
    labels={'Count': 'Número de Estudiantes', 'Year-Term': 'Año y Term'}
)

fig.add_scatter(
    x=data_sorted['Year-Term'], 
    y=data_sorted['Retention Rate (%)'], 
    mode='lines+markers', 
    name='Retention Rate (%)', 
    yaxis='y2'
)

# Ajustar el diseño para doble eje Y
fig.update_layout(
    yaxis=dict(title='Número de Estudiantes'),
    yaxis2=dict(title='Retention Rate (%)', overlaying='y', side='right'),
    xaxis=dict(title='Año-Term'),
    legend_title="Categoría",
    template='plotly_white'
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
st.markdown("""
###  **1. Aumento en las Inscripciones**
- Las inscripciones a la universidad han **aumentado con el tiempo**, lo que muestra una **mayor popularidad** de la institución.

###  **2. Brecha entre Aplicaciones, Admitidos y Matriculados**
- Aunque los **admitidos y matriculados** han aumentado con los años, **no siguen la misma tendencia alcista** de las aplicaciones.

###  **3. Patrón de Admisiones por Período**
- **No se evidencian patrones distintos** entre los períodos de los años (**Spring y Fall**), lo que indica una distribución uniforme de admisiones.

### ⚠ **4. Caída en la Tasa de Retención en 2020**
- La tasa de **retención estudiantil fluctúa** hasta el año **2020**, donde tiene una **caída considerablemente grave**, posiblemente asociada a la **pandemia**.

###  **5. Recuperación de la Tasa de Retención**
- A partir de **2021**, la **tasa de retención aumenta sostenidamente**, indicando una posible **mejoría en estrategias institucionales**.
""")



