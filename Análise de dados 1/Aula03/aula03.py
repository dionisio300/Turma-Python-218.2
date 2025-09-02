'''
A tabela abaixo mostra os pesos (em kg) de 50 alunos de uma academia:

a) Construa uma tabela de frequência por intervalos de classe utilizando a regra de strugs para calcular as classes, considerando o menor valor 58 kg e o maior 118 kg.

b) A partir da tabela, indique:

O intervalo de classe com maior frequência absoluta.

A frequência relativa acumulada até a terceira classe.

c) Costrua a Tabela de frequência com um dicionário e depois transforme em um DataFrame
'''

import pandas as pd
import math

pesos = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 1\\Aula03\\dados_brutos_pesos.csv')

amplitude = pesos['Peso (kg)'].max() - pesos['Peso (kg)'].min()

print(f'Amplitude = {amplitude}')

n = len(pesos['Peso (kg)'])

print(f'N = {n}')

numero_classes = 1 + 3.3*math.log10(n)
numero_classes = round(numero_classes)

print(f'Número de Classes = {numero_classes}')

Amplitude_classe = amplitude/numero_classes
Amplitude_classe = round(Amplitude_classe)

print(f'Amplitude Classe = {Amplitude_classe}')

###############################################################
#### Criar um dicionário com as frequências de cada classe ####
###############################################################

print(pesos.describe())

# Média
print(f'Média = {pesos['Peso (kg)'].mean()}')

# Mediana
print(f'Mediana = {pesos['Peso (kg)'].median()}')

# Moda
print(f'Moda = \n{pesos['Peso (kg)'].mode()}')

# Variância
print(f'Variância = {pesos['Peso (kg)'].var()}')

# Desvio padrão
print(f'Desvio Padrão = {pesos['Peso (kg)'].std()}')

# Quartis
print(f'Q1 = {pesos["Peso (kg)"].quantile(0.25)}')
print(f'Q2 = {pesos["Peso (kg)"].quantile(0.50)}')
print(f'Q3 = {pesos["Peso (kg)"].quantile(0.75)}')
print(f'Q4 = {pesos["Peso (kg)"].quantile(1)}')

# IQR
q1 = pesos["Peso (kg)"].quantile(0.25)
q3 = pesos["Peso (kg)"].quantile(0.75)
print(f'IQR = {q3 - q1}')

# Outliers
iqr = q3 - q1
limites = [q1-1.5*iqr,q3+1.5*iqr]
print(f'Limites = {limites}')

# Normalização e Padronização (Depois)

# Correlação
planos = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 1\\Aula03\\plano_saude.csv')

print(f'Correlação = \n {planos.corr()}')
