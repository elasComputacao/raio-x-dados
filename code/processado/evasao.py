import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

geral = df_alunos.query("periodo_ingresso >= 2000.1")
mulheres = geral.query("sexo == 'Feminino'")
print(mulheres['forma_evasao'].value_counts())