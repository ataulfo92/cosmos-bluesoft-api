import requests
import json

url = "https://api.cosmos.bluesoft.com.br/gtins/7898917991145.json"

querystring = {"barcode":"7898917991145"}

headers = {
          'X-Cosmos-Token': 'SEU_TOKEN_DE_ACESSO',
          'Content-Type': 'application/json',
          'User-Agent': 'Cosmos-API-Request'
}

response = requests.get(url, headers=headers, params=querystring)
meu_dicionario = json.loads(response.content)

print(meu_dicionario)
