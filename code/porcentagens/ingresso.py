import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

df_geral = df_alunos.query("periodo_ingresso >= 2000.1")
geral = df_geral.groupby(['periodo_ingresso']).size().reset_index().rename(columns={0:'geral'})
mulheres = df_geral.query("sexo == 'Feminino'").groupby(['periodo_ingresso']).size().reset_index().rename(columns={0:'mulheres'})
df_ingresso = geral.join(mulheres['mulheres'])
df_ingresso.mulheres = df_ingresso.mulheres.fillna(0.0).astype(int)
df_ingresso.periodo_ingresso = df_ingresso.periodo_ingresso.astype(str)

df_ingresso['porcentagem_mulheres'] = df_ingresso['mulheres']/df_ingresso['geral']*100
df_ingresso['porcentagem_mulheres'] = df_ingresso['porcentagem_mulheres'].round(2)

media_geral = df_ingresso['porcentagem_mulheres'].sum() / df_ingresso['porcentagem_mulheres'].count()
print('Media ingresso geral:', media_geral.round(2))

antes_2007 = df_ingresso.query("periodo_ingresso < '2007.1'")
media_antes = antes_2007['porcentagem_mulheres'].sum() / antes_2007['porcentagem_mulheres'].count()
print('Media ingresso antes de 2007.1:', media_antes.round(2))

depois_2007 = df_ingresso.query("periodo_ingresso >= '2007.1'")
media_depois = depois_2007['porcentagem_mulheres'].sum() / depois_2007['porcentagem_mulheres'].count()
print('Media ingresso a partir de 2007.1:', media_depois.round(2))