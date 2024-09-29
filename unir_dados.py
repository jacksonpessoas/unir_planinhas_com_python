import pandas as pd
import os

# Defina o caminho onde as planilhas estão armazenadas
caminho_das_planilhas = '.'

# Crie uma lista para armazenar os DataFrames
planilhas = []

# Para cada arquivo no diretório
for arquivo in os.listdir(caminho_das_planilhas):
    if arquivo.endswith('.xlsx'):
        # Leia a planilha e adicione à lista, especificando a engine openpyxl
        df = pd.read_excel(os.path.join(caminho_das_planilhas, arquivo), engine='openpyxl')
        planilhas.append(df)

# Combine todas as planilhas em um único DataFrame
planilha_combinada = pd.concat(planilhas)

# Remova as linhas duplicadas com base nas colunas especificadas
planilha_combinada_sem_duplicatas = planilha_combinada.drop_duplicates(subset=['Nome', 'Contato', 'Endereco', 'Numero', 'Bairro', 'UF'])

# Salve a planilha combinada (com todas as colunas) em um novo arquivo Excel
planilha_combinada_sem_duplicatas.to_excel('planilha_combinada_sem_duplicatas.xlsx', index=False)

print("Planinha criada com sucesso!")