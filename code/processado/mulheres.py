import pandas as pd
df_alunos = pd.read_csv("../dados/alunos_raiox.csv")

mulheres = df_alunos.query("sexo == 'Feminino'")
#mulheres.to_csv('mulheres.csv') 
#files.download('mulheres.csv')