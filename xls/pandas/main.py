## python -m venv colegios
## colegios/Scripts/Activate 
## deactivate
## pip install pandas
## pip install xlrd
"""
OBS.: Este projeto demonstra como trabalhar com arquivo xls. A biblioteca pandas permite trabalhar com esta extensão.
Outras bibliotecas podem permitir trabalhar somente com xlsx.
"""

import pandas as pd

from dados import info
caminho = info()[0]
arquivo = info()[1]


lido = pd.read_excel(f'{caminho}{arquivo}') 

# Criado esta variável para gerar um contador para linha da planilha
posicao = 0


# lento das as linhas da planilha
for i in lido:
    posicao = posicao + 1
    # Pegando a posição de cada coluna e mostrando o resultado de cada linha
    cpf = lido.iloc[posicao][0]
    nome = lido.iloc[posicao][1]
    sobrenome = lido.iloc[posicao][2]
    

    # imprimindo o resultado
    print(cpf , nome , sobrenome)




