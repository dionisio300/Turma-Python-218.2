import pandas as pd
import numpy as np

dadosCredito = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 1\\Aula04\\credit_data.csv')

print(dadosCredito.head(10))

'''
1) Calcular a média da idade, renda e dívida
2) Calcular a mediana da idade, renda e dívida
3) Calcular e interpretar o desvio padrão da idade, renda e dívida
4) Calcular a amplitude das colunas
5) Calcular e interpretar o coeficiente de variação da idade, renda e dívida
6) Faça o intervalo de identificação dos outliers da idade, renda e dívida
7) Faça uma lista com dados da divida normalizados
'''

q1renda, q3renda = dadosCredito['income'].quantile([0.25,0.75])
iqr = q3renda - q1renda
limSup = q3renda + (1.5*iqr)
limInf = q1renda - (1.5*iqr)

limitesRenda = [limInf,limSup]
print(limitesRenda)


q1divida, q3divida = dadosCredito['loan'].quantile([0.25,0.75])
iqr = q3divida - q1divida
limSup = q3divida + (1.5*iqr)
limInf = q1divida - (1.5*iqr)

limitesDivida = [limInf,limSup]
print(limitesDivida)

dividaMax = dadosCredito['loan'].max()
dividaMin = dadosCredito['loan'].min()

print(dividaMax,dividaMin)

dadosCredito['DividaNormalizada'] = (dadosCredito['loan'] - dividaMin)/(dividaMax - dividaMin)

print(dadosCredito)

# Filtragem de dados

# condições simples
dados2 = dadosCredito['loan'] > 2000
print(dados2.sum())

dados3 = dadosCredito[dadosCredito['loan'] > 2000]
print(dados3)

dados4 = dadosCredito[dadosCredito['age'] < 0]
print(dados4)

print(dadosCredito[dadosCredito['age'] < 0])

print(dadosCredito.head(17))

print(dadosCredito[dadosCredito['clientid'] == 16])

# loc

print(dadosCredito.loc[dadosCredito['age'] < 0])

dadosCredito.loc[dadosCredito['age'] < 0,['age','loan']] = dadosCredito['age'].mean()

print(dadosCredito.loc[(dadosCredito['age'] < 30) & (dadosCredito['loan'] < 2000)])
# print(dadosCredito.head(16))

# iloc

# dados5 = dadosCredito.iloc[:,4]
# print(dados5)
'''
Faça um filtro que:
1) Mostre apenas clientid e age dos clintes que pagaram.
2) Filtrar clientes com renda entre 40000 e 60000
3) Usar o iloc para pegar a última linha e todas as colunas
4) mostrar os geristros com idade > 50 ou dívida maior que 8000
'''
# 1
print(dadosCredito.loc[dadosCredito['default'] == 1, ['clientid','age']])

# 2
print(dadosCredito.loc[(dadosCredito['income'] >= 40000) & (dadosCredito['income'] <= 60000)])

# 3
print(dadosCredito.iloc[-1,[0,2,4]])

# 4
print(dadosCredito.loc[(dadosCredito['age'] > 50) | (dadosCredito['loan'] > 8000)])


