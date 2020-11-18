import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

mulheres = df_alunos.query("sexo == 'Feminino'").query("periodo_ingresso >= 2000.1")
cont_18 = mulheres['idade_ingresso'][mulheres['idade_ingresso'] == 18].count()
cont_geral = mulheres['idade_ingresso'].count()
porcentagem_18 = cont_18  * 100 / cont_geral  
print('A porcentagem das mulheres com 18 anos é', porcentagem_18.round(2))

um = (1 * 100) / cont_geral
print('A porcentagem de uma menina é', um.round(2))