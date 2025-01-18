import streamlit as st
import pandas as pd
from datetime import datetime

# Inicializar as variáveis de sessão se ainda não estiverem definidas
if 'receitas' not in st.session_state:
    st.session_state.receitas = []
if 'despesas' not in st.session_state:
    st.session_state.despesas = []
if 'dividas' not in st.session_state:
    st.session_state.dividas = []

# Função para adicionar receitas, despesas e dívidas
def adicionar_transacao(tipo, descricao, valor, data):
    # Formatar a data para o formato dd/mm/aaaa
    data_formatada = data.strftime('%d/%m/%Y')
    
    if tipo == "Receita":
        st.session_state.receitas.append({"Data": data_formatada, "Descrição": descricao, "Valor": valor})
    elif tipo == "Despesa":
        st.session_state.despesas.append({"Data": data_formatada, "Descrição": descricao, "Valor": valor})
    elif tipo == "Dívida":
        st.session_state.dividas.append({"Data": data_formatada, "Descrição": descricao, "Valor": valor})

# Função para gerar o resumo
def gerar_resumo():
    # Calculando o total de receitas, despesas e dívidas
    total_receitas = sum([r["Valor"] for r in st.session_state.receitas])
    total_despesas = sum([d["Valor"] for d in st.session_state.despesas])
    total_dividas = sum([d["Valor"] for d in st.session_state.dividas])
    
    saldo = total_receitas - total_despesas - total_dividas

    resumo = {
        "Total de Receitas": total_receitas,
        "Total de Despesas": total_despesas,
        "Total de Dívidas": total_dividas,
        "Saldo Atual": saldo
    }
    
    return resumo

# Função para exibir as transações
def exibir_transacoes():
    st.subheader("Receitas")
    st.write(pd.DataFrame(st.session_state.receitas))
    
    st.subheader("Despesas")
    st.write(pd.DataFrame(st.session_state.despesas))
    
    st.subheader("Dívidas")
    st.write(pd.DataFrame(st.session_state.dividas))

# Título da aplicação
st.title("Organizador Financeiro")

# Formulário de entrada
st.header("Adicionar Transação")
tipo_transacao = st.selectbox("Tipo de Transação", ["Receita", "Despesa", "Dívida"])
descricao = st.text_input("Descrição")
valor = st.number_input("Valor", min_value=0.01, format="%.2f")
data = st.date_input("Data da Transação", datetime.today())

# Exibir a data no formato dd/mm/yyyy no campo de input
st.write(f"Data Selecionada: {data.strftime('%d/%m/%Y')}")

if st.button("Adicionar Transação"):
    if descricao and valor > 0:
        adicionar_transacao(tipo_transacao, descricao, valor, data)
        st.success(f"Transação de {tipo_transacao} adicionada com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos corretamente.")

# Exibir resumo financeiro
st.header("Resumo Financeiro")
resumo = gerar_resumo()
st.write(pd.DataFrame([resumo]))

# Exibir transações
exibir_transacoes()
