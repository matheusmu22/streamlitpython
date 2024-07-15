import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Dados dos meses de janeiro a junho de 2024
data = {
    'Month': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Occupancy Rate': [56.14, 59.85, 62.22, 64.07, 63.24, 64.82],
    'Infection Rate': [0.21, 0.53, 0.47, 0.10, 0.41, 0.71],
    'Mortality Rate': [1.66, 1.05, 1.97, 2.10, 2.27, 1.90],
    'Satisfaction Rate': [88.00, 87.62, 90.30, 89.29, 90.40, 79.88],
    'Vaginal Births': [86, 102, 110, 87, 113, 89],
    'C-sections': [139, 144, 133, 112, 135, 95],
    'Surgeries': [586, 583, 607, 593, 608, 0]
}

df = pd.DataFrame(data)

# Título do aplicativo com logo
col1, col2 = st.columns([1, 8])
with col1:
    st.image("NQSP.jpeg", width=50)
with col2:
    st.title("NQSP - Gestão de Indicadores")

metrics = ['Occupancy Rate', 'Infection Rate', 'Mortality Rate', 'Satisfaction Rate', 'Vaginal Births', 'C-sections', 'Surgeries']
titles = ['Taxa de Ocupação', 'Taxa de Infecção', 'Taxa de Mortalidade', 'Taxa de Satisfação', 'Partos Vaginais', 'Partos Cesáreos', 'Procedimentos Cirúrgicos']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Criando gráficos de colunas para cada métrica
for i, metric in enumerate(metrics):
    fig = go.Figure()
    for j, month in enumerate(df['Month']):
        fig.add_trace(go.Bar(x=[month], y=[df[metric][j]], marker_color=colors[j], name=month))
    
    fig.update_layout(title=titles[i], xaxis_title='Mês', yaxis_title='Valor')
    st.plotly_chart(fig)
