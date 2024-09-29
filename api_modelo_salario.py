# Construção da API do Modelo
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe com os dados de entrada que virão no request body com os tipos esperados
class request_body(BaseModel):
    tempo_na_empresa: int
    nivel_na_empresa: int


# Carregar model para realizar predição
modelo_poly = joblib.load('./modelo_salario.pkl')


@app.route('/predict')
def predict(data: request_body):
    input_features = {
        'tempo_na_empresa': data.tempo_na_empresa,
        'nivel_na_empresa': data.nivel_na_empresa
    }

    pred_df = pd.DataFrame(input_features, index=[1])

    y_pred = modelo_poly.predict(pred_df)[0].astype(float)

    return {'salario_em reais': y_pred.tolist()}

# Nesta aula, vamos aprender como entregar um modelo de machine learning através de uma aplicação usando o Streamlit. Vamos criar uma API usando o FastAPI para receber os dados de entrada, carregar o modelo treinado e fazer a predição. Para isso, vamos importar as bibliotecas necessárias, criar uma instância do FastAPI, definir a classe para validação dos dados de entrada e criar a função de predição. Por fim, vamos decorar a função com o decorador do FastAPI para expor a função como uma API REST.