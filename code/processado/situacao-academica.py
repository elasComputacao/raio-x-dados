import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

df_situacao_academica = pd.DataFrame(df_alunos.query("periodo_ingresso >= 2000.1")\
                                              .groupby(['forma_saida', 'sexo'])['id'].count())\
                                              .reset_index().rename(columns={'id':'quantidade'})
# df_situacao_academica.to_csv("situacao-academica.csv", index=False)