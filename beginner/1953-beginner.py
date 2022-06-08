def main():
    n = int(input())
    epr = 0
    ehd = 0
    intrusos = 0

    for _ in range(n):
        a = input().split()
        if a[1] == 'EPR':
            epr += 1
        elif a[1] == 'EHD':
            ehd += 1
        else:
            intrusos += 1

    print(f'EPR: {epr}\nEHD: {ehd}\nINTRUSOS: {intrusos}')

while True:
    try:
        main()
    except EOFError:
        break
