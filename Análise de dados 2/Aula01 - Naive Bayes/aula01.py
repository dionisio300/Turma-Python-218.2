import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

base_risco_credito = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula1/risco_credito.csv")

# print(base_risco_credito)

# pip install scikit-learn

# Dividindo a base em previsores e classes
X_risco_credito = base_risco_credito.iloc[:,0:4].values
Y_risco_credito = base_risco_credito.iloc[:,4].values

# print(X_risco_credito)
# print(Y_risco_credito)

# Transformando atributos categóricos em numéricos - Label Encoder
from sklearn.preprocessing import LabelEncoder

label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantia = LabelEncoder()
label_encoder_renda = LabelEncoder()


X_risco_credito[:,0] = label_encoder_historia.fit_transform(X_risco_credito[:,0])
X_risco_credito[:,1] = label_encoder_divida.fit_transform(X_risco_credito[:,1])
X_risco_credito[:,2] = label_encoder_garantia.fit_transform(X_risco_credito[:,2])
X_risco_credito[:,3] = label_encoder_renda.fit_transform(X_risco_credito[:,3])

print(X_risco_credito)

# Criando o classificador Naive Bayes
naive_Numerico = GaussianNB()
naive_Numerico.fit(X_risco_credito, Y_risco_credito)

print(naive_Numerico.class_prior_)

# classication report
from sklearn.metrics import classification_report
y_risco_credito_predito = naive_Numerico.predict(X_risco_credito)
print(classification_report(Y_risco_credito, y_risco_credito_predito))

while True:
    opcao = input('1 - Prever\n2 - Sair\n')
    if opcao == '2':
        break
    if opcao == '1':
        historia = input(f'História ( {label_encoder_historia.classes_[0]}, {label_encoder_historia.classes_[1]} ou {label_encoder_historia.classes_[2]}): ')
        divida = input(f'Divida ( {label_encoder_divida.classes_[0]} ou {label_encoder_divida.classes_[1]} ): ')

        garantias = input(f'Garantias ( {label_encoder_garantia.classes_[0]} ou  {label_encoder_garantia.classes_[1]} ): ')

        renda  = input(f'Renda ( {label_encoder_renda.classes_[0]}, {label_encoder_renda.classes_[1]} ou {label_encoder_renda.classes_[2]} ): ')

        historia = label_encoder_historia.transform([historia])
        divida = label_encoder_divida.transform([divida])
        garantias = label_encoder_garantia.transform([garantias])
        renda = label_encoder_renda.transform([renda])

        entrada = np.array([historia, divida, garantias, renda])
        entrada = entrada.reshape(1, -1)

        previsao = naive_Numerico.predict(entrada)
        print(f'Previsão de risco: {previsao[0]}')