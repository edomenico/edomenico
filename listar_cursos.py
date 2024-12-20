"""Página de Listagem de Cursos."""



def listar():
    import pandas as pd
    import streamlit as st
    """Função de Listar Cursos."""
    st.title("Listagem de TAF")
    try:
        st.dataframe(pd.read_csv("taf.csv"))
    except:
        st.warning("Nenhum curso dísponível encontrado!")
