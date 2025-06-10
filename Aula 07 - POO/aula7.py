# Criação de uma classe
class Livro:
    def __init__(self,titulo,autor,ano_publicacao):
        # Criação dos atributos
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.status = 'disponivel'
    def emprestar(self):
        if self.status == 'disponivel':
            self.status = 'emprestado'
        else:
            print('Livro indisponível')
    def devolver(self):
        self.status = 'disponivel'
    def detalhes(self):
        return f'Título: {self.titulo}, autor: {self.autor}, Ano de puclicação: {self.ano_publicacao}, status: {self.status}'

# instância de um objeto
livro = Livro('Cálculo','James Stewart',2013)

# Acessando um método do objeto criado
livro.emprestar()

print(livro.detalhes())

# Acessando atributos de um objeto
print(livro.titulo)

livro.titulo = 'O pequeno príncipe'

print(livro.titulo)

#1. Crie uma classe chamada ContaBancaria que represente uma conta bancária.
#A classe deve ter os atributos saldo e titular. Implemente métodos para depositar, sacar everificar o saldo da conta. 

# 2. Crie classe Calculadora com os conceitos de POO. Ela deverá ter as 4 operações básicas como métodos.

#3. Crie uma classe chamada Círculo. Essa classe deverá ter o raio como atributo e os métodos calcular área e círculo e calcular perímetro.

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)

    def listarLivrosDisponiveis(self):
        print('Livros disponíveis: ')
        for livro in self.livros:
            if livro.status == "disponivel":
                print(livro.detalhes())
    def emprestar(self,titulo):
        for livro in self.livros:
            if titulo == livro.titulo:
                livro.emprestar()
                print(f'Livro {titulo} emprestado com sucesso')
                return
        print(f'O livro {titulo} não foi encontrado!')
    def devolver(self,titulo):
        for livro in self.livros:
            if titulo == livro.titulo:
                livro.devolver()
                print(f'Livro {titulo} devolvido com sucesso')
                return
        print(f'O livro {titulo} não foi encontrado!')
            



bece = Biblioteca()

livro1 = Livro("Ilíada","Homero",700)
livro2 = Livro("A divina comédia","Dante",1304)
livro3 = Livro("Hamlet","Willian",1603)

bece.adicionarLivro(livro1)
bece.adicionarLivro(livro2)
bece.adicionarLivro(livro3)

while True:
    opcao = input(f'Digite uma opção:\n1 - Cadastrar Livro\n2 - Emprestar Livro\n3 - Devolver Livro\n4 - Listar Livros Disponíveis\n5 - Sair\n')
    if opcao == '5':
        break
    if opcao == '1':
        titulo = input('Título: ')
        autor = input('Autor: ')
        ano = input('Ano: ')
        livro = Livro(titulo,autor,ano)
        bece.adicionarLivro(livro)
    if opcao == '2':
        titulo = input('Titulo: ')
        bece.emprestar(titulo)
    if opcao == '3':
        titulo = input('Titulo: ')
        bece.devolver(titulo)
    if opcao == '4':
        bece.listarLivrosDisponiveis()
