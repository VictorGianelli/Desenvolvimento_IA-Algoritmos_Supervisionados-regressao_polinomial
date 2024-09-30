# Construindo Front-end
import streamlit as st
import json
import requests

# Título da Aplicação

st.title("Modelo Predição de Salário")

# Inputs

st.write("Há quantos meses o profissional está na sua empresa?")
tempo_na_empresa = st.slider("Meses", min_value=1, max_value=120, value=60, step=1)

st.write("Qual o nível do profissional na empresa?")
nivel_na_empresa = st.slider("Nível", min_value=1, max_value=10, value=5, step=1)

# Preparar dados para API

input_features = {
    'tempo_na_empresa': tempo_na_empresa,
    'nivel_na_empresa': nivel_na_empresa
}

# Criar um botão de captura de evento deste botão
if st.button('Estimar salário'):
    res = requests.post(url='http://localhost:8000/predict', data=json.dumps(input_features))

    res_json = json.loads(res.text)
    # salario_em_reais = round(res_json, 2)
    # index = res_json.index('salario_em_reais')
    print("-------------------------")
    print(res_json)
    # print(salario_em_reais)
    # st.subheader(f'O salário estimado é de R$ {salario_em_reais}')
    st.subheader(f'O salário estimado é de R$ {res_json}')

# Nesta aula, vamos preparar os dados para a API e construir a aplicação no Streamlit. Vamos importar o Streamlit, o módulo JSON e o módulo Requests. Em seguida, vamos criar um título para a aplicação e definir um formulário com as entradas do usuário, como a quantidade de meses e o nível do profissional. Usaremos um slider para permitir que o usuário selecione o número de meses e um input para o nível do profissional. Depois criaremos um botão e definir a ação que esse botão irá executar. Vamos chamar uma API usando o módulo Requests e exibir o resultado na tela. Para capturar o evento do botão, utilizamos um if para verificar se o botão foi clicado. Em seguida, chamamos a API usando o método POST do Requests, passando a URL e os dados em formato JSON. O resultado é armazenado na variável REST e convertido para um dicionário JSON. Por fim, exibimos o valor do salário estimado na tela usando o st.subheader.