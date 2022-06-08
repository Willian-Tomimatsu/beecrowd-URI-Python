o = input()
matriz = []
soma = 0
q = 12  # tamanho da matriz quadrada (par)
ele = (q * q - q - q) / 4

for _ in range(q):
    vetor = []
    for _ in range(q):
        m = float(input())
        vetor.append(m)
    matriz.append(vetor)

s = 2
for i in range(1, q//2):
    for n in range(-1, -s, -1):
        soma += matriz[i][n]
    s += 1

s = q//2
for i in range(q//2, q-1):
    for n in range(-1, -s, -1):
        soma += matriz[i][n]
    s -= 1

if o == 'S':
    print(f'{soma:.1f}')
elif o == 'M':
    media = soma / ele
    print(f'{media:.1f}')
