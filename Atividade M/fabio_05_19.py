'''
19. Escreva a seguinte matriz:  
1 1 1 1 1 1 
1 2 2 2 2 1 
1 2 3 3 2 1
1 2 3 3 2 1
1 2 2 2 2 1
1 1 1 1 1 1 
'''
def main():
	N = 6

	Matriz = criar_matriz_vazia(N, N)

	for i in range(N):
		for j in range(N):
			valores_possiveis = [i+1, j+1, N-j, N-i]
			menor = menor_valor(valores_possiveis)
			Matriz[i][j] = menor

	escrever_matriz(Matriz)


def menor_valor(vetor):
	menor = vetor[0]
	for valor in vetor:
		if menor > valor:
			menor = valor
	return menor


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
				print("%d" % matriz[i][j])
			else:
				print("%d " % matriz[i][j], end = "")


if __name__ == '__main__':
    main()