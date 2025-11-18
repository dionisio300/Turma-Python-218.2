import pandas as pd
import numpy as np

# Carregar o conjunto de dados
housePrices = pd.read_csv(r"C:\Users\dioni\OneDrive\Área de Trabalho\Youth Data 218.02\Curso Data\218\Análise de dados 2\Aula06 - Regressão Linear e Polinomial\house_prices.csv")

x_housePrices = housePrices.iloc[:,5].values
y_housePrices = housePrices.iloc[:,2].values

print(x_housePrices,y_housePrices)
correlacao = np.corrcoef(x_housePrices, y_housePrices)
print("Coeficiente de correlação:\n", correlacao)

x_housePrices = x_housePrices.reshape(-1, 1)
y_housePrices = y_housePrices.reshape(-1, 1)

# Regressão Linear Simples

# separar dados de treino e teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_housePrices, y_housePrices, test_size=0.25, random_state=0)

# Regressão Linear
from sklearn.linear_model import LinearRegression
regressaoLinear = LinearRegression()
regressaoLinear.fit(X_train, y_train)

# Fazer previsões
previsao_Linear = regressaoLinear.predict(X_test)

# R² Regressão Linear
r2 = regressaoLinear.score(X_test, y_test)
print(f"Escore R² Regressão Linear: {r2}")

# Regressão Polinomial
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=4)
x_housePrices_poly = poly.fit_transform(X_train)

regressaoPolinomial = LinearRegression()
regressaoPolinomial.fit(x_housePrices_poly, y_train)

x_housePrices_poly_test = poly.transform(X_test)

previsao_Polinomial = regressaoPolinomial.predict(x_housePrices_poly_test)

# R² Regressão Polinomial
r2_poly = regressaoPolinomial.score(x_housePrices_poly_test, y_test)
print(f"Escore R² Regressão Polinomial: {r2_poly}")


# Árvore de Regressão
from sklearn.tree import DecisionTreeRegressor
arvoreRegr = DecisionTreeRegressor(random_state=0)
arvoreRegr.fit(X_train, y_train)
previsao_Arvore = arvoreRegr.predict(X_test)
r2_arvore = arvoreRegr.score(X_test, y_test)
print(f"Escore R² Árvore de Regressão: {r2_arvore}")


y_train = y_train.reshape(-1)

# Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor
randomForestRegr = RandomForestRegressor(random_state=0, n_estimators=100)
randomForestRegr.fit(X_train, y_train)
previsao_RandomForest = randomForestRegr.predict(X_test)
r2_randomForest = randomForestRegr.score(X_test, y_test)
print(f"Escore R² Random Forest Regressor: {r2_randomForest}")

# MLP Regressor
from sklearn.neural_network import MLPRegressor