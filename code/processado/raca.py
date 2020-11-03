import pandas as pd
df_alunos = pd.read_csv("../dados/alunos_raiox.csv")

mulheres = df_alunos.query("periodo_ingresso >= 2000.1").query("sexo == 'Feminino'")
raca = mulheres[['periodo_ingresso','nome_cor']]
raca['periodo_ingresso'].astype(str)
raca.head()
#raca.to_csv('raca.csv') 
#files.download('raca.csv')