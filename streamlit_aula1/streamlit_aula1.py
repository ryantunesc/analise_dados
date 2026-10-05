import streamlit as st
import pandas as pd

st.title("Meu primeiro dash")
st.subheader("Ryan")

st.write("Olá, mundo")

nome = "Ryan"
idade = 18
st.write(nome, idade)

df = pd.DataFrame({
    'first column': ['Português', 'Matemática', 'Python', 'Frame'],
    'second column': [5, 9, 7, 10]
})

st.write(df)

precos_produtos = {
    "Batata": 4.50,
    "Arroz": 22.00,
    "Feijão": 7.50,
    "Leite": 5.20
}

item_selecionado = st.selectbox("Selecione um item do mercado:", list(precos_produtos.keys()))

quantidade = st.number_input("Digite a quantidade:", min_value=1, value=1, step=1)

def calcular_preco(item, qtd):
    preco_unitario = precos_produtos[item]
    return preco_unitario * qtd

total = calcular_preco(item_selecionado, quantidade)
st.write(f"O preço total de compra para {quantidade}x {item_selecionado} é: R$ {total:.2f}")
