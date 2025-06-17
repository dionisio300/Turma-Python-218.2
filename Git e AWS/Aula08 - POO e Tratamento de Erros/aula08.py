# # Criação de uma classe
# class Livro:
#     def __init__(self,titulo,autor,ano_publicacao):
#         # Criação dos atributos
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.status = 'disponivel'
#     def emprestar(self):
#         if self.status == 'disponivel':
#             self.status = 'emprestado'
#         else:
#             print('Livro indisponível')
#     def devolver(self):
#         self.status = 'disponivel'
#     def detalhes(self):
#         return f'Título: {self.titulo}, autor: {self.autor}, Ano de puclicação: {self.ano_publicacao}, status: {self.status}'

# # instância de um objeto
# livro = Livro('Cálculo','James Stewart',2013)

# # Acessando um método do objeto criado
# livro.emprestar()

# print(livro.detalhes())

# # Acessando atributos de um objeto
# print(livro.titulo)

# livro.titulo = 'O pequeno príncipe'

# print(livro.titulo)

# #1. Crie uma classe chamada ContaBancaria que represente uma conta bancária.
# #A classe deve ter os atributos saldo e titular. Implemente métodos para depositar, sacar everificar o saldo da conta. 

# # 2. Crie classe Calculadora com os conceitos de POO. Ela deverá ter as 4 operações básicas como métodos.

# #3. Crie uma classe chamada Círculo. Essa classe deverá ter o raio como atributo e os métodos calcular área e círculo e calcular perímetro.

# class Biblioteca:
#     def __init__(self):
#         self.livros = []

#     def adicionarLivro(self, livro):
#         self.livros.append(livro)

#     def listarLivrosDisponiveis(self):
#         print('Livros disponíveis: ')
#         for livro in self.livros:
#             if livro.status == "disponivel":
#                 print(livro.detalhes())
#     def emprestar(self,titulo):
#         for livro in self.livros:
#             if titulo == livro.titulo:
#                 livro.emprestar()
#                 print(f'Livro {titulo} emprestado com sucesso')
#                 return
#         print(f'O livro {titulo} não foi encontrado!')
#     def devolver(self,titulo):
#         for livro in self.livros:
#             if titulo == livro.titulo:
#                 livro.devolver()
#                 print(f'Livro {titulo} devolvido com sucesso')
#                 return
#         print(f'O livro {titulo} não foi encontrado!')
            



# bece = Biblioteca()

# livro1 = Livro("Ilíada","Homero",700)
# livro2 = Livro("A divina comédia","Dante",1304)
# livro3 = Livro("Hamlet","Willian",1603)

# bece.adicionarLivro(livro1)
# bece.adicionarLivro(livro2)
# bece.adicionarLivro(livro3)

# while True:
#     opcao = input(f'Digite uma opção:\n1 - Cadastrar Livro\n2 - Emprestar Livro\n3 - Devolver Livro\n4 - Listar Livros Disponíveis\n5 - Sair\n')
#     if opcao == '5':
#         break
#     if opcao == '1':
#         titulo = input('Título: ')
#         autor = input('Autor: ')
#         ano = input('Ano: ')
#         livro = Livro(titulo,autor,ano)
#         bece.adicionarLivro(livro)
#     if opcao == '2':
#         titulo = input('Titulo: ')
#         bece.emprestar(titulo)
#     if opcao == '3':
#         titulo = input('Titulo: ')
#         bece.devolver(titulo)
#     if opcao == '4':
#         bece.listarLivrosDisponiveis()


class Animal:
    def __init__(self,raca,tamanho,cor):
        self.raca = raca,
        self.tamanho = tamanho,
        self.cor = cor
    def comer(self):
        return 'O animal está comendo'
    def dormir(self):
        return 'O animal está dormindo'

# Encapsulamento -> Variáveis privadas só podem ser acessadas por dentro da própria classe

class ContaBancaria:
    def __init__(self,saldo,titular):
        self.__saldo = saldo # "__NomeVariavel é como definimos que é privada"
        self.titular = titular

    def sacar(self,valor):
        self.__saldo -= valor
        return f'{self.titular} sacou {valor}. Saldo atual: {self.__saldo}'
    def depositar(self,valor):
        self.__saldo += valor
        return f'{self.titular} depositou {valor}. Saldo atual: {self.__saldo}'
    def verificarSaldo(self):
        return self.__saldo


conta1 = ContaBancaria(500,'Maria')

print(conta1.verificarSaldo())

conta1.depositar(1000)

print(conta1.verificarSaldo())


conta1.sacar(700)
print(conta1.verificarSaldo())
print(conta1.verificarSaldo())


# Herança
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return f'Olá meu nome é {self.nome} e tenho {self.idade} anos de idade!'
    
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    def estudar(self):
        return f'{self.nome} está estudando {self.curso}'

class Medico(Pessoa):
    def __init__(self, nome, idade,salario):
        super().__init__(nome, idade)
        self.salario = salario
    def atender():
        return 'O médico está atendendo...'

estudante1 = Estudante('Maria',20,'Python')

estudantes = [
    Estudante('Tiago',21,'JavaScript'),
    Estudante('Caio',20,'C++'),
    Estudante('Elie',19,'Python')
]

print(estudante1.cumprimentar())
print(estudantes)

# Herança multipla

class Base:
    def __init__(self, nome, cor_olhos):
        self.nome = nome
        self.cor_olhos = cor_olhos

    def andar(self):
        return 'Andando...'

    def dormir(self):
        return 'Dormindo...'

    def comer(self):
        return 'Comendo...'


class Mae(Base):
    def __init__(self, nome, cor_olhos, cor_cabelo):
        Base.__init__(self, nome, cor_olhos)
        self.cor_cabelo = cor_cabelo

    def dancar(self):
        return "Dançando..."


class Pai(Base):
    def __init__(self, nome, cor_olhos, cor_pele):
        Base.__init__(self, nome, cor_olhos)
        self.cor_pele = cor_pele

    def cantar(self):
        return 'Cantando...'


class Filha(Mae, Pai):
    def __init__(self, nome, cor_olhos, cor_cabelo, cor_pele, peso: int):
        Mae.__init__(self, nome, cor_olhos, cor_cabelo)
        Pai.__init__(self, nome, cor_olhos, cor_pele)
        self.peso = peso

    def caminhar(self):
        return 'Caminhando...'

filha1 = Filha('Maria','Castanhos','Preto','Parda',10)

print(f'A {filha1.nome} tem olhos {filha1.cor_olhos}, pele {filha1.cor_pele}, cabelo {filha1.cor_cabelo} e pesa {filha1.peso} kg')


# Polimorfismo -> Reescrita de métodos da superclasse

class Animal:
    def emitirSom(self):
        print('Som do Animal')

class Gato(Animal):
    def emitirSom(self):
        print('Miau...')

class Humano(Animal):
    def emitirSom(self):
        print('Olá')

class Cachorro(Animal):
    def passear(self):
        print('Passeando...')

pessoa1 = Humano()
pessoa1.emitirSom()

gato1 = Gato()
gato1.emitirSom()

cachorro1 = Cachorro()
cachorro1.emitirSom()
cachorro1.passear()

