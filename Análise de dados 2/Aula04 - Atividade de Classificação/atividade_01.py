# Análise de dados - Atividade de Classificação Clientes Telecom

# pipiline de análise de dados para o dataset de clientes de telecomunicações
# carregar os dados, explorar, tratar valores faltantes, visualizar distribuições e correlações, preparar dados para modelagem

import pandas as pd
import numpy as np

clientes_telecom = pd.read_csv("C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 2\\Aula04 - Atividade de Classificação\\Clientes_telecom.csv")

print(clientes_telecom.describe())

# describe para colunas categóricas sem diminuir a quantidade de colunas exibidas
print(clientes_telecom.describe(include="object"))

print(clientes_telecom.isnull().sum())

# verificar se há valores duplicados
print(clientes_telecom.duplicated().sum())



# Mostrar histograma da classe
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.countplot(x='Churn', data=clientes_telecom)
# plt.title('Distribuição da Classe Churn')
# plt.show()

# Mostrar o balanceamento da classe
print(clientes_telecom['Churn'].value_counts(normalize=True)*100)

#balanceamento da classe com oversampling
# instalar o pacote imbalanced-learn se ainda não estiver instalado
# pip install imbalanced-learn

from imblearn.over_sampling import SMOTE
x = clientes_telecom.iloc[:,1:19]
y = clientes_telecom.iloc[:,20]

# Separar os previsores da classe ajustar o balanceamento

x_clientes_telecom = clientes_telecom.iloc[:,1:19].values
y_clientes_telecom = clientes_telecom.iloc[:,20].values

# Label Encoding para variáveis categóricas
from sklearn.preprocessing import LabelEncoder

gender_encoder1 = LabelEncoder()
partner_encoder3 = LabelEncoder()
dependents_encoder4 = LabelEncoder()
phone_service_encoder6 = LabelEncoder()
multiple_lines_encoder7 = LabelEncoder()
internet_service_encoder8 = LabelEncoder()
online_security_encoder9 = LabelEncoder()
online_backup_encoder10 = LabelEncoder()
device_protection_encoder11 = LabelEncoder()
tech_support_encoder12 = LabelEncoder()
streaming_tv_encoder13 = LabelEncoder()
streaming_movies_encoder14 = LabelEncoder()
contract_encoder15 = LabelEncoder()
paperless_billing_encoder16 = LabelEncoder()
payment_method_encoder17 = LabelEncoder()

x_clientes_telecom[:,0] = gender_encoder1.fit_transform(x_clientes_telecom[:,0])
x_clientes_telecom[:,2] = partner_encoder3.fit_transform(x_clientes_telecom[:,2])
x_clientes_telecom[:,3] = dependents_encoder4.fit_transform(x_clientes_telecom[:,3])
x_clientes_telecom[:,5] = phone_service_encoder6.fit_transform(x_clientes_telecom[:,5])
x_clientes_telecom[:,6] = multiple_lines_encoder7.fit_transform(x_clientes_telecom[:,6])
x_clientes_telecom[:,7] = internet_service_encoder8.fit_transform(x_clientes_telecom[:,7])
x_clientes_telecom[:,8] = online_security_encoder9.fit_transform(x_clientes_telecom[:,8])
x_clientes_telecom[:,9] = online_backup_encoder10.fit_transform(x_clientes_telecom[:,9])
x_clientes_telecom[:,10] = device_protection_encoder11.fit_transform(x_clientes_telecom[:,10])
x_clientes_telecom[:,11] = tech_support_encoder12.fit_transform(x_clientes_telecom[:,11])
x_clientes_telecom[:,12] = streaming_tv_encoder13.fit_transform(x_clientes_telecom[:,12])
x_clientes_telecom[:,13] = streaming_movies_encoder14.fit_transform(x_clientes_telecom[:,13])
x_clientes_telecom[:,14] = contract_encoder15.fit_transform(x_clientes_telecom[:,14])
x_clientes_telecom[:,15] = paperless_billing_encoder16.fit_transform(x_clientes_telecom[:,15])
x_clientes_telecom[:,16] = payment_method_encoder17.fit_transform(x_clientes_telecom[:,16])

# separar treino e teste
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_clientes_telecom, y_clientes_telecom, test_size=0.30, random_state=0)

# Aplicar naive bayes
from sklearn.naive_bayes import GaussianNB
naive_bayes = GaussianNB()
naive_bayes.fit(x_train, y_train)

y_pred = naive_bayes.predict(x_test)

print("Predições:", y_pred)
print("Valores reais:", y_test)

# Avaliar o modelo
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Relatório de Classificação:\n", classification_report(y_test, y_pred))
print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred,normalize='true')*100)

# Modelo random forest
from sklearn.ensemble import RandomForestClassifier
random_forest = RandomForestClassifier(n_estimators=100, random_state=0, max_depth=3)
random_forest.fit(x_train, y_train)
y_pred_rf = random_forest.predict(x_test)

print("Acurácia Random Forest:", accuracy_score(y_test, y_pred_rf))
print("Relatório de Classificação Random Forest:\n", classification_report(y_test, y_pred_rf))
print("Matriz de Confusão Random Forest:\n", confusion_matrix(y_test, y_pred_rf,normalize='true')*100)

# Normalização dos dados
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Modelo KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=41)
knn.fit(x_train_scaled, y_train)
y_pred_knn = knn.predict(x_test_scaled)

print("Acurácia KNN:", accuracy_score(y_test, y_pred_knn))
print("Relatório de Classificação KNN:\n", classification_report(y_test, y_pred_knn))
print("Matriz de Confusão KNN:\n", confusion_matrix(y_test, y_pred_knn,normalize='true')*100)

# Modelo MLP 
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(21,), early_stopping=False, tol=0.00001,solver='adam', max_iter=50000, random_state=0)

mlp.fit(x_train_scaled, y_train)
y_pred_mlp = mlp.predict(x_test_scaled)
print("Acurácia MLP:", accuracy_score(y_test, y_pred_mlp))
print("Relatório de Classificação MLP:\n", classification_report(y_test, y_pred_mlp))
print("Matriz de Confusão MLP:\n", confusion_matrix(y_test, y_pred_mlp,normalize='true')*100)

# Modelo SVM
from sklearn.svm import SVC
svm = SVC(kernel='rbf', random_state=0, C=3.0, gamma=0.05)
svm.fit(x_train_scaled, y_train)
y_pred_svm = svm.predict(x_test_scaled)


print("Acurácia SVM:", accuracy_score(y_test, y_pred_svm))
print("Relatório de Classificação SVM:\n", classification_report(y_test, y_pred_svm))
print("Matriz de Confusão SVM:\n", confusion_matrix(y_test, y_pred_svm,normalize='true')*100)
