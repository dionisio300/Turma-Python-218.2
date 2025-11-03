import pandas as pd
import numpy as np

# Carregar a base de dados
census = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula2/census.csv")

# Separar previsores e classe
x_census = census.iloc[:,0:14].values
y_census = census.iloc[:,14].values

# Tratar dados categóricos
from sklearn.preprocessing import LabelEncoder

labelEncoder_workclass = LabelEncoder()  
labelEncoder_education = LabelEncoder()
labelEncoder_marital_status = LabelEncoder()
labelEncoder_occupation = LabelEncoder()
labelEncoder_relationship = LabelEncoder()
labelEncoder_race = LabelEncoder()
labelEncoder_sex = LabelEncoder()
labelEncoder_native_country = LabelEncoder()

x_census[:,1] = labelEncoder_workclass.fit_transform(x_census[:,1])
x_census[:,3] = labelEncoder_education.fit_transform(x_census[:,3])
x_census[:,5] = labelEncoder_marital_status.fit_transform(x_census[:,5])
x_census[:,6] = labelEncoder_occupation.fit_transform(x_census[:,6])
x_census[:,7] = labelEncoder_relationship.fit_transform(x_census[:,7])
x_census[:,8] = labelEncoder_race.fit_transform(x_census[:,8])
x_census[:,9] = labelEncoder_sex.fit_transform(x_census[:,9])
x_census[:,13] = labelEncoder_native_country.fit_transform(x_census[:,13])

# Dividir base de dados em treino e teste
from sklearn.model_selection import train_test_split

x_census_treino, x_census_teste, y_census_treino, y_census_teste = train_test_split(x_census, y_census, test_size=0.3, random_state=0)

# Aplicar o algoritmo Naive Bayes

from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
classificador.fit(x_census_treino, y_census_treino)

# Fazer previsões
previsoes = classificador.predict(x_census_teste)

# Avaliar o modelo
from sklearn.metrics import accuracy_score, confusion_matrix

precisao = accuracy_score(y_census_teste, previsoes)
print(f"A precisão do modelo é: {precisao * 100}%")

# Arvore de decisão
from sklearn.tree import DecisionTreeClassifier

classificador_arvore = DecisionTreeClassifier(criterion='entropy')

classificador_arvore.fit(x_census_treino, y_census_treino)

previsoes_arvore = classificador_arvore.predict(x_census_teste)

precisao_arvore = accuracy_score(y_census_teste, previsoes_arvore)

print(f"A precisão da árvore de decisão é: {precisao_arvore * 100}%")

# Mostrar a árvore de decisão
from sklearn import tree
import matplotlib.pyplot as plt

# plt.figure(figsize=(12,8))
# tree.plot_tree(classificador_arvore, filled=True)
# plt.show()

from sklearn.preprocessing import MinMaxScaler
normalizacao = MinMaxScaler()
x_census_treino_normalizado = normalizacao.fit_transform(x_census_treino)
x_census_teste_normalizado = normalizacao.transform(x_census_teste)

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(100,50,20), early_stopping=False)
mlp.fit(x_census_treino_normalizado,y_census_treino)
previsoes_mlp = mlp.predict(x_census_teste_normalizado)

precisao_mlp = accuracy_score(y_census_teste, previsoes_mlp)
print(f"MLP: {precisao_mlp * 100}%")
matriz_confusao = confusion_matrix(y_census_teste, previsoes_mlp,)
print(matriz_confusao)