import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

mulheres = df_alunos.query("periodo_ingresso >= 2000.1").query("sexo == 'Feminino'")
raca = mulheres[['periodo_ingresso','nome_cor']]
raca['periodo_ingresso'].astype(str)

raca.to_csv('raca.csv') 
files.download('raca.csv')