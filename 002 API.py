import requests, mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "turma_b"
)
meucursor = banco.cursor()
cep = input("Qual é o CEP?\n")
if len(cep) == 8:
    link = f"https://viacep.com.br/ws/{cep}/json/"
    requisicao = requests.get(link)
    print(requisicao)
    dic_requisicao = requisicao.json()

    cep = dic_requisicao["cep"]
    logradouro = dic_requisicao["logradouro"]
    complemento = dic_requisicao["complemento"]
    uf = dic_requisicao["uf"]
    cidade = dic_requisicao["localidade"]
    bairro = dic_requisicao["bairro"]
    print(dic_requisicao)
    sql = "insert into endereco (logradouro, cep, complemento) values (%s,%s,%s)"
    data = (logradouro, cep, complemento)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()
    banco.close()
else:
    print("CEP Inválido")