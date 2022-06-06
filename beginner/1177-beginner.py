t = int(input())
x = 0
n = [0]*1000

for i in range(1000):
    if x < t:
        n[i] = x
        x += 1
    else:
        n[i] = 0
        x = 1

for i in range(1000):
    print(f'N[{i}] = {n[i]}')
