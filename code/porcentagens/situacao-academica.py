import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

geral = df_alunos.query("periodo_ingresso >= 2000.1")
homens = geral.query("sexo == 'Masculino'").query("forma_saida != 'Outros'")
print(homens['forma_saida'].value_counts(normalize=True).round(4))

mulheres = geral.query("sexo == 'Feminino'")
print(mulheres['forma_saida'].value_counts(normalize=True).round(4))

mulheres = df_alunos.query("periodo_ingresso >= 2000.1").query("sexo == 'Feminino'")
cont_graduadas = mulheres['forma_saida'][mulheres['forma_saida'] == 'Graduado'].count()
print('Quantidade de graduadas:',cont_graduadas)