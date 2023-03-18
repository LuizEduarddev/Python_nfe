import funcoes as fc
import pandas as pd
import datetime as dt
#Pegando o horario do pc    
quantidade = 10
quantidade_prod = 0
data = dt.datetime.now()
data_form = data.strftime("%d/%m/%Y %H:%M")   
#Pegando e organizando as tabelas
vendas = pd.read_excel("C:\\Users\\dudud\\OneDrive\\Documentos\\Faculdade\\Estudos Gerais\\Python\\Sistema_nfe\\Vendas.xlsx")
vendas_formatado = vendas.loc[vendas['Data'] == '2019-12-01', ['Código Venda','Produto', 'Quantidade']]
vendas_divisao = vendas_formatado.loc[vendas['Produto'] == 'Casaco']
qntd_colunas = vendas_divisao.shape
qntd_colunas = qntd_colunas[int(0)]

while vendas_divisao != Cells


