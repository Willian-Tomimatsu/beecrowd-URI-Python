ln = [0]*20

for i in range(20):
    x = int(input())
    ln[i] = x

for i in range(20):
    print(f'N[{i}] = {ln[-(i+1)]}')
