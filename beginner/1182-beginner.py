c = int(input())
t = input()
matriz = []
coluna = []


def soma_coluna(coluna):
    soma = 0
    for i in coluna:
        soma += i
    return soma


for _ in range(12):
    vetor = []
    for _ in range(12):
        m = float(input())
        vetor.append(m)
    matriz.append(vetor)

for i in range(12):
    coluna.append(matriz[i][c])

soma = soma_coluna(coluna)
if t == 'S':
    print(f'{soma:.1f}')
elif t == 'M':
    media = soma / len(coluna)
    print(f'{media:.1f}')
