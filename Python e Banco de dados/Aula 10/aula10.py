import mysql.connector as my

def conectar_banco():
    conexao = my.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'lojadb'
    )
    return conexao

def listar_clientes():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from clientes'
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(f'Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, E-mail: {resultado['email']}')
    conexao.close()
    return resultados


def buscar_categoria(busca):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = "select * from produtos where categoria like '%"+busca+"%'"
    print(sql)
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(f'Nome: {resultado['nome']}, Preço: {resultado['preco']}')
    conexao.close()
    return resultados

def inserir_cliente(nome,email,telefone):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'insert into clientes (nome,email,telefone) values (%s,%s,%s)'
    cursor.execute(sql,(nome,email,telefone))
    conexao.commit()
    conexao.close()
    return 'Dados inseridos com sucesso'

def atualizar_funcao(id,novaFuncao):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'update funcionarios set funcao = %s where id = %s'
    cursor.execute(sql,(novaFuncao,id))
    conexao.commit()
    conexao.close()
    return 'Dados atualizados com sucesso'

def deletar_funcionario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'delete from funcionarios where id = %s'
    cursor.execute(sql,(id,))
    conexao.commit()
    conexao.close()
    return 'Dado deletado com sucesso!'

while True:
    opcao = input('1 - Listar os Clientes\n2 - Buscar Categoria\n3 - Inserir Cliente\n4 - Atualizar Função\n5 - Deletar funcionário\n6 - Sair\n')
    if opcao == '6':
        print('Saindo...')
        break
    if opcao == '1':
        listar_clientes()
    if opcao == '2':
        busca = input('Categoria: ')
        buscar_categoria(busca)
    if opcao == '3':
        nome= input('Nome: ')
        email= input('E-mail: ')
        telefone= input('Telefone: ')
        inserir_cliente(nome,email,telefone)
    if opcao == '4':
        id = input('ID: ')
        novaFuncao = input('Nova Função: ')
        atualizar_funcao(id,novaFuncao)
    if opcao == '5':
        id = input('ID: ')
        deletar_funcionario(id)