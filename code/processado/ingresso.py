import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

ingresso = df_alunos.groupby(['periodo_ingresso','sexo']).size().reset_index().rename(columns={0:'contagem'}).sort_values('periodo_ingresso',ascending=False)
ingresso = ingresso.query("periodo_ingresso >= 2000.1")
#df_ingresso.to_csv('ingresso.csv') 
#files.download('ingresso.csv')