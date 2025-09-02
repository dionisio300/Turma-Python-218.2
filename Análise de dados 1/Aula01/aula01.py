# Revisão breve de python
# Listas

nomes = ['Ana', 'Bia','Caio','David']
print(nomes[1])

for nome in nomes:
    print(f'Nome: {nome}')

# Dicionário

pessoa = {
    'nome':'Ana',
    'idade':30,
    'cidade':'Fortaleza'
}

print(pessoa)
print(f'Nome: {pessoa['nome']}')
print(f'Idade: {pessoa['idade']}')
print(f'Cidade: {pessoa['cidade']}')

for chave, valor in pessoa.items():
    print(f'{chave} : {valor}')

# funções - Sem parâmetro e sem retorno
def saudacao():
    print('Olá mundo!')

saudacao()

# Função com parâmetro e sem retorno

def saudacaoNome(nome):
    print('Olá '+ nome)

saudacaoNome('Caio')

# Função sem parâmetros e com retorno

def mensagemErro():
    return f'Olá, parece que tivemos um problema'

print(mensagemErro())

# Funções com parâmetros e retorno

def saudacaoNomeIdade(nome,idade):
    if idade >= 18:
        return f'Olá {nome}, você tem {idade} anos de idade e é Adulto'
    else:
        return f'Olá {nome}, você tem {idade} anos e é Menor'
    

print(saudacaoNomeIdade('Maria',10))

# Funções com parâmetros nomeados

print(saudacaoNomeIdade(idade=20,nome='Maria'))

# Funções com parâmetros default

# print(saudacaoNomeIdade())

def saudacaoNomeIdade(nome = '',idade = ''):
    if idade:
        if nome:
            if idade >= 18:
                return f'Olá {nome}, você tem {idade} anos de idade e é Adulto'
            else:
                return f'Olá {nome}, você tem {idade} anos e é Menor'
        else:
            return f'Falta o nome'
    else:
        return f'Faltam Parâmetros'

print(saudacaoNomeIdade(idade=20))


# Classes e Objetos -> Atributos (Variáveis) e Métodos (Funções)
# Conta Bancária

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
    # Depositar
    def depositar(self, valor):
        self.__saldo += valor
        print(f'Depósito de {valor} realizado com sucesso!')
        print(f'Novo Saldo = {self.__saldo}')
    # Sacar
    def sacar(self, valor):
        if valor > self.__saldo:
            print(f'Saldo insuficiente para saque de {valor}.')
        else:
            self.__saldo -= valor
            print(f'Saque de {valor} realizado com sucesso!')
            print(f'Lhe resta {self.__saldo} na sua conta.')
    # Extrato
    def extrato(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo: {self.__saldo}')

conta1 = ContaBancaria('Aline',1000)

conta1.depositar(1000)
conta1.sacar(500)
conta1.sacar(10000)
conta1.extrato()

conta1.saldo = 10000
conta1.extrato()

# 1. Dada a lista de nomes, crie uma nova lista com apenas os nomes com mais de 5 letras

nomes=["Ana", "Bruno", "Carla", "Daniela", "Eva", "Fernanda", "Igor"]

# 2. Dada a lista de notas de alunos, calcule a média apenas dos alunos que tiraram nota maior ou igual a 7

# 3. Escreva uma função que recebe uma lista de notas e retorna:
# a média e o conceito (A: >= 9, B: >= 7, C: >= 5, D: <5)

# 5. Dada uma lista de dicionários com informações de pessoas, calcule a média das idades.
dados=[
{"nome": "Ana", "idade": 23},
{"nome": "Bruno", "idade": 25},
{"nome": "Carlos", "idade": 30},
{"nome": "Diana", "idade": 20}
]
# Resultado
# 6. A partir da mesma lista acima, filtre apenas as pessoas com idade acima de 24.
# pip install pandas
# pip install numpy

# 1. Criando uma Series a partir de uma lista
import pandas as pd
valores = [10,20,30,40]
# Criar a serie
serie1 = pd.Series(valores)
print(valores)
print(serie1)

# 2. Definindo um índice personalizado
indices = ['a','b','c','d']
serie2 = pd.Series(valores,index=indices)
print(serie2['a'])

# 3. Criando a partir de um dicionário

dados = {
    'Maça':14,
    'Banana':10,
    'Laranja':15
}
serie3 = pd.Series(dados,dtype=float)
print(dados)
print(serie3)

# 4. Criando a partir de um valor escalar (repetido)

valor = 1
serie4 = pd.Series(valor,index=[0,1,2,3,4,5])

print(serie4)


dados = {
    'nomes':['Alice','Bruno','Carlos'],
    'Idades':[25,30,35],
    'Cidade':['São Paulo', 'Fortaleza','Caucaia']
}

df1 = pd.DataFrame(dados)
print(dados)
print(df1)

# Indices diferentes
indices = ['a','b','c']

df2 = pd.DataFrame(dados,index=indices)
print(df2)

# 3. Criando a partir de uma lista de dicionários
dados2 = [
    {'nome':'Alice','idade':25,'cidade':'São Paulo'},
    {'nome':'Bruno','idade':35,'cidade':'Fortaleza'},
    {'nome':'Carlos','idade':20,'cidade':'Caucaia'}
]

df3 = pd.DataFrame(dados2)
print(df3)

credit = pd.read_csv('credit_data.csv')
print(credit)

'''
Atividades :
Atividade 1: Crie uma lista com os nomes de cinco frutas e transforme essa lista em uma Series do pandas.

Atividade 2: Crie uma lista com os valores de temperatura ao longo de 7 dias. Crie uma Series que use os dias da semana como índice.

Atividade 3: Crie uma Series usando um dicionário onde as chaves são nomes de alunos e os valores são suas notas finais.

Atividade 4: Crie uma Series com os números de 1 a 5 e defina índices personalizados em formato de letras.
'''
# Renomear Colunas

credit.rename(columns={
    'clientid': 'ID',
    'income': 'Renda',
    'age': 'idade',
    'loan': 'Dívida',
    'default': 'Inadimplente'
}, inplace=True)

print(credit)

print(credit.describe())