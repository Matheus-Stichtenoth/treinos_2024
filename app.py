import streamlit as st
import pandas as pd
import datetime
import os
import plotly.express as px
from interface_gui import page_gui

st.title('Rastreador de Treinos')

tab_gui, tab_teteu = st.tabs(["Guilherme", "Matheus"])

with tab_gui:
    page_gui()
with tab_teteu:
    st.write("Em breve!")