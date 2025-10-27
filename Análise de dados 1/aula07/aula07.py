import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

credit = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 1\\aula07\\credit_data.csv')

census = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 1\\aula07\\census.csv')

titanic = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 1\\aula07\\Titanic-Dataset.csv')


# Forma de identificar os dados faltantes
print(credit.isnull().sum())

print(credit.dtypes)

print(credit.info())

credit['age'] = pd.to_numeric(credit["age"], errors="coerce")

print(credit[credit['age'].isnull()])

print(credit.info())

print(census['sex'].value_counts())

census["sex"] = census["sex"].str.lower().str.strip()
census['sex'] = census["sex"].replace({
    'm':'male',
    'f':'female'
})

print(census['sex'].value_counts())

print(census['education'].value_counts(normalize=True)*100)

print(census.describe())
print(credit.describe())


pd.set_option("display.max_columns", None)

print(census)

print(census.describe(include="object"))

credit['age'] = credit["age"].fillna(credit["age"].mean())

print(credit['age'].isnull().sum())

census["occupation"] = census["occupation"].fillna(" Desconhecido")
census["occupation"] = census["occupation"].str.strip()
census["occupation"] = census["occupation"].replace({'?':'Desconhecido'})

print(census['occupation'].value_counts())

# Elimina linhas com qualquer valor nulo
census.dropna(inplace=True)

# Elimina as linhas quetem uma coluna específica com valor nulo
# census.dropna(subset=['final-weight'],inplace=True)

# Elimina colunas inteiras se tiverem nulos
# census.dropna(axis=1, inplace=True)

print(census)

print(census.isnull().sum())

print(titanic.isnull().sum())

# Deletar apenas uma coluna
titanic.drop(columns=['Cabin'],inplace=True)

titanic['Age'] = titanic["Age"].fillna(titanic["Age"].mean())
titanic.dropna(inplace=True)

print(titanic.isnull().sum())

print(f'dados duplicados Titanic = {titanic.duplicated().sum()}')
print(f'dados duplicados Census = {census.duplicated().sum()}')
print(f'dados duplicados Credit = {credit.duplicated().sum()}')

# Remove duplicatas
census.drop_duplicates(inplace=True)
print(f'dados duplicados Census = {census.duplicated().sum()}')

# Identificando dados inconsistentes
print(credit.describe())
# Substitui valores negativos
print(credit.loc[(credit["age"] < 0) | (credit["age"] > 130)])

credit.loc[(credit["age"] < 0) | (credit["age"] > 100), "age"] = credit["age"].mean()#identificar os clientes de indice 15, 21, 26

print(credit.loc[(credit['clientid'] == 16) | (credit['clientid'] == 22) | (credit['clientid'] == 27)])


# Itendificar as idades outliers
Q1 = titanic['Fare'].quantile(0.25)
Q3 = titanic['Fare'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f'Limite inferior: {limite_inferior}')
print(f'Limite superior: {limite_superior}')

print(titanic[['Fare','Pclass']][(titanic['Fare'] < limite_inferior) | (titanic['Fare'] > limite_superior)])

# plt.figure(figsize=(8, 6))
# sns.boxplot(data=titanic,
#             x="Pclass",           # Variável categórica no eixo X
#             y="Fare", # Variável numérica no eixo Y
#             palette="Set2",    # Paleta de cores
#             showmeans=True)    # Mostra a média

# plt.title("Distribuição de Tarifas por Classe", fontsize=14)
# plt.xlabel("Classe", fontsize=12)
# plt.ylabel("Tarifa", fontsize=12)
# plt.show()

# # Contagem de sobreviventes com grafico de barras
# plt.figure(figsize=(8, 6))
# sns.countplot(data=titanic, x='Survived', palette='Set2')
# plt.title("Contagem de Sobreviventes", fontsize=14)
# plt.xlabel("Sobrevivência", fontsize=12)
# plt.ylabel("Contagem", fontsize=12)
# plt.show()

# # Contagem de sobreviventes por classe com grafico de barras
# plt.figure(figsize=(8, 6))
# sns.countplot(data=titanic, x='Pclass', hue='Survived', palette='Set2')
# plt.title("Contagem de Sobreviventes por Classe", fontsize=14)
# plt.xlabel("Classe", fontsize=12)
# plt.ylabel("Contagem", fontsize=12)
# plt.legend(title="Sobrevivência", loc="upper right", labels=["Não Sobreviveu", "Sobreviveu"])
# plt.show()

