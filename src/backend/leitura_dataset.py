from google.colab import drive
import pandas as pd

__path = '/content/drive/MyDrive/Colab Notebooks/API1S/base_dados_por_municipio'

def autenticacao_google():
    drive.mount('/content/drive')


def __leitura_arq_cod_nome(lista_nomes_arq): #[]'ncm', 'co_sh']
  lista_arq = []

  for arq in lista_nomes_arq:
    path = f'{__path}/{arq}.csv'
    df = pd.read_csv(path, delimiter=';', on_bad_lines='skip', encoding='latin-1')
    df.columns = df.columns.str.strip()

    if 'SG_UF' in df.columns:
      df = df[df['SG_UF'] == 'SP']

    lista_arq.append(df)

  return lista_arq


def __leitura_arq_mun(tipo, ano):
  path = f'{__path}/{tipo}_{ano}_MUN.csv'
  df_mun = pd.read_csv(path, delimiter=';', on_bad_lines='skip', encoding='latin-1', usecols='''CO_MES SH4 CO_PAIS SG_UF_MUN CO_MUN KG_LIQUIDO VL_FOB'''.split())
  df_mun.columns = df_mun.columns.str.strip()
  df_sp = df_mun[df_mun['SG_UF_MUN'] == 'SP']

  return df_sp


def __carregar_dados_mun():
  dados = {}

  for ano in range(2019, 2025):
    dados[ano] = {'EXP': __leitura_arq_mun('EXP', ano), 'IMP': __leitura_arq_mun('IMP', ano)}

  return dados


def pegar_dados():
  dados = __carregar_dados_mun()

  #carregamento dos arquivos de códigos e correspondências:
  nome_arq = ['UF_MUN', 'PAIS', 'NCM_SH']
  lista_arquivos = __leitura_arq_cod_nome(nome_arq)

  lista_arquivos[0].rename(columns={'CO_MUN_GEO': 'CO_MUN'}, inplace=True)
  lista_arquivos[2].rename(columns={'CO_SH4': 'SH4'}, inplace=True)

  df_municipios = lista_arquivos[0][['CO_MUN', 'NO_MUN']]
  df_ncm_sh = lista_arquivos[2][['SH4', 'NO_SH4_POR']]

  df_mun_nomes = sorted(df_municipios['NO_MUN'].unique().tolist())
  df_ncm_sh_nomes = sorted(df_ncm_sh['NO_SH4_POR'].unique().tolist())

  util_data = {
    "df_municipios": df_municipios,
    "df_ncm_sh": df_ncm_sh,
    "df_mun_nomes": df_mun_nomes,
    "df_ncm_sh_nomes": df_ncm_sh_nomes,
  }
  return dados, util_data
