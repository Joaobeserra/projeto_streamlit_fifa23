import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime
import os


st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

if "data" not in st.session_state:
    caminho_arquivo = os.path.join("dataset", "CLEAN_FIFA23_official_data.csv")
    df_data = pd.read_csv(caminho_arquivo, index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.write("# FIFA OFFICIAL DATASET ⚽")
st.sidebar.markdown("Desenvolvido por [João Vitor](https://www.linkedin.com/in/joaobeserra/)")
btn = st.button("Acesse os dados")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    O conjunto de dados que abrange o período de 2017 a 2023 concentra-se em fornecer uma 
    visão detalhada e abrangente do universo dos jogadores de futebol profissionais. 
    
    Nele, você encontrará uma extensa gama de informações, abrangendo desde dados demográficos 
    dos jogadores e características físicas até estatísticas de desempenho em partidas, detalhes contratuais e suas afiliações a clubes.

    Este conjunto de dados é verdadeiramente valioso, com **mais de 17.000 registros**, e é uma ferramenta indispensável para analistas de futebol, 
    pesquisadores e aficionados que desejam se aprofundar nos diversos aspectos do mundo do futebol. 
    
    Ele possibilita a exploração de uma variedade de temas, incluindo as características individuais dos jogadores, 
    métricas que revelam o desempenho em campo, a valoração de mercado dos atletas, análises sobre os clubes, 
    a posição tática dos jogadores e até mesmo o desenvolvimento ao longo do tempo de cada jogador.
    """
)