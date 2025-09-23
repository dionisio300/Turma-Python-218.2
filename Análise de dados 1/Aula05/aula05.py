import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dadosCensus = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 1\\Aula05\\census.csv')

# # Histograma das idades

# plt.figure()
# plt.hist(dadosCensus['age'], color='blue', edgecolor='black')
# plt.title('Histograma das Idades')
# plt.xlabel('Idade')
# plt.ylabel('Quantidade')

# # Grafico de pizza

# income_counts = dadosCensus['income'].value_counts()
# plt.figure()
# plt.pie(income_counts,labels=income_counts.index,colors=['blue', 'red'])
# plt.title('Distribuição de Renda')
# print(income_counts)

# # boxplot

# plt.figure()
# sns.boxplot( y='education-num', data=dadosCensus)

# plt.figure()
# sns.scatterplot(x='age', y='education-num', data=dadosCensus, hue='race')

# plt.figure()
# sns.pairplot(dadosCensus, hue='income', vars=['age', 'education-num', 'hour-per-week','capital-gain'])

plt.figure()
sns.heatmap(dadosCensus[['age', 'education-num', 'hour-per-week']].corr(), annot=True, cmap='coolwarm')

plt.show()

'''
1.	Tendência dos estudos por idade
A coordenação de políticas públicas quer saber se os anos médios de escolaridade aumentam ou diminuem com a idade da população.
o	Use um gráfico de linha no Matplotlib mostrando a média de education-num por age.
o	Lembre-se de colocar título e rótulos nos eixos.
________________________________________
2.	Quem são os estados civis mais frequentes?
O setor de estatísticas sociais deseja identificar quais são os 5 estados civis mais comuns.
o	Faça um gráfico de barras no Matplotlib com as 5 categorias mais frequentes de marital-status.
o	Coloque título e gire os rótulos do eixo X para facilitar a leitura.
________________________________________
3.	Proporção de homens e mulheres
Uma ONG de gênero quer ter uma noção geral da proporção de homens e mulheres na base.
o	Use um gráfico de pizza no Matplotlib para mostrar a distribuição de sex.
o	Mostre também os percentuais em cada fatia.
________________________________________
4.	Distribuição de idades
Um pesquisador está estudando a composição etária. Ele quer enxergar se existem mais jovens, adultos ou idosos.
o	Construa um histograma no Seaborn (sns.histplot) para age.
o	Use 30 faixas de idade (bins) e adicione uma curva de densidade.
________________________________________
5.	Horas semanais por sexo
O setor de trabalho deseja comparar as jornadas médias entre homens e mulheres.
o	Crie um boxplot no Seaborn comparando hour-per-week em função de sex.
o	Analise se há diferenças entre os grupos.
________________________________________
6.	Educação e idade coloridas por renda
Um estudo de mobilidade social quer entender se há relação entre idade, anos de estudo e renda.
o	Monte um scatterplot no Seaborn usando age no eixo X, education-num no eixo Y e income como cor.
o	Use transparência nos pontos (alpha) para melhorar a visualização.
________________________________________
7.	Mapa de correlações
Para avaliar quais variáveis andam juntas, um economista pediu um resumo em forma de mapa de calor.
o	Gere um heatmap no Seaborn mostrando a correlação entre age, education-num, hour-per-week, capital-gain e capital-loos.
o	Inclua os valores numéricos dentro da figura.
________________________________________
8.	Visão geral de múltiplas variáveis
O grupo de pesquisa em desigualdade social quer uma visão ampla de como idade, anos de estudo e horas semanais se relacionam com a renda.
o	Crie um pairplot no Seaborn com age, education-num, hour-per-week e income como cor.
o	Observe se há padrões entre os grupos.
________________________________________
9.	Exploração rápida com Pandas
Antes de preparar gráficos mais elaborados, um analista quer só um panorama inicial.
o	Usando apenas o Pandas, faça:
	um histograma da coluna age;
	um boxplot comparando age e education-num.


'''

