import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Graficos dom Streamlit")

st.header("Plotando Gráficos")
st.subheader("Grafico de Linha")
st.text("st.line_chart(data=None, *, x=None, y=None, width=0, height=0, use_container_width=True)")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.subheader("Grafico de Linha")
st.text("st.area_chart(data=None, *, x=None, y=None, width=0, height=0, use_container_width=True)")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.area_chart(chart_data)

st.subheader("Grafico de Barra")
st.text("st.bar_chart(data=None, *, x=None, y=None, width=0, height=0, use_container_width=True)")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])
st.bar_chart(chart_data)

st.subheader("Grafico Pyplot")
st.text("st.pyplot(fig=None, clear_figure=None, use_container_width=True, **kwargs)")
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)