import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "aula_sqlpython"
    )

cursor = conexao.cursor()

def cadastrar():
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu email: ")
    cpf = input("Digite seu cpf: ")
    endereco = input("Digite seu endereco: ")
    
    sql = "INSERT INTO cliente (nome, telefone, email, cpf, endereco) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, telefone, email, cpf, endereco)
    
    cursor.execute(sql, valores)
    conexao.commit()
    print("Cliente cadastrado com sucosso!")
    
    while True:
        print("1 - CADASTRAR")
        
        op = input("Digite uma opção: ")
        if op == '1':
            cadastrar()
            
            