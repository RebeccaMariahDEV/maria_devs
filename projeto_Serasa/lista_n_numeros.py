n = int(input("Digite a quantidade de numeros que deseja processar\n"))
maior =  -1_000_000
menor = 1_000_000

entrada = map(int, input(f"Digite {n} numeros, separado por vírgula:\n").split(","))

for atual in entrada:
    menor = min(menor, atual)
    maior = max(maior, atual)

print(f"Maior é : {maior}")
print(f"Menor é: {menor}")