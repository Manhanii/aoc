
with open("8.txt") as file:
    data = [row.strip() for row in file.readlines()]

linhas = len(data)          
colunas = len(data[0])      

borda = (linhas*2) + ((colunas-2)*2)    
total = borda                           
pontos = []                             

for row in range(1, linhas-1):
    for col in range(1, colunas-1):
        arvores = data[row][col]           


        esquerda = [data[row][col-i] for i in range(1, col+1)]
        direita = [data[row][col+i] for i in range(1, colunas-col)]
        cima = [data[row-i][col] for i in range(1, row+1)]
        baixo = [data[row+i][col] for i in range(1, linhas-row)]

    
        if max(esquerda)<arvores or max(direita)<arvores or max(cima)<arvores or max(baixo)<arvores:
            total += 1


        ponto = 1
        for lst in (esquerda, direita, cima, baixo):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < arvores:
                    tracker += 1
                elif lst[i] >= arvores:
                    tracker += 1
                    break
            
            ponto *= tracker

        pontos.append(ponto)

print("resposta 1:", total)
print("resposta 2:", max(pontos))