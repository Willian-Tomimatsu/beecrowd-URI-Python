def string_para_int(lista):
    for i, n in enumerate(lista): lista[i] = int(n)
    return lista


def baralho(quant_cartas, baralho):
    for i in range(quant_cartas):
        carta = input().split()
        baralho.append(string_para_int(carta))
    return baralho


def result(atributo, baralho_1, carta_1, nome_1, baralho_2, carta_2, nome_2):
    if baralho_1[carta_1][atributo] == baralho_2[carta_2][atributo]:
        print('Empate')
    elif baralho_2[carta_2][atributo] > baralho_1[carta_1][atributo]:
        print(f'{nome_2}')
    elif baralho_1[carta_1][atributo] > baralho_2[carta_2][atributo]:
        print(f'{nome_1}')


def main():
    n = int(input())
    m, l = input().split()
    m, l = int(m), int(l)
    baralho_m = []
    baralho_l = []

    baralho(m, baralho_m)
    baralho(l, baralho_l)

    c_m, c_l = input().split()
    c_m, c_l = int(c_m)-1, int(c_l)-1
    a = int(input())-1

    result(a, baralho_m, c_m, 'Marcos', baralho_l, c_l, 'Leonardo')


while True:
    try:
        main()
    except EOFError:
        break
