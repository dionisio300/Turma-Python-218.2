# Importando bibliotecas básicas
import pandas as pd
import numpy as np

# Leitura do dataset
df = pd.read_csv("C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 2\\Aula04 - Atividade de Classificação\\Clientes_telecom.csv")

# Visualizar as primeiras linhas
print(df.head())

# Tamanho do dataset
print("Número de linhas e colunas:", df.shape)

# Informações gerais das colunas
df.info()
# Estatísticas das colunas numéricas
df.describe()


# Contar valores únicos de cada coluna
for col in df.columns:
    print(col, ":", df[col].nunique())

# Converter TotalCharges para numérico e detectar problemas
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Verificar valores faltantes
print(df.isnull().sum())

df["TotalCharges"].fillna(0, inplace=True)

print(df["Churn"].value_counts(normalize=True))

import matplotlib.pyplot as plt

plt.figure(figsize=(5,4))
df["Churn"].value_counts().plot(kind="bar", color=["skyblue","salmon"])
plt.title("Distribuição de Clientes - Churn (Cancelamento)")
plt.xlabel("Churn")
plt.ylabel("Número de Clientes")
plt.show()

# Mapa de calor para correlações
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular a correlação apenas das colunas numéricas
corr = df[["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]].corr()

# Mapa de calor
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Calor - Correlação entre Variáveis Numéricas")
plt.show()

# separar features e target
X_telecom = df.drop("Churn", axis=1)
y_telecom = df["Churn"]

# fazer a codificação das variáveis categóricas  com o label encoder
from sklearn.preprocessing import LabelEncoder
le_gender = LabelEncoder()
le_partner = LabelEncoder()
le_dependents = LabelEncoder()
le_phone_service = LabelEncoder()
le_multiple_lines = LabelEncoder()
le_internet_service = LabelEncoder()
le_online_security = LabelEncoder()
le_online_backup = LabelEncoder()
le_device_protection = LabelEncoder()
le_tech_support = LabelEncoder()
le_streaming_tv = LabelEncoder()
le_streaming_movies = LabelEncoder()
le_contract = LabelEncoder()
le_payment_method = LabelEncoder()

X_telecom["gender"] = le_gender.fit_transform(X_telecom["gender"])
X_telecom["Partner"] = le_partner.fit_transform(X_telecom["Partner"])
X_telecom["Dependents"] = le_dependents.fit_transform(X_telecom["Dependents"])
X_telecom["PhoneService"] = le_phone_service.fit_transform(X_telecom["PhoneService"])
X_telecom["MultipleLines"] = le_multiple_lines.fit_transform(X_telecom["MultipleLines"])
X_telecom["InternetService"] = le_internet_service.fit_transform(X_telecom["InternetService"])
X_telecom["OnlineSecurity"] = le_online_security.fit_transform(X_telecom["OnlineSecurity"])
X_telecom["OnlineBackup"] = le_online_backup.fit_transform(X_telecom["OnlineBackup"])
X_telecom["DeviceProtection"] = le_device_protection.fit_transform(X_telecom["DeviceProtection"])
X_telecom["TechSupport"] = le_tech_support.fit_transform(X_telecom["TechSupport"])
X_telecom["StreamingTV"] = le_streaming_tv.fit_transform(X_telecom["StreamingTV"])
X_telecom["StreamingMovies"] = le_streaming_movies.fit_transform(X_telecom["StreamingMovies"])
X_telecom["Contract"] = le_contract.fit_transform(X_telecom["Contract"])
X_telecom["PaymentMethod"] = le_payment_method.fit_transform(X_telecom["PaymentMethod"])
print(X_telecom.head())

from sklearn.model_selection import train_test_split

X_telecom_treino, X_telecom_teste, y_telecom_treino, y_telecom_teste = train_test_split(
    X_telecom, y_telecom, test_size=0.25, random_state=0, stratify=y_telecom
)

print("Tamanho treino:", X_telecom_treino.shape)
print("Tamanho teste:", X_telecom_teste.shape)

from sklearn.preprocessing import MinMaxScaler

normalizador = MinMaxScaler()
X_telecom_treino_norm = normalizador.fit_transform(X_telecom_treino)
X_telecom_teste_norm = normalizador.transform(X_telecom_teste)


