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

