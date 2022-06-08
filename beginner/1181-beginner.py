l = int(input())
t = input()
matriz = []


def soma_linha(matriz, linha):
    soma = 0
    for i in matriz[linha]:
        soma += i
    return soma


for _ in range(12):
    vetor = []
    for _ in range(12):
        m = float(input())
        vetor.append(m)
    matriz.append(vetor)

if t == 'S':
    soma = soma_linha(matriz, l)
    print(f'{soma:.1f}')
elif t == 'M':
    soma = soma_linha(matriz, l)
    media = soma / len(matriz[l])
    print(f'{media:.1f}')
