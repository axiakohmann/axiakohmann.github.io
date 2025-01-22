import streamlit as st
import pandas as pd
import os
import random
from compare import *
from alter import *

pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.float_format = "{:,.2f}".format
st.set_page_config(layout='wide')

def intro():
    import streamlit as st

    st.write("# Bem vindo ao Nutrição APP 👋")
    st.sidebar.success("Escolha uma das opções de visualização")

    st.markdown(
        """
        Esse é um APP em desenvolvimento para auxiliar na alteração e comparação de preços

        **👈 Selecione uma das opções à esquerda** 

        ### Tem sugestão de melhorias?

        Estou sempre disponível para ouvir 😊

    """
    )

antes='Dez'
depois='Jan'

page_names_to_funcs = {
    "Intro": intro,
    "Comparação": plotting_demo,
    "Alteração de dados": alter_demo
}

demo_name = st.sidebar.selectbox("Escolha função", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
