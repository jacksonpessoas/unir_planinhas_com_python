# VISÃO GERAL

Este projeto combina várias planilhas Excel em um único arquivo, removendo duplicatas com base em colunas específicas. É útil para consolidar dados de diferentes fontes e garantir que não haja registros duplicados.

### PRÉ-REQUISITOS

Certifique-se de ter o Python instalado e as seguintes bibliotecas:

- **pandas**: Para manipulação de dados em planilhas Excel.
- **openpyxl**: Para leitura de arquivos Excel.

Para instalar as bibliotecas necessárias, execute:

```bash
pip install pandas openpyxl
```

### FUNCIONAMENTO DO CODIGO
1. Leitura de Planilhas: O código lê todos os arquivos .xlsx do diretório atual.

2. Combinação de Dados: Combina os dados de todas as planilhas em um único DataFrame.

3. Remoção de Duplicatas: Remove linhas duplicadas com base nas colunas Nome, Contato, Endereco, Numero, Bairro e UF.

4. Salvamento: Salva a planilha combinada (sem duplicatas) em um novo arquivo Excel chamado planilha_combinada_sem_duplicatas.xlsx.

### COMO EXECUTAR
- Coloque todas as planilhas Excel que deseja combinar no mesmo diretório do script.
- Execute o script Python:

```
unir_dados.py 
```

### RESULTADO
Após a execução do script, um novo arquivo chamado planilha_combinada_sem_duplicatas.xlsx será criado no diretório, contendo todos os dados combinados sem duplicatas.

#### TÓPICOS
[VISÃO GERAL](##visão-geral), [PRÉ REQUISITOS](##pré-requisitos), [FUNCIONAMENTO DO CODIGO](##funcionamento-do-codigo), [COMO EXECUTAR](##como-executar), [RESULTADO](##resultado)


## Criado por

JacksonPessoaS 

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jacksonpessoas)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jackson-pessoa-soares)


Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato!
