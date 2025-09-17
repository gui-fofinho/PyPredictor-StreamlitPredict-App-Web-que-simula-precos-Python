import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('pizzas.csv') #importar o arquivo csv

 #parametros x , y   / treinamento do modelo              
modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]

#treinar modelo 
modelo.fit(x,y)

#criar web app

st.markdown(
    "<h1 style='text-align: center; color: #FF6347;'>Previsão de Preços de Pizzas 🍕</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr>", unsafe_allow_html=True)


diametro = st.number_input('Informe o diâmetro da pizza (cm):')

#teste do modelo
if diametro: 
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'O preço previsto para uma pizza de {diametro} cm é R$ {preco_previsto:.2f}')


