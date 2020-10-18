"""
Exercícios Python [1]
Você possui uma variável a = 10 e uma variável b = 5, e precisa trocar o valor das duas. Como você faria?
"""

a = 10
b = 5
a, b = b, a
print(a, b)
nome = "Ana Roberta"
print(f"Olá meu nome é {nome}")

"""
Exercícios Python [2]¶
Faça um programa que pergunte que dia é, e diga quantos faltam até o final do mês. Considere o mês com trinta e um dias.
"""


dia = int(input('Que dia é hoje?'))
mes = 30 - dia
print(f"Faltam {mes} para acabar o mês")


"""
Exercícios Python [3]
Faça um programa que receba o número de brindes do Maria vai com as Devs que a Jéssica vai mandar fazer,
e imprima quanto de entrada ela irá que pagar. Considere que cada brinde custa R$25,00, e a entrada para o fabricante é de 50% do valor total.
"""


quantidade = int(input("Quantos brinde quer fazer?"))
unidade = 25
entrada = quantidade * unidade / 2
print(f"O valor da entrada será de {entrada:.2f}")




"""
Exercícios Python [4]
A Serasa irá gerar um minicurso de aprendizagem financeira e está planejando um coffee break ás 15 horas.

Leia o número de participantes do minicurso e imprima:

Quantos litros de refrigerante teremos que comprar
Quantas coxinhas e quanto iremos gastar.
Considere que cada participante toma 400ml de refrigerante, come 10 coxinhas, que cada litro de refrigerante custa 4,00 e cada coxinha custa 0,50.
"""

participantes = int(input("Qual o numero de participantes do curso?"))

#Refri
litro_1 = 4.0
consumo_participante = 0.400
consumo_refri = participantes * consumo_participante
total_refri = consumo_refri * litro_1
#print(consumo_refri)
#print(total_refri)

#coxinha
coxinha_1 = .50
consumo_coxinha = 10
salgado = consumo_coxinha * participantes
total = salgado * coxinha_1
#print(salgado)
#print(total)

#gastos
gastos= total + total_refri

print(f"Serão necessários comprar {consumo_refri} litros de refrigerante.\nSerão necessários comprar {salgado} unidades de coxinhas.\nIremos gastar R${gastos}")



"""
Exercícios Python [5]
Para que a jéssica consiga enviar os brindes e não errar na preferência de cores de todas as participantes, 
ela precisa saber a quantidade de pessoas que preferem a cor rosa, roxo ou azul. Faça um programa que leia a quantidade 
de pessoas que preferem cada cor e retorne a porcentagem de cada uma destas cores.
"""
rosa, roxo, azul = map(int, input("Informe separado por virgulas quantas participantes por cor: ").split(","))
total_participantes = rosa + roxo + azul

porcentagem_rosa = rosa / total_participantes * 100
porcentagem_roxo = roxo / total_participantes * 100
porcentagem_azul = azul / total_participantes * 100

print(f"{porcentagem_rosa:.2f} % de pessoas preferem rosa.")
print(f"{porcentagem_roxo:.2f} % de pessoas preferem roxo.")
print(f"{porcentagem_azul: .2f} % de pessoas preferem azul.")


"""

Exercícios Python [6]¶
Dez pessoas assinalaram que iriam participar do encontro do Maria vai com as Devs hoje.

Faça um programa que leia o número de pessoas presentes e escreva “Sucesso!” se todas as pessoas compareceram, e “Alguém faltou :/” caso contrário.

Se houverem mais de dez pessoas imprima “Temos um intruso entre nós :v”.

"""

presentes = int(input("Quantas pessoas estão presentes no evento hoje? "))
if presentes == 10:
    print("Sucesso!")
elif presentes <= 9:
    print("Alguém faltou")
else:
    print("Temos um intruso entre nós")




"""
Exercícios Python [7]
Receba duas notas, uma é de uma prova e outra é de um trabalho, por fim retorne:

Se a nota da prova for maior ou igual a 5 e nota do trabalho maior que 6: “Aprovado”; Senão: “Reprovado”.
"""

nota_traballho = float(input("Qual a nota do trabalho? "))
nota_prova = float(input("Qual a nota da prova? "))
if nota_prova >= 5 or nota_prova <= 10 and nota_traballho >= 6 or nota_traballho <= 10:
    print("Aprovado")
else:
    print("Reprovado")



"""
Exercícios Python [8]
A Serasa anualmente promove a ida dos desenvolvedores para a Python Brasil, mas como temos um número limitado de ingressos disponíveis, pode ser necessário decidir quem irá.

Como critério de desempate sobre os ingressos, quem nunca participou do evento terá prioridade.

Receba o número de ingressos disponíveis, o número total de interessados e o número de interessados que já participaram do evento antes, 
diga se é possível distribuir os ingressos apenas com essas regras, ou se será necessário um sorteio.
"""
ingressos = int(input("Quantos ingressos disponíveis? "))
interessados = int(input("Quantas pessoas estão interessadas? "))
ja_participaram = int(input("Quantos já participaram do evento antes? "))

if interessados <= ingressos:
        print("Todos podem ir")
elif interessados >= ingressos:
    if ja_participaram <= interessados:
        print("Os que não foram vão ser escolhidos, os outros serão sorteio")
else:
    print("Teremos que fazer um sorteio")

"""
Exercícios Python [9]
Nos últimos anos o Brasil está com muita variação de temperatura, e uma coisa louca acontecendo é que você pode passar 
por várias estações do ano num mesmo dia! Para ajudar as pessoas a não pegar uma gripe ou uma insolação, você vai ler a 
temperatura e a umidade do ar da tabela a seguir,e criar um programa que classifica quais itens de sobrevivência são necessários para nossos dias de “verão”.

Temperatura às 8h - ºC	Umidade do ar - %	Itens de sobrevivência
10ºC < 15ºC	0 <= 40	Blusa de frio e regata
10ºC < 15ºC	40 <= 100	Blusa de frio, regata e guarda-chuva
15ºC < 20ºC	0 < 40	Blusa de frio e regata
15ºC < 20ºC	40 <= 100	Blusa de frio, regata e guarda-chuva
20ºC < 25ºC	0 < 40	Regata
20ºC < 25ºC	40 <= 100	Regata e guarda-chuva
"""
temperatura = int(input("Quantos graus está lá fora? "))

umidade = int(input("Qual a umidade do ar? "))

if (temperatura >=10 or temperatura <= 15) and (umidade <= 40 or umidade >= 0):
    print("Vai precisar de uma blusa de frio e regata")

elif (temperatura >= 10 or temperatura <= 15) and (umidade <=100 or umidade >= 40):
    print("Blusa de frio, regata e guarda-chuva")

elif (temperatura >= 15 or temperatura <= 20) and (umidade <= 40 or umidade >= 0):
    print("Blusa de frio e regata")

elif (temperatura >= 15 or temperatura <= 20) and (umidade <= 100 or umidade >= 40):
    print("Blusa de frio, regata e guarda-chuva")

elif (temperatura >= 20 or temperatura <= 25) and (umidade <= 40 or umidade >= 0):
    print("Regata")

else:
    print("Regata e guarda-chuva")


"""
Exercícios Python [10]
Você é o responsável por gerar os certificados dos da trilha financeira da serasa, 
porém, sabemos que eventualmente os participantes não cooperam e escrevem seus nomes sem seguir a norma padrão, 
apenas com a primeira letra maiúscula. Para evitar certificados despadronizados, você resolveu escrever um programa em Python para normalizar os nomes para você!

O programa recebe um nome e padroniza o nome para você:
"""
nome = input("Qual seu nome? ")
corrigido = nome.capitalize()
print(corrigido)



"""
Exercício Python[11]
Leia números enquanto a soma dos números lidos seja menor que 20.
"""
numero = input("Digite um numero: ")
soma = 0
for n in numero:
    n = int(n)
    soma = soma + n
if soma <= 20:
    print(f"A soma dos numeros é {soma}")
else:
    print(soma)

"""

Exercicio Pyhton [12]
Possuímos uma lista de cinco desenvolvedoras que participam do programa Maria vai com as devs. Elas se chamam: Andorinha, Azaléia, Amélia, Margarida e Rosa.

Construa um programa que descubra quantas delas possuem o nome começando com a letra “A”.
"""
devs = ["Andorinha", "Azaléia", "Amélia", "Margarida", "Rosa"]
letra = "A"
for dev in devs:
    if dev[0] == letra:
        print(dev)
