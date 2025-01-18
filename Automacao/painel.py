import streamlit as st
import pandas as pd
import yfinance as yf

# Título
st.title('Painel de Ações')
codigo = input('Digite o código da ação: ')
# Sidebar
st.sidebar.title('Configurações')
st.sidebar.subheader('Selecione a Ação')
acao = st.sidebar.text_input('Código da Ação',{codigo} )

# Busca a ação
ticker = yf.Ticker(acao)
df = ticker.history(period='1d')

# Exibe os dados
st.write(df)

#Para executar o código, basta salvar o arquivo e executar o comando `streamlit run painel.py` no terminal. Isso abrirá um servidor local e exibirá o painel no navegador.