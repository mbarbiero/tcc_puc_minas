##
#   Consolida os arquivos de dados municipais baixados da base CNIR
#   Seleciona apenas os campos necessários ao processo de aprendizagem e vinculação
##
import pandas as pd
import json
import os
import io

pasta = '..\\DADOS'
caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
arqs_json = [arq for arq in arquivos if arq.lower().endswith('.json')]

cnirs = pd.DataFrame()

for arq_json in arqs_json:
    print(arq_json)
    str_json  = io.open(arq_json, "r").read()
    dados_json = json.loads(str_json)
    sel_dados_json = pd.json_normalize(dados_json)[['codigoCnir', 'codigoIncra', 'nirfs', 'municipioSede.codigo', 'areaTotal', 'titularPrincipal.ni']]

    cnirs = cnirs.append(sel_dados_json, ignore_index=True)

    print(len(cnirs.index))

cnirs.to_csv(r'd:\\temp\\cnir\\cnirs.csv')