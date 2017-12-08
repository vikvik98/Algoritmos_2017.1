'''
20. Escreva a seguinte matriz:  
01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25 
'''
def main():
	N = 5

	Matriz = criar_matriz_vazia(N, N)

	for i in range(N):
		for j in range(N):
			Matriz[i][j] = (j+1) + N*i

	escrever_matriz(Matriz)


def criar_matriz_vazia(linhas, colunas):
	matriz_vazia = [0]*linhas
	for i in range(linhas):
		linha = [0]*colunas
		matriz_vazia[i] = linha
	return matriz_vazia


def escrever_matriz(matriz):
	N = len(matriz)
	for i in range(N):
		for j in range(N):
			if j==N-1:
				print("%.2d" % matriz[i][j])
			else:
				print("%.2d " % matriz[i][j], end = "")


if __name__ == '__main__':
    main()