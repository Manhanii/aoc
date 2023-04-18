
with open('9.txt') as f:
    lines = [l.strip().split(' ') for l in f.readlines()]

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, p):
        return abs(self.x - p.x), abs(self.y - p.y)

def solucao(nos):
    ponto_cauda = [Ponto()]
    pontos = [Ponto() for _ in range(nos)]

    for direcao, i in lines:
        if direcao in ['R', 'L']:
            move, dir_ = ('x', 1) if direcao == 'R' else ('x', -1)
        if direcao in ['U', 'D']:
            move, dir_ = ('y', 1) if direcao == 'U' else ('y', -1)

        for j in range(int(i)):
            h = pontos[0]
            setattr(h, move, getattr(h, move) + 1*dir_)
            for k in range(1, nos):
                p = pontos[k]
                ponto_antes = pontos[k-1]
                xd, yd = ponto_antes.dist(p)
                if xd > 1 or yd > 1:
                    if p.x < ponto_antes.x:
                        p.x += 1
                    elif p.x > ponto_antes.x:
                        p.x -= 1
                    if p.y < ponto_antes.y:
                        p.y += 1
                    elif p.y > ponto_antes.y:
                        p.y -= 1
                    if k == len(pontos) - 1:
                        ponto_cauda.append(Ponto(p.x, p.y))


    return len(set([(p.x, p.y) for p in ponto_cauda]))

print("resposta 1: ", solucao(2))
print("resposta 2: ", solucao(10))