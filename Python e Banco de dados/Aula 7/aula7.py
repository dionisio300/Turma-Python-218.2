# Questão: Sistema de Biblioteca
# Enunciado:
# Crie um programa em Python que simule um sistema de biblioteca. O programa deve permitir que o usuário realize as seguintes operações:

# Cadastrar Livro: O usuário pode cadastrar um novo livro, informando título, autor e quantidade de cópias disponíveis.

def cadastrar_livro(livros):
    titulo = input('Titulo: ')
    autor = input('Autor: ')
    copias = int(input('Cópias: '))
    # Criando o dicionário
    livro = {'titulo':titulo, 'autor':autor, 'copias':copias}

    # Adicionando o dicionário na lista
    livros.append(livro)
    print(livros)




# Verificar Disponibilidade: O usuário pode verificar se um livro está disponível para empréstimo.
# lista_livros = [
#     {'titulo':'O pequeno Prinicipe', 'autor':'autor1','copias':20},
#     {'titulo':'Harry Potter', 'autor':'JK Rowling','copias':20}
# ]

def verficar_disponibilidade(livros):
    titulo = input('Livro: ')
    for livro in livros:
        if livro['titulo'] == titulo:
            if livro['copias'] > 0:
                print('Livro Disponível')
                return
            else:
                print('Livro indisponível')
                return
    print('Livro não encontrado')



# Emprestar Livro: O usuário pode emprestar um livro, reduzindo a quantidade de cópias disponíveis.

def emprestar_livro(livros):
    titulo = input('Livro: ')
    for livro in livros:
        if livro['titulo'] == titulo:
            if livro['copias'] > 0:
                print('Livro Disponível')
                livro['copias'] -= 1
                print(f'Livro emprestado com sucesso. Quantidade disponível: {livro['copias']}')
                return
            else:
                print('Livro indisponível')
                return
    print('Livro não encontrado')


# Devolver Livro: O usuário pode devolver um livro, aumentando a quantidade de cópias disponíveis.

def devolver_livro(livros):
    titulo = input('Título: ')
    for livro in livros:
        if titulo == livro['titulo']:
            livro['copias'] += 1
            print('Livro devolvido com sucesso!!')
            return
    print('Livro não encontrado!!')


# Listar Livros: O usuário pode visualizar todos os livros cadastrados na biblioteca, com suas informações detalhadas.

def listar_livros(livros):
    for livro in livros:
        print(f'Título: {livro["titulo"]} | Autor: {livro["autor"]} | Cópias: {livro["copias"]}')

# O programa deve ser interativo, exibindo um menu para o usuário escolher a operação desejada. Use dicionários para armazenar as informações dos livros e listas para armazenar todos os livros cadastrados.


# Estrutura Esperada:
# Use uma lista para armazenar os livros, onde cada livro é um dicionário com as chaves: titulo, autor e copias.

lista_livros = [
    {'titulo':'O pequeno Prinicipe', 'autor':'autor1','copias':20},
    {'titulo':'Harry Potter', 'autor':'JK Rowling','copias':20}
]

# Use funções para cada operação (cadastrar, verificar, emprestar, devolver, listar).

# Use um loop para manter o programa em execução até que o usuário escolha sair.

while True:
    opcoes = input('1 - Cadastrar\n2 - Verificar\n3 - Emprestar\n4 - Devolver\n5 - Listar\n6 - Sair\n')
    if opcoes == '6':
        print('Saindo...')
        break
    if opcoes == '1':
        cadastrar_livro(lista_livros)
    if opcoes == '2':
        verficar_disponibilidade(lista_livros)
    if opcoes == '3':
        emprestar_livro(lista_livros)
    if opcoes == '4':
        devolver_livro(lista_livros)
    if opcoes == '5':
        listar_livros(lista_livros)
    

