i = 0
while i <= 10:
    j = i*0.2
    if str(j)[2] == '0':
        print(f'I={int(j)} J={int(1+j)}')
        print(f'I={int(j)} J={int(2+j)}')
        print(f'I={int(j)} J={int(3+j)}')
    else:
        print(f'I={j:.1f} J={1+j:.1f}')
        print(f'I={j:.1f} J={2+j:.1f}')
        print(f'I={j:.1f} J={3+j:.1f}')
    i += 1
