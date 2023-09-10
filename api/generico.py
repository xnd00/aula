##  pip install requests

import requests


# Exemplo de uma solicitação GET
url = 'https://api.estaleiroexemplo.com/recurso'
response = requests.get(url)

# Se a API requer autenticação, você pode passar credenciais da seguinte forma:
# response = requests.get(url, auth=('seu_usuario', 'sua_senha'))

# Se a API requer parâmetros na URL, você pode incluí-los assim:
# params = {'parametro1': 'valor1', 'parametro2': 'valor2'}
# response = requests.get(url, params=params)

if response.status_code == 200:  # Status de sucesso
    data = response.json()  # Supondo que a resposta é JSON
    # Faça algo com os dados retornados
    print(data)
else:
    print(f'A solicitação falhou com status {response.status_code}')
    print(response.text)  # Exibir o conteúdo da resposta em caso de erro
