# Projeto de Consulta ao Clima com OpenWeatherMap

Este projeto consulta a API do [OpenWeatherMap](https://openweathermap.org/) para coletar informações sobre o clima atual da cidade de Passo Fundo. As informações obtidas incluem:
- Descrição do clima;
- Temperatura atual, sensação térmica, temperatura mínima e máxima (convertidas de Kelvin para Celsius);
- Pressão atmosférica;
- Humidade do ar;
- Velocidade do vento;
- Horários de gravação, nascer e pôr do sol.

Os dados são transformados em um *DataFrame* utilizando a biblioteca **pandas** e, em seguida, exportados para um arquivo CSV chamado `clima_atual_passo_fundo.csv`.

## Pré-requisitos

- Python
- Bibliotecas:
  - `pandas`
  - `requests`
- Uma conta no [OpenWeatherMap](https://openweathermap.org/) e uma API Key válida.
- Uma instância EC2 da Amazon (este projeto foi desenvolvido e testado em uma instância EC2).

## Configuração

1. Crie um arquivo chamado `credenciais.txt` na raiz do projeto e insira a sua API Key do OpenWeatherMap.
2. Certifique-se de que todas as bibliotecas necessárias estão instaladas. Caso contrário, instale-as utilizando:
   ```bash
   pip install pandas requests
