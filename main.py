import json                           #IMPORTANDO AS BIBLIOTECAS
from datetime import datetime
import pandas as pd
import requests

# MONTANDO O URL DA API
nome_cidade = "Passo Fundo"        
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

with open("credenciais.txt", 'r') as f:
    api_key = f.read()

def kelvin_para_cel(temp_in_kelvin):            #FUNÇÃO PARA CONVERTER OS GRAUS DE KELVIN PARA CELCIUS
    temp_in_cel = (temp_in_kelvin - 273)
    return temp_in_cel

url_completo = base_url + nome_cidade + "&APPID=" + api_key #URL COMPLETO É UMA JUNÇÃO DE TODOS ESSES

r = requests.get(url_completo)
dados = r.json()
#print(dados)

#ATRIBUINDO OS DADOS DO ARQUIVO JSON PARA VARIAVEIS
cidade = dados["name"]
descrição_do_clima = dados["weather"][0]["description"]
temperatura = kelvin_para_cel(dados["main"]["temp"])
sensacao_clima = kelvin_para_cel(dados["main"]["feels_like"])
min_temp = kelvin_para_cel(dados["main"]["temp_min"])
max_temp = kelvin_para_cel(dados["main"]["temp_max"])
pressao = dados["main"]["pressure"]
humidade = dados["main"]["humidity"]
velocidade_vento = dados["wind"]["speed"]
hora_gravacao = datetime.fromtimestamp(dados["dt"] + dados["timezone"])
nascer_sol = datetime.fromtimestamp(dados["sys"]["sunrise"] + dados["timezone"])
por_sol = datetime.fromtimestamp(dados["sys"]["sunset"] + dados["timezone"])


#COLOCANDO OS DADOS EM UM DICIONARIO PARA TRANSFORMAR EM UM DATAFRAME DEPOIS
dados_transformados = {"Cidade": cidade,
                       "Descrição": descrição_do_clima,
                       "Temperatura C°": temperatura,
                       "Sensação Térmica C°": sensacao_clima,
                       "Temperatura Minima C°": min_temp,
                       "Temperatura Maxima C°": max_temp,
                       "Pressão Atmosferica": pressao,
                       "Humidade do Ar:":humidade,
                       "Velocidade do Vento": velocidade_vento,  
                       "Momento da Gravação": hora_gravacao,
                       "Nascer do Sol": nascer_sol,
                       "Por do Sol": por_sol
                       }

dados_transformados_lista = [dados_transformados]
df_dados = pd.DataFrame(dados_transformados_lista)

df_dados.to_csv("clima_atual_passo_fundo.csv", index = False)  #INDEX = FALSE PARA NÃO CRIAR O INDEX DO DATAFRAME NO ARQUIVO