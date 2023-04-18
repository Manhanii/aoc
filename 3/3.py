from string import ascii_letters


with open('3.txt') as file:
    data = [i for i in file.read().strip().split("\n")]


# PART 1 


soma = 0
for dados in data:

    meio = len(dados)//2
    
    # Split up the string
    direito = set(dados[:meio])
    esquerdo = set(dados[meio:])

    # print(direito, esquerdo)
    for valor, caractere in enumerate(ascii_letters):
        if caractere in direito and caractere in esquerdo:
            soma += valor + 1

print("resp 1: ", soma)

# ==== PART 2 ====
soma = 0
j = 3
for i in range(0, len(data), 3):
    dados = data[i:j]
    j += 3

    for valor, caractere in enumerate(ascii_letters):
        if caractere in dados[0] and caractere in dados[1] and caractere in dados[2]:
            soma += valor + 1


print("resp 2: ", soma)