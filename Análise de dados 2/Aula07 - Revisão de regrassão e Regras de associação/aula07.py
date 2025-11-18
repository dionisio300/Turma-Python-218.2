import plotly.express as px
# pip install plotly
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
# pip instal matplotlib 
import pandas as pd
import numpy as np

# Carregar o conjunto de dados
planoSaude = pd.read_csv(r"C:\Users\dioni\OneDrive\Área de Trabalho\Youth Data 218.02\Curso Data\218\Análise de dados 2\Aula06 - Regressão Linear e Polinomial\plano_saude.csv")

print(planoSaude)

x_planoSaude = planoSaude.iloc[:,0].values
y_planoSaude = planoSaude.iloc[:,1].values

correlacao = np.corrcoef(x_planoSaude, y_planoSaude)
print("Coeficiente de correlação:\n", correlacao)

x_planoSaude = x_planoSaude.reshape(-1, 1)
y_planoSaude = y_planoSaude.reshape(-1, 1)

# Regressão Linear Simples
# pip install scikit-learn
from sklearn.linear_model import LinearRegression
regressaoLinear = LinearRegression()
regressaoLinear.fit(x_planoSaude, y_planoSaude)

print("Coeficiente angular (b1): ", regressaoLinear.coef_)
print("Coeficiente linear (b0): ", regressaoLinear.intercept_)

previsao_Linear = regressaoLinear.predict(x_planoSaude)

# Grafico Regressão Linear
plt.figure()
grafico = plt.scatter(x=x_planoSaude.ravel(), y=y_planoSaude.ravel())
grafico = plt.plot(x_planoSaude.ravel(), previsao_Linear.ravel(), color='red')

# Mostrar os residuais
erros = y_planoSaude - previsao_Linear



# Previsão com valor específico
valor_especifico = np.array([[40]])
print(valor_especifico.shape)

Valor_Plano = regressaoLinear.predict(valor_especifico)
print(f"Valor do plano de saúde para {valor_especifico[0][0]} anos: R$", Valor_Plano[0][0].round(2))

# Verificação do escore R²
r2 = regressaoLinear.score(x_planoSaude, y_planoSaude)
print(f"Escore R²: {r2}")

# Regressão Polinomial
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3)
x_planoSaude_poly = poly.fit_transform(x_planoSaude)

print(x_planoSaude_poly)
regressaoPolinomial = LinearRegression()
regressaoPolinomial.fit(x_planoSaude_poly, y_planoSaude)
previsao_Polinomial = regressaoPolinomial.predict(x_planoSaude_poly)


erros_poly = y_planoSaude - previsao_Polinomial

plt.figure()
grafico = plt.plot(x_planoSaude.ravel(), erros_poly.ravel(), color='orange')
grafico = plt.plot(x_planoSaude.ravel(), erros.ravel(), color='blue')

# Grafico Regressão Polinomial
plt.figure()
grafico = plt.scatter(x=x_planoSaude.ravel(), y=y_planoSaude.ravel())
grafico = plt.plot(x_planoSaude.ravel(), previsao_Polinomial.ravel(), color='green')
# plt.show()

# erro R² Regressão Polinomial
r2_poly = regressaoPolinomial.score(x_planoSaude_poly, y_planoSaude)
print(f"Escore R² Regressão Polinomial: {r2_poly}")

# Previsão com valor específico - Regressão Polinomial
idade = np.array([[40]])
valor_do_plano = regressaoPolinomial.predict(poly.transform(idade))
print(f" Valor do plano = {valor_do_plano[0][0].round(2)}")

print(x_planoSaude)
print(y_planoSaude)

from sklearn.tree import DecisionTreeRegressor
regressaoArvore = DecisionTreeRegressor()
regressaoArvore.fit(x_planoSaude, y_planoSaude)

previsao_Arvore = regressaoArvore.predict(x_planoSaude)

# score R² - Regressão Árvore de Decisão
r2_arvore = regressaoArvore.score(x_planoSaude, previsao_Arvore)
print(f"Escore R² Regressão Árvore de Decisão: {r2_arvore}")

# Gráfico Regressão Árvore de Decisão


idades = np.array([[28,29,30,31,32]])
valores_planos = regressaoArvore.predict(idades.reshape(-1,1))
print(f"Valores dos planos para as idades {idades}: {valores_planos}")

x_testes_arvore = np.arange(min(x_planoSaude),max(x_planoSaude),0.1).reshape(-1,1)
previsao_Arvore_testes = regressaoArvore.predict(x_testes_arvore)

plt.figure()
grafico = plt.scatter(x=x_planoSaude.ravel(), y=y_planoSaude.ravel())
grafico = plt.plot(x_testes_arvore.ravel(), previsao_Arvore_testes.ravel(), color='purple')
plt.show()

# Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor
randomForest = RandomForestRegressor(n_estimators=100)
randomForest.fit(x_planoSaude, y_planoSaude)
previsao_RandomForest = randomForest.predict(x_planoSaude)
r2_randomForest = randomForest.score(x_planoSaude, y_planoSaude)
print(f"Escore R² Regressão Random Forest: {r2_randomForest}")

# Gráfico Regressão Random Forest
previsao_randomForestCompleto = randomForest.predict(x_testes_arvore)

plt.figure()
grafico = plt.scatter(x=x_planoSaude.ravel(), y=y_planoSaude.ravel())
grafico = plt.plot(x_testes_arvore.ravel(), previsao_randomForestCompleto.ravel(), color='brown')
plt.show()