
with open('4.txt') as file:
    data = [i for i in file.read().strip().split("\n")]


pares = 0
for dados in data:
    primeiro, segundo = dados.split(",")
    primeiro = [int(i) for i in primeiro.split("-")]
    segundo = [int(i) for i in segundo.split("-")]

    if primeiro[0] <= segundo[0] and primeiro[1] >= segundo[1]:
        pares += 1
    elif segundo[0] <= primeiro[0] and segundo[1] >= primeiro[1]:
        pares += 1

print("resposta 1:", pares)

pares = 0
for dados in data:
    primeiro, segundo = dados.split(",")
    primeiro = [int(i) for i in primeiro.split("-")]
    segundo = [int(i) for i in segundo.split("-")]

    if primeiro[0] in range(segundo[0], segundo[1]+1) or primeiro[1] in range(segundo[0], segundo[1]+1):
        pares += 1
    elif segundo[0] in range(primeiro[0], primeiro[1]+1) or segundo[1] in range(primeiro[0], primeiro[1]+1):
        pares += 1


print("resposta 2:", pares)