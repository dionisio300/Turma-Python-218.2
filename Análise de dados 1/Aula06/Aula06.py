import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

census = pd.read_csv("C:\\Users\\dioni\\OneDrive\\Área de Trabalho\Youth Data 218.02\\Curso Data\\218\\Análise de dados 1\\Aula06\\census.csv")

media_educacao = census.groupby('age')['education-num'].mean()
media_horas_trabalho = census.groupby('age')['hour-per-week'].mean()

# Grafico de linhas
# print(media_educacao.index)
# plt.figure(num=1,figsize=(8,5))
# plt.plot(media_educacao.index,media_educacao.values, color="red",marker='x')
# # plt.plot(media_horas_trabalho.index,media_horas_trabalho.values, color="blue")
# plt.title('Média de anos de estudo por idade')
# plt.xlabel('Idades')
# plt.ylabel('Médias de anos de estudo')

# # Histograma

# estado_civil = census['marital-status'].value_counts()
# print(estado_civil)

# plt.figure(num=2,figsize=(8,5))
# sns.histplot(census['marital-status'])
# plt.title('Hitograma do estado civil')
# plt.xlabel('Estado civil')
# plt.ylabel('Contagem')

# # Grafico de barras
# plt.figure(num=3,figsize=(8,5))
# plt.bar(estado_civil.index,estado_civil.values)
# plt.title('Hitograma do estado civil')
# plt.xlabel('Estado civil')
# plt.ylabel('Contagem')
# plt.xticks(rotation=-30)

# genero = census['sex'].value_counts()
# # Grafico de pizza
# plt.figure(num=4,figsize=(8,5))
# plt.pie(genero,labels=genero.index,autopct='%.1f%%')

# #boxplot
# plt.figure(num=5,figsize=(8,5))
# sns.boxplot(data=census,
#             x="marital-status",           # Variável categórica no eixo X
#             y="hour-per-week", # Variável numérica no eixo Y
#             palette="Set2",    # Paleta de cores
#             showmeans=True)    # Mostra a média

# #Gráfico de dispersão
# plt.figure()
# sns.scatterplot(data=census, x='age',y='education-num',hue='race')

# # pairplot

# plt.figure()
# sns.pairplot(census[["age", "education-num", "race"]] ,hue='race')

# mapa de calor

# credit = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\\Análise de dados 1\\Aula06\\credit_data.csv')

# plt.figure()
# sns.heatmap(credit[['age','income','loan','default']].corr(),annot=True, cmap='coolwarm',fmt=".2f")

flores = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 218.02\\Curso Data\\218\Análise de dados 1\\Aula06\\iris2.csv')

flores1 = flores[flores['species'] == 'setosa']
print(flores['species'].value_counts())


plt.show()