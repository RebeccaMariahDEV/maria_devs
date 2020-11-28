import csv
from MVC import pygres_connection
from MVC import pessao_db


#cabecalho = ['nome,cpf,uf,turma,data_nascimento,email,endereco,período,modulo']
from MVC.pessao_db import retorna_pessoa


def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as filer:
        leitor = csv.DictReader(filer, delimiter=',')

        pygres_connection.cursor.execute("select * from pessoa")
        print(pygres_connection.cursor.fetchall())

        lista_pessoas = [item for item in leitor]
        #print(lista_pessoas)

        #for item in leitor:
         #   print(item)

ler_arquivo()

pessoa = {
    'nome':'rebecca',
    'endereco':'bla bla bla',
    'cpf':'35706454876',
    'estado':'sp',
    'turma':'mvcad',
    'periodo':'manha',
    'modulo':'mvcad'
}
pessao_db.insere_pessoa(pessoa)
print(retorna_pessoa())