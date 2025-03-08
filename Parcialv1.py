import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Título de la app
st.title("Análisis de Admisiones")
data= pd.read_csv('/content/university_student_dashboard_data.csv')
data.head()
