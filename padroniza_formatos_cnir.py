##
#   Padroniza o formato dos valores 
##
import numpy
import pandas as pd
import os

arquivo = '..\\DADOS\\cnirs.csv'

cnirs = pd.read_csv(arquivo)


print(cnirs)
cnirs.to_csv(r'd:\\temp\\cnir\\cnirs.csv')