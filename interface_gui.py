import streamlit as st
import pandas as pd
import datetime
import os
import plotly.express as px
import base64

# Arquivo para salvar os dados
DATA_FILE = "data/treinos_gui.csv"

def page_gui():

    # Função para carregar ou criar o arquivo de dados
    def load_data():
        if os.path.exists(DATA_FILE):
            return pd.read_csv(DATA_FILE)
        else:
            df = pd.DataFrame(columns=["Pessoa","Data", "Tipo"])
            df.to_csv(DATA_FILE, index=False)
            return df

    # Função para salvar os dados
    def save_data(data):
        df = load_data()
        df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)

    # Carregar dados
    df = load_data()


    # Caminho da imagem
    image_path = "data/foto_gui.png"

    # Função para converter imagem para Base64
    def get_image_base64(image_path):
        with open(image_path, "rb") as file:
            encoded_image = base64.b64encode(file.read()).decode()
        return encoded_image

    # Codificar a imagem
    image_base64 = get_image_base64(image_path)

    # Inserir a imagem no canto superior direito usando HTML
    st.markdown(
        f"""
        <style>
        .img-right {{
            position: absolute;
            top: 20px;
            right: 20px;
            width: 100px;
            height: auto;
            border-radius: 10px; /* Arredonda as bordas */
        }}
        </style>
        <img src="data:image/png;base64,{image_base64}" class="img-right">
        """,
        unsafe_allow_html=True
    )

    # Interface do Streamlit
    st.title("Guilherme Stick")

    # Registrar treino
    st.header("Registrar Treino")
    pessoa = 'Guilherme'
    col_1, col_2 = st.columns(2)

    with col_1:
        tipo = st.selectbox("Tipo de Treino", ["Musculação", "Jiu-Jitsu"])
    with col_2:
        data = st.date_input("Data", datetime.date.today())

    if st.button("Salvar Treino"):
        save_data([{"Pessoa": pessoa,"Data": str(data), "Tipo": tipo}])
        st.success("Treino registrado com sucesso!")

    # Visualizar progresso
    st.header("Progresso")
    st.write("Treinos Registrados:")
    st.dataframe(df)

    # Gráficos
    st.subheader("Gráficos de Progresso")
    if not df.empty:
        treinos_por_tipo = df["Tipo"].value_counts()
        st.bar_chart(treinos_por_tipo)
    else:
        st.info("Nenhum treino registrado ainda.")