def main():
    n = int(input('digite a ordem da raiz: '))
    matriz = [0] * n
    for i in range(n):
        coluna = [0] * n
        for j in range(n):
            x = int(input('digite o valor da possição [%d][%d]: '%(i,j)))
            coluna[j] = x
        matriz[i] = coluna
    diagonal_principal = soma_de_valores(matriz)[0]
    diagonal_secundario = soma_de_valores(matriz)[1]
    outros_valores = soma_de_valores(matriz)[2]
    print(matriz)
    print('A soma dos valores da diagonal principal eh %d'%diagonal_principal)
    print('A soma da diagonal secundaria eh %d'%diagonal_secundario)
    print('a soma dos elementos que nao estao nas diagonais eh %d'%outros_valores)

def soma_de_valores(matriz):
    diagonal_principal = 0
    diagonal_secundario = 0
    outros_valores = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                diagonal_principal += matriz[i][j]
            if i == len(matriz)-j-1:
                diagonal_secundario += matriz[i][j]
            if i != j and i != len(matriz)-j-1:
                outros_valores += matriz[i][j]
    return diagonal_principal , diagonal_secundario,outros_valores


if __name__ == '__main__':
    main()
