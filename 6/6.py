
with open('6.txt') as file:
    input = file.read()


for i in range(4, len(input)):
    s = set(input[(i-4):i])
    if len(s) == 4:
        print("resposta 1: ", i)
        break

for i in range(14, len(input)):
    s = set(input[(i-14):i])
    if len(s) == 14:
        print("resposta 2: ", i)
        break