import pandas as pd
import datetime as dt

def hora_pc():
    data = dt.datetime.now()
    data_form = data.strftime("%d/%m/%Y %H:%M")
    return data_form

def cria_tabela (data):
    vendas = pd.read_excel("C:\\Users\\dudud\\OneDrive\\Documentos\\Faculdade\\Estudos Gerais\\Python\\Sistema_nfe\\Vendas.xlsx")
    separa_prod(vendas, data)
    return vendas
    

def separa_prod(vendas, data):
    vendas.loc
    