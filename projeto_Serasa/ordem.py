presentes = int(input("Quantas pessoas estão presentes?\n"))
pessoas = []

for i in range(presentes):
    pessoas.append(input("Digite o nome do participante:\n").title())

pessoas.sort() #ordena em ordem crescente alfabética
print("Participantes por ordem alfabética:\n")
print('\n'.join(pessoas))
