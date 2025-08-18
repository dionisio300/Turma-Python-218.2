import mysql.connector as my
def conectarBanco():
    return my.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'curso'
    )


def ler_alunos():
    conexao = conectarBanco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from alunos'
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(f"Nome: {resultado['nome']} - Matrícula: {resultado['matricula']}")

    conexao.close()
    return resultados


def inserir_aluno():
    conexao = conectarBanco()
    nome = input('Digite o nome do aluno: ')
    matricula = input('Digite a matrícula: ')
    sql = 'insert into alunos (nome, matricula) values (%s,%s)'
    cursor = conexao.cursor()
    cursor.execute(sql,(nome,matricula))
    conexao.commit()
    conexao.close()

def atualizar_nome_aluno():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    sql = 'update alunos set nome = %s where id = %s'
    id = int(input('Digite o ID do aluno: '))
    nome = input('Digite o nome do aluno: ')
    cursor.execute(sql,(nome,id))
    conexao.commit()
    conexao.close()

def deletar_aluno():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    sql = 'delete from alunos where id = %s'
    id = int(input('Digite o ID a ser deletado: '))
    cursor.execute(sql,(id,))
    conexao.commit()
    conexao.close()

# ler_alunos()

# inserir_aluno()

# ler_alunos()

# atualizar_nome_aluno()
ler_alunos()
deletar_aluno()
ler_alunos()






