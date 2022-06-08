p, n = input().split()
p, n = int(p), int(n)
c = input().split()

for i in range(n):
    c[i] = int(c[i])

for i in range(n):
    if i == n-1:
        print('YOU WIN')
        break
    elif c[i]-p > c[i+1] or c[i+1] > c[i]+p:
        print('GAME OVER')
        break
