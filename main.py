import requests, json

iso2_identifiers = []

try:
    r = requests.get('https://servicodados.ibge.gov.br/api/v1/paises/')
except requests.ConnectionError:
    print("Erro ao adquirir dados da API")
    exit()

output = json.loads(r.content)

for dados in output:
    iso2_identifiers.append(dados['id']['ISO-3166-1-ALPHA-2'])

print(iso2_identifiers)
print(len(iso2_identifiers))