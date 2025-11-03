import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

credit_data = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula1/credit_data.csv")

x_credit_data = credit_data.iloc[:,1:4].values
y_credit_data = credit_data.iloc[:,4].values

# print(x_credit_data,y_credit_data)

# Separar dados de treino e teste

from sklearn.model_selection import train_test_split

x_credit_data_treino, x_credit_data_teste, y_credit_data_treino, y_credit_data_teste = train_test_split(x_credit_data, y_credit_data, test_size=0.20, random_state=0)

###############################################################################
########################### Naive Bayes #######################################
###############################################################################

modelo_naive = GaussianNB()
modelo_naive.fit(x_credit_data_treino, y_credit_data_treino)

previsoes = modelo_naive.predict(x_credit_data_teste)

from sklearn.metrics import accuracy_score

precisao = accuracy_score(y_credit_data_teste, previsoes)
print(f'Naive Bayes: {precisao*100}%')

# Matriz de confusão
from sklearn.metrics import confusion_matrix

matriz_confusao = confusion_matrix(y_credit_data_teste, previsoes)
print(matriz_confusao)


###############################################################################
########################### Árvore de Decisão ################################
###############################################################################


from sklearn.tree import DecisionTreeClassifier

classificador_arvore = DecisionTreeClassifier(criterion='entropy')

classificador_arvore.fit(x_credit_data_treino, y_credit_data_treino)

previsoes_arvore = classificador_arvore.predict(x_credit_data_teste)

precisao_arvore = accuracy_score(y_credit_data_teste, previsoes_arvore)

print(f"Árvore de Decisão: {precisao_arvore * 100}%")
matriz_confusao = confusion_matrix(y_credit_data_teste, previsoes_arvore)
print(matriz_confusao)

#########################################################################
################################### KNN #################################
##########################################################################

from sklearn.preprocessing import MinMaxScaler
normalizacao = MinMaxScaler()
x_credit_data_treino_normalizado = normalizacao.fit_transform(x_credit_data_treino)
x_credit_data_teste_normalizado = normalizacao.fit_transform(x_credit_data_teste)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3,metric='euclidean')
knn.fit(x_credit_data_treino_normalizado,y_credit_data_treino)

previsoes_knn = knn.predict(x_credit_data_teste_normalizado)
precisao_knn = accuracy_score(y_credit_data_teste, previsoes_knn)

print(f"KNN: {precisao_knn * 100}%")
matriz_confusao = confusion_matrix(y_credit_data_teste, previsoes_knn)
print(matriz_confusao)


#########################################################################
################################### MLP #################################
##########################################################################

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(32,32), verbose=True, early_stopping=False)
mlp.fit(x_credit_data_treino_normalizado,y_credit_data_treino)
previsoes_mlp = mlp.predict(x_credit_data_teste_normalizado)

precisao_mlp = accuracy_score(y_credit_data_teste, previsoes_mlp)
print(f"MLP: {precisao_mlp * 100}%")
matriz_confusao = confusion_matrix(y_credit_data_teste, previsoes_mlp,)
print(matriz_confusao)




# Mostrar a árvore de decisão
from sklearn import tree
import matplotlib.pyplot as plt

# plt.figure(figsize=(12,8))
# tree.plot_tree(classificador_arvore, filled=True)
# plt.show()

# classication report
# from sklearn.metrics import classification_report
# y_credit_data_predito = modelo_naive.predict(x_credit_data)
# print(classification_report(y_credit_data, y_credit_data_predito))

# # classication report arvore
# y_credit_data_predito_arvore = classificador_arvore.predict(x_credit_data)
# print(classification_report(y_credit_data, y_credit_data_predito_arvore))