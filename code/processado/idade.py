import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

alunos = df_alunos.query("periodo_ingresso >= 2000.1")
alunos = alunos.query("sexo == 'Feminino'")
idade = alunos.groupby(['periodo_ingresso'])['idade_ingresso'].mean().astype(int).reset_index()

idade.to_csv('idade.csv') 
files.download('idade.csv')