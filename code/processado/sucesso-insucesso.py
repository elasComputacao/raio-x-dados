# situacoes = aprovado, reprovado, reprovado por falta

# insucesso = (reprovado + reprovado por falta) / situacoes

# sucesso = aprovado / situacoes


import pandas as pd
from functools import reduce


def pre_processamento():

    alunos = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/alunos_raiox.csv")
    alunos = alunos[(alunos.periodo_ingresso >= 2006.1) & (alunos.periodo_ingresso <= 2019.2)]
    
    historico = pd.read_csv("https://raw.githubusercontent.com/elasComputacao/raio-x-dados/main/data/dados-brutos/historico_alunos_raiox.csv")
    historico = historico[(historico.periodo_ingresso >= 2006.1) & (historico.periodo_ingresso <= 2019.2)]
        
    # Merge de alunos e historico
    geral = pd.merge(alunos, historico, how='left')
    
    # Mudando as colunas object para minúsculo
    colunas = geral.columns[geral.dtypes.eq('object')]
    geral[colunas] = geral[colunas].apply(lambda x: x.astype(str).str.upper())
    
    # Removendo as dispensas e as disciplinas em curso
    geral = geral[~geral.tipo_matricula.isin(['DISPENSA','EM CURSO'])] 

    # Considerando apenas as situações Aprovado, Reprovado e Reprovado Por Falta
    # descartando as opções Trancado e Cancelado
    geral = geral[geral.situacao.isin(['APROVADO', 'REPROVADO', 'REPROVADO POR FALTA'])]
       
    # Seleção das colunas necessárias
    geral = geral[['id', 'periodo_ingresso', 'nome_disciplina', 'periodo_matricula', 'situacao', \
                   'periodo_evasao', 'forma_evasao', 'periodo_relativo', 'evadiu_periodo', 'tipo_matricula', \
                   'forma_saida','sexo']]
    
    # Separando apenas as disciplinas com tipo de matricula Normal
    geral = geral[geral.tipo_matricula == 'NORMAL']

    return geral




def get_df_taxas(geral):

    # Criando um dataframe para as taxas
    df_taxas = pd.DataFrame(geral.groupby(['situacao', 'nome_disciplina'])['id'].count())\
                                 .reset_index().rename(columns={'id':'quantidade'})
        
    # Criando tabelas temporárias para cada situação
    # Aprovados
    temp_apv = pd.DataFrame(df_taxas[df_taxas.situacao == 'APROVADO'].groupby('nome_disciplina')['quantidade'].sum())\
                                    .reset_index().rename(columns={'quantidade':'aprovado'})
    # Reprovados
    temp_rep = pd.DataFrame(df_taxas[df_taxas.situacao == 'REPROVADO'].groupby('nome_disciplina')['quantidade'].sum())\
                                    .reset_index().rename(columns={'quantidade':'reprovado'})
    # Reprovados Por Falta
    temp_rep_falta = pd.DataFrame(df_taxas[df_taxas.situacao == 'REPROVADO POR FALTA']\
                                        .groupby('nome_disciplina')['quantidade'].sum())\
                                        .reset_index().rename(columns={'quantidade':'reprovado_falta'})
    
    # Merge Dataframes
    df_taxas = reduce(lambda left,right: pd.merge(left,right, on='nome_disciplina', how='outer'), \
                              [temp_apv, temp_rep, temp_rep_falta]).fillna(0)
        
    df_taxas['soma_situacoes'] = df_taxas.loc[:,'aprovado':'reprovado_falta'].sum(axis=1)
    df_taxas['sucesso'] = round(df_taxas['aprovado']/ df_taxas['soma_situacoes'],4)
    df_taxas['insucesso'] = round((df_taxas.loc[:,'reprovado':'reprovado_falta'].sum(axis=1))/ df_taxas['soma_situacoes'],4)

    return df_taxas

# utilizando as funcoes do script
geral = pre_processamento()
df_taxas = get_df_taxas(geral)
# df_taxas.to_csv('taxas.csv')