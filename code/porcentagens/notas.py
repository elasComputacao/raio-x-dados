import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

geral = df_alunos.query("periodo_ingresso >= 2000.1").query("apv_media_geral != 'NaN'").query("apv_media_geral != '0.0'")
mulheres = geral.query("sexo == 'Feminino'")
mulheres = mulheres.groupby(['periodo_ingresso'])['apv_media_geral'].mean().round(2)

mulheres = mulheres.to_frame('media_mulheres').reset_index()

geral = geral.groupby(['periodo_ingresso'])['apv_media_geral'].mean().round(2)
geral = geral.to_frame('media_geral').reset_index()

nota_geral = geral.join(mulheres['media_mulheres'])

media_total_mulheres = nota_geral['media_mulheres'].sum() / nota_geral['media_mulheres'].count()
print('A média total das mulheres é', media_total_mulheres.round(2))

media_total = nota_geral['media_geral'].sum() / nota_geral['media_geral'].count()
print('A média total de todos os alunos é', media_total.round(2))