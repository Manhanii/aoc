values = [1]
with open('10.txt') as file:
    for line in file.readlines():
        line = line.strip().split(' ')
        values.append(values[-1])        
        if line[0] == 'addx':
            values.append(int(line[1]) + values[-1])
print("RESPOSTA1: ", sum([x * values[x-1] for x in range(20, 221, 40)]))
for i in range(len(values)):
    print('#' if abs(values[i] - (i % 40)) <= 1 else ' ', end='')
    print('\n' if ((i+1) % 40 == 0) else '', end='')
