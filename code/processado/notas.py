import pandas as pd
df_alunos = pd.read_csv("../dados/alunos_raiox.csv")

geral = df_alunos.query("periodo_ingresso >= 2000.1").query("apv_media_geral != 'NaN'")
mulheres = geral.query("sexo == 'Feminino'")
mulheres = mulheres.groupby(['periodo_ingresso'])['apv_media_geral'].mean().astype(int)

mulheres = mulheres.to_frame('media_mulheres').reset_index()

geral = geral.groupby(['periodo_ingresso'])['apv_media_geral'].mean()
geral = geral.to_frame('media_geral').reset_index()


nota_geral = geral.join(mulheres['media_mulheres'])
nota_geral['periodo_ingresso'].astype(str)
nota_geral = pd.wide_to_long(nota_geral, stubnames='media', i=['periodo_ingresso'], j='classe',
                    sep='_', suffix='\w+').reset_index()
nota_geral.head()
#nota_geral.to_csv('notas.csv') 
#files.download('notas.csv')