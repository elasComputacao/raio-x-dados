import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

mulheres = df_alunos.query("sexo == 'Feminino'")
mulheres.to_csv('mulheres.csv') 
files.download('mulheres.csv')