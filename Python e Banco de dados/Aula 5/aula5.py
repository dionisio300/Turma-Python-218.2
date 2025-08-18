# Questão: Sistema de Biblioteca
# Enunciado:
# Crie um programa em Python que simule um sistema de biblioteca. O programa deve permitir que o usuário realize as seguintes operações:

# Cadastrar Livro: O usuário pode cadastrar um novo livro, informando título, autor e quantidade de cópias disponíveis.

def cadastrar_livro(titulo,autor,copias,livros):
    livro = {'titulo':titulo,'autor':autor, 'copias':copias}
    livros.append(livro)
    print('Livro adicionado com sucesso!')


# Verificar Disponibilidade: O usuário pode verificar se um livro está disponível para empréstimo.

def verificar_disponibilidade(titulo, livros):
    for livro in livros:
        if titulo == livro['titulo']:
            print(f'O livro está disponível\nCópias: {livro['copias']}')
            return
        
    print('O livro não foi encontrado!')

# Emprestar Livro: O usuário pode emprestar um livro, reduzindo a quantidade de cópias disponíveis.

def emprestar(titulo,livros):
    for livro in livros:
        if titulo == livro['titulo']:
            if livro['copias'] > 0:
                livro['copias'] -= 1
                return 'Empréstimo realizado com sucesso'
            else:
                return 'Livro não disponível'
        
    return 'Livro não encontrado'

# Devolver Livro: O usuário pode devolver um livro, aumentando a quantidade de cópias disponíveis.

def devolver(titulo,livros):
    for livro in livros:
        if titulo == livro['titulo']:
           livro['copias'] += 1
           return 'Livro devolvido!'
        
    return 'Livro não encontrado'

# Listar Livros: O usuário pode visualizar todos os livros cadastrados na biblioteca, com suas informações detalhadas.

def listar_livros(livros):
    for livro in livros:
        print(f'Título : {livro['titulo']}, Autor: {livro['autor']}, Cópias: {livro['copias']}')

# O programa deve ser interativo, exibindo um menu para o usuário escolher a operação desejada. Use dicionários para armazenar as informações dos livros e listas para armazenar todos os livros cadastrados.


# Estrutura Esperada:
# Use uma lista para armazenar os livros, onde cada livro é um dicionário com as chaves: titulo, autor e copias.
lista_livros = [
    {'titulo':'O pequeno Príncipe','autor':'Frances','copias':10},
    {'titulo':'Harry Potter','autor':'JK Rowling','copias':5},
    {'titulo':'Game of Thrones','autor':'Jorge RR Martin','copias':8}
]
# Use funções para cada operação (cadastrar, verificar, emprestar, devolver, listar).

# Use um loop para manter o programa em execução até que o usuário escolha sair.

while True:
    opcao = input('1 - Cadastrar\n2 - Verificar\n3 - Emprestar\n4 - Devolver\n5 - listar\n6 - Sair\n')
    if opcao == '6':
        print('Saindo...')
        break
    if opcao == '1':
        titulo = input('Título: ')
        autor = input('Autor: ')
        copias = int(input('Cópias: '))
        cadastrar_livro(titulo,autor,copias,lista_livros)
    if opcao == '5':
        listar_livros(lista_livros)
    if opcao == '2':
        titulo = input('Qual livro? ')
        verificar_disponibilidade(titulo,lista_livros)
    if opcao == '3':
        titulo = input('Qual livro? ')
        mensagem = emprestar(titulo,lista_livros)
        print(mensagem)
    if opcao == '4':
        titulo = input('Qual livro? ')
        mensagem = devolver(titulo,lista_livros)
        print(mensagem)
        