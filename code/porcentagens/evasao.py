import pandas as pd
df_alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")

geral = df_alunos.query("periodo_ingresso >= 2000.1").query("forma_evasao != 'GRADUADO'").query("forma_evasao != 'REGULAR'")
mulheres = geral.query("sexo == 'Feminino'")
cont_geral = mulheres['forma_evasao'].count()
abandono = mulheres['forma_evasao'][mulheres['forma_evasao'] == 'CANCELAMENTO POR ABANDONO'].count()
porc_abandono = abandono * 100 / cont_geral
print('A porcentagem de evasão por abandono:', porc_abandono.round(2))

reingresso = mulheres['forma_evasao'][mulheres['forma_evasao'] == 'CANCELADO NOVO INGRESSO MESMO CURSO'].count()
porc_reingresso = reingresso * 100 / cont_geral
print('A porcentagem de evasão por reingresso:', porc_reingresso.round(2))

faltas = mulheres['forma_evasao'][mulheres['forma_evasao'] == 'CANCELADO REPROVOU TODAS POR FALTAS'].count()
porc_faltas = faltas * 100 / cont_geral
print('A porcentagem de evasão por reprovação por faltas:', porc_faltas.round(2))

reprov3 = mulheres['forma_evasao'][mulheres['forma_evasao'] == 'CANCELADO 3 REPROV MESMA DISCIPLINA'].count()
porc_reprov3 = reprov3 * 100 / cont_geral
print('A porcentagem de evasão por 3 reprovações na mesma disciplina:', porc_reprov3.round(2))

abandono_faltas = (abandono + faltas)* 100 / cont_geral
print('A porcentagem de abandono e reprovação por faltas:', abandono_faltas.round(2))