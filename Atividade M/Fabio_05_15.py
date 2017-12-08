def main():
    n = int(input('digite a ordem da raiz: '))
    matriz = [0] * n
    for i in range(n):
        coluna = [0] * n
        for j in range(n):
            x = int(input('digite o valor da possição [%d][%d]: '%(i,j)))
            coluna[j] = x
        matriz[i] = coluna
    print(verificar_simetria(matriz))


def verificar_simetria(matriz):
    simetricidade = 'É simetrica'
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                simetricidade = 'Nao e simetrica'
            break
    return  simetricidade

if __name__ == '__main__':
    main()
