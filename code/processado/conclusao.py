import pandas as pd
df_alunos = pd.read_csv("../dados/alunos_raiox.csv")

geral = df_alunos.query("periodo_ingresso >= 2000.1")
print(geral['forma_saida'].value_counts(normalize=True))
# outros:
# 10) "CONCLUIDO - NAO COLOU GRAU"
# 13) "CUMPRIMENTO CONVENIO"
# 51) "VALIDACAO DECLARACAO PENDENTE"

geral = df_alunos.query("periodo_ingresso >= 2000.1")
mulheres = geral.query("sexo == 'Feminino'")
print(mulheres['forma_saida'].value_counts(normalize=True))