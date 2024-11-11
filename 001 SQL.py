import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "turma_b"
)
opcao = 0
meucursor = banco.cursor()
while opcao != 3:
    opcao = int(input("1 - Pesquisa\n 2 - Inserir\n 3 - Sair\n"))
    if opcao == 1:
        pesquisa = "select * from alunos;"
        meucursor.execute(pesquisa)
        resultado = meucursor.fetchall()
        for x in resultado:
            print(x)
    elif opcao == 2:
        meucursor = banco.cursor()
        nome1 = input("Digite seu nome: ")
        telefone1 = input("Digite seu telefone: ")
        sql = "insert into alunos (nome, telefone) values (%s,%s)"
        data = (nome1, telefone1)
        meucursor.execute(sql, data)
        banco.commit()
    elif opcao == 3:
        print("Programa encerrado.")
        meucursor.close()
        banco.close()