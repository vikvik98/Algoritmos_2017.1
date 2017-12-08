x = int(input("Digite a quantidade de linhas da matriz:\n"))
y = int(input("Digite a quantidade de colunas da matriz:\n"))


def geramatriz(x,y):
    matriz = [0] * x
    for i in range(len(matriz)):
        matriz[i] = [0] * y
    return matriz

matriz = geramatriz(x,y)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input("Digite o valor do elemento da linha %d coluna %d:\n" % (i,j)))

print(matriz)        


