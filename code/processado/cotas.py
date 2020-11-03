import pandas as pd
df_alunos = pd.read_csv("../dados/alunos_raiox.csv")

mulheres = df_alunos.query("periodo_ingresso >= 2000.1").query("sexo == 'Feminino'").query("tipo_reserva_vagas != 1")
cotas = mulheres[['periodo_ingresso','forma_reserva_vagas']]
cotas['periodo_ingresso'].astype(str)
#cotas.head()
#cotas.to_csv('cotas.csv') 
#files.download('cotas.csv')