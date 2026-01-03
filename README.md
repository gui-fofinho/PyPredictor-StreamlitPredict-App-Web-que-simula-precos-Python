# 🍕 Pizza Price Predictor com Machine Learning e Streamlit

Este projeto é uma **aplicação web interativa** que utiliza **Machine Learning** para prever o **preço de uma pizza** com base no seu **diâmetro**.

A aplicação foi desenvolvida em **Python**, utilizando **Streamlit** para a interface web e **Scikit-learn** para o modelo de regressão linear.

---

## 🚀 Como funciona

- O modelo é treinado com uma base de dados contendo:
  - diâmetro da pizza
  - preço correspondente
- O usuário informa o **diâmetro da pizza** na interface web
- O modelo de **Regressão Linear** calcula e exibe o **preço estimado**

---

## 🧠 Tecnologias utilizadas

- **Python**
- **Streamlit** (interface web)
- **Pandas** (manipulação de dados)
- **Scikit-learn** (Machine Learning)

---

## 📦 Estrutura do projeto

```text
📦 pizza-price-predictor-streamlit
 ┣ 📄 app.py
 ┣ 📄 pizzas.csv
 ┣ 📄 README.md
 ┣ 📄 pyproject.toml
 ┗ 📄 poetry.lock
 ```
 ## 📄 Descrição dos arquivos
 ```txt
app.py → Código principal da aplicação Streamlit

pizzas.csv → Base de dados usada para treinar o modelo

pyproject.toml / poetry.lock → Gerenciamento de dependências

README.md → Documentação do projeto
 ```
 
## ▶️ Como executar o projeto localmente

1️⃣ Instalar as dependências

Você pode usar pip:
 ```bash
pip install streamlit pandas scikit-learn
 ```

Ou, se preferir, Poetry:
 ```bash
poetry install
 ```
2️⃣ Executar a aplicação

⚠️ Importante: projetos Streamlit devem ser executados com streamlit run
 ```bash
streamlit run app.py
 ```

Após isso:
 ```txt
O navegador será aberto automaticamente
A aplicação estará pronta para uso
 ```
##🌐 Aplicação online

A aplicação também está disponível online no Streamlit Cloud:
 ```txt
👉 https://owner-avatar-python-ia-inteligencia-artificial-e-previsoes-6y3.streamlit.app/
 ```
 
## 📊 Modelo de Machine Learning
 ```txt
Tipo: Regressão Linear

Entrada: Diâmetro da pizza (cm)

Saída: Preço estimado (R$)

Este modelo é simples e didático, ideal para fins de aprendizado.
 ```

##📚 Observações
 ```txt
Projeto com fins educacionais

Ideal para quem está aprendendo:

Machine Learning

Streamlit

Criação de aplicações web simples com Python

Pode ser facilmente expandido com: novos dados, gráficos, outros modelos de regressão.
 ```

## 👨‍💻 Autor

Projeto desenvolvido por **Guilherme Matté**,
durante o curso da Hashtag Treinamentos,
com foco em aprendizado prático de Machine Learning e Streamlit.
