o = input()
matriz = []
soma = 0
tam_matriz_quad = q = 12
ele = (q * q - q) / 2

for _ in range(q):
    vetor = []
    for _ in range(q):
        m = float(input())
        vetor.append(m)
    matriz.append(vetor)

s = 1
for i in range(q):
    for item in matriz[i][s:]:
        soma += item
    s += 1

if o == 'S':
    print(f'{soma:.1f}')
elif o == 'M':
    media = soma / ele
    print(f'{media:.1f}')
