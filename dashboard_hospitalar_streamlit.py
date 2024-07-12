import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Dados fictícios para os meses de janeiro a junho de 2024
data = {
    'Month': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Occupancy Rate': [80, 85, 75, 90, 95, 88],
    'Infection Rate': [2, 1.8, 2.5, 2.2, 2, 1.5],
    'Mortality Rate': [1, 1.2, 1.1, 1.5, 1.3, 1.2],
    'Satisfaction Rate': [90, 92, 85, 88, 91, 89],
    'Vaginal Births': [150, 160, 145, 170, 165, 155],
    'C-sections': [80, 85, 78, 90, 88, 84],
    'Surgeries': [120, 130, 125, 140, 135, 128]
}

df = pd.DataFrame(data)

# Título do aplicativo com logo
col1, col2 = st.columns([1, 8])
with col1:
    st.image("logo.jpeg", width=50)
with col2:
    st.title("NQSP - Gestão de Indicadores")

metrics = ['Occupancy Rate', 'Infection Rate', 'Mortality Rate', 'Satisfaction Rate', 'Vaginal Births', 'C-sections', 'Surgeries']
titles = ['Taxa de Ocupação', 'Taxa de Infecção', 'Taxa de Mortalidade', 'Taxa de Satisfação', 'Partos Vaginais', 'Partos Cesáreos', 'Quantidade de Cirurgias']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Criando gráficos de colunas para cada métrica
for i, metric in enumerate(metrics):
    fig = go.Figure()
    for j, month in enumerate(df['Month']):
        fig.add_trace(go.Bar(x=[month], y=[df[metric][j]], marker_color=colors[j], name=month))
    
    fig.update_layout(title=titles[i], xaxis_title='Mês', yaxis_title='Valor')
    st.plotly_chart(fig)
