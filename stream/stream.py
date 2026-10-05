import pandas as pd
import streamlit as st

nome = "Enzo"
idade = "19"
st.write("Olá ", nome, idade)

df = pd.DataFrame({
   'first column': ["Português", "Matemática", "Python", "Frame"],
   'second column': [5, 9, 7, 10]
 })

st.title("Meu primeiro dash")
st.subheader("Enzo")

df

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