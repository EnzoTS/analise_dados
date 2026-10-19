import pandas as pd
import streamlit as st

st.set_page_config(page_title= "Mercado", layout="centered")

produtos = {"nome": ["Arroz", "Feijão", "Leite", "Bife", "Queijo"],
            "preco": [7.50, 6.00, 5.50, 10.00, 15.00]}

def somar_precos(selecionados, produtos):
    total = 0
    for nome, preco in zip(produtos["nome"], produtos["preco"]):
        if nome in selecionados:
            total += preco
    return total

select = st.multiselect("Escolha o produto",
                      (produtos["nome"]))

total = somar_precos(select, produtos)
st.write(f"Total: R$ {total}")

st.columns
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro número", value=0.0, step=1.0)

with col2:
    num2 = st.number_input("Segundo número", value=0.0, step=1.0)

calculo = st.selectbox("Escolha a operação a ser feita", ("adição", "subtração", "divisão", "multiplicação"))

resultado = 0

if st.button("Calcular", type="primary"):
     
     if calculo == "adição":
         resultado = num1 + num2
    
     if calculo == "subtração":
         resultado = num1 - num2

     if calculo == "divisão":
         if num2 == 0: 
             st.error("Não é possivel dividir por 0")
         resultado = num1 / num2

     if calculo == "multiplicação":
         resultado = num1 * num2

     if resultado is not None:
        st.success(f"**Resultado:** {resultado}")

if st.button("Comprar", type="primary"):
    if calculo == "adição":
         resultado = num1 + num2
    
    if calculo == "subtração":
         resultado = num1 - num2

    if calculo == "divisão":
         if num2 == 0: 
             st.error("Não é possivel dividir por 0")
         resultado = num1 / num2

    if calculo == "multiplicação":
         resultado = num1 * num2
    troco = resultado - total
    if troco >= 0:
        st.success(f"**Troco:** {troco}")
    
    else: st.success(f"**Não há troco**")