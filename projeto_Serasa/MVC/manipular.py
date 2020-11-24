import csv

"""arquivo = open('curso-mvcad.csv', 'r')
print(arquivo.read())
arquivo.close()

with open('teste.txt', 'w') as file:
    escritor = csv.writer(file)
    escritor.writerow(["oi line", "tudo bem?" ])
    
    
with open('teste.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        nova = 3
        
        
"""

# with open('curso-mvcad.csv', 'r') as filer:
#    for line in filer:
#       print(line)

lista_cabecalho = ['nome', 'idade']
nomeArquivo = 'teste.txt'


def escrever_cabeçalho(lista_cabecalho):
    with open(nomeArquivo, 'a') as file:
        escritor = csv.DictWriter(file, fieldnames=lista_cabecalho, delimiter=',')
        escritor.writeheader()


def escrever_linha(lista_cabecalho):
    with open(nomeArquivo, 'a') as file:
        escritor = csv.DictWriter(file, fieldnames=lista_cabecalho, delimiter=',')
        escritor.writerow(pessoa1)
        escritor.writerow(pessoa2)
        escritor.writerow(pessoa3)


pessoa1 = {
    'nome': 'Lu',
    'idade': 30
}
pessoa2 = {
    'nome': 'Suzi',
    'idade': 28
}
pessoa3 = {
    'nome': 'Becca',
    'idade': 24
}

# escrever_cabeçalho(lista_cabecalho)
escrever_linha(lista_cabecalho)
