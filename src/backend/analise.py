import pandas as pd
from IPython.display import display, clear_output

def realizar_analise(dados, df_municipios, df_ncm_sh, ano, atividade, tipo, mes_num, municipio):
    print(f"Parâmetros Selecionados:")
    print(f"- Ano: {ano}")
    print(f"- Atividade: {atividade}")
    print(f"- Filtro: {tipo}")
    print(f"- Mês: {'Todos' if mes_num is None else mes_num}")
    print(f"- Município: {municipio}\n")

    df_base = dados[ano]['IMP'] if atividade == 'Importação' else dados[ano]['EXP']
    print(df_base.head())
    df = df_base.copy()

    df = df[df['KG_LIQUIDO'] > 0]
    df['VALOR_AGREGADO'] = df['VL_FOB'] / df['KG_LIQUIDO']
    df = df.merge(df_municipios, on='CO_MUN', how='left')
    df = df.merge(df_ncm_sh, on='SH4', how='left')

    if mes_num is not None:
        df = df[df['CO_MES'] == mes_num]
    df = df[df['NO_MUN'] == municipio]

    match tipo:
        case 'Valor Agregado':
            resultado = df.groupby(['NO_MUN', 'SG_UF_MUN', 'NO_SH4_POR'])['VALOR_AGREGADO'].mean().reset_index()
            resultado = resultado.sort_values(by='VALOR_AGREGADO', ascending=False).head(5)
        case 'SH4':
            resultado = df['NO_SH4_POR'].value_counts().head(5).reset_index()
            resultado.columns = ['NO_SH4_POR', 'Contagem']
        case 'KG_LIQUIDO':
            resultado = df.groupby('NO_SH4_POR')['KG_LIQUIDO'].sum().sort_values(ascending=False).head(5).reset_index()
        case 'Valor FOB':
            resultado = df.groupby('NO_SH4_POR')['VL_FOB'].sum().sort_values(ascending=False).head(5).reset_index()
        case _:
            resultado = pd.DataFrame({'Mensagem': ['Tipo de análise não reconhecido']})

    #display(resultado)
    return resultado