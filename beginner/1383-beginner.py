n = int(input())
sudoku = False


def teste(vetor):
    for i in range(1, 10):
        if vetor.count(i) > 1:
            return False
    return True


for matrizes in range(n):
    # Cria a matriz
    matriz = []
    for _ in range(9):
        vetor = input().split()
        for ind, item in enumerate(vetor):
            vetor[ind] = int(item)
        matriz.append(vetor)

    for _ in range(1):
        # Teste das linhas
        for linha in range(9):
            if teste(matriz[linha]):
                sudoku = True
                continue
            sudoku = False
            break
        if not sudoku: break

        # Teste das colunas
        for lin in range(9):
            coluna = []
            for col in range(9):
                coluna.append(matriz[col][lin])
            if teste(coluna):
                sudoku = True
                continue
            sudoku = False
            break
        if not sudoku: break

        # Teste dos blocos
        for blo_y in range(0, 9, 3):
            for blo_x in range(0, 9, 3):
                bloco = []
                for lin in range(blo_y, blo_y+3):
                    for col in range(blo_x, blo_x+3):
                        bloco.append(matriz[lin][col])
                if teste(bloco):
                    sudoku = True
                    continue
                sudoku = False
                break
            if not sudoku: break
        if not sudoku: break

    print(f'Instancia {matrizes+1}')
    if sudoku: print('SIM\n')
    else: print('NAO\n')
