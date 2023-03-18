import funcoes as fc
import pandas as pd
import datetime as dt
#Pegando o horario do pc    
data = dt.datetime.now()
data_form = data.strftime("%Y-%m-%d")   
#Pegando e organizando as tabelas
vendas = pd.read_excel("C:\\Users\\dudud\\OneDrive\\Documentos\\Faculdade\\Estudos Gerais\\Python\\Sistema_nfe\\Vendas.xlsx")
vendas_form = vendas.loc[vendas['Data'] == '12-03-2023']

print(vendas_form)