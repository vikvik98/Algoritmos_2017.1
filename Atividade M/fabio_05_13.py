#13. Leia uma matriz quadrada de ordem N, calcule e escreva seu determinante. 

def main():
	N = int(input("Ordem da matriz: "))

	matriz = criar_matriz(N, N)
	print("Matriz dada:")
	escrever_matriz(matriz)

	determinante = calcular_determinante(matriz)
	print("\nDeterminante da matriz:", determinante)


def calcular_determinante(matriz):
	N = len(matriz)
	determinante = 0

	if N == 1:
		return matriz[0][0]

	else:
		determinante = 0
		for i in range(N):
			determinante += matriz[i][0] * calcular_complemento_algebrico(matriz, i, 0)
		return determinante


def calcular_complemento_algebrico(matriz, linha, coluna):
	complemento_algebrico = (-1)**(linha + coluna)
	complemento_algebrico *= calcular_menor_complementar(matriz, linha, coluna)
	return complemento_algebrico

def calcular_menor_complementar(matriz, linha, coluna):
	N = len(matriz)
	matriz_suprimida = suprimir_linha_coluna(matriz, linha, coluna)
	menor_complementar = calcular_determinante(matriz_suprimida)
	return menor_complementar


def suprimir_linha_coluna(matriz, linha, coluna):
	N = len(matriz)
	nova_matriz = espelhar_matriz(matriz)
	del nova_matriz[linha]
	for i in range(N-1):
		for j in range(N):
			if j == coluna:
				del nova_matriz[i][j]
	return nova_matriz

def espelhar_matriz(matriz):
	linha = len(matriz)
	coluna = len(matriz[0])
	matriz_espelho = criar_matriz_vazia(linha, coluna)
	for i in range(linha):
		for j in range(coluna):
			matriz_espelho[i][j] = matriz [i][j]
	return matriz_espelho


def criar_matriz(linhas, colunas):
	matriz = criar_matriz_vazia(linhas, colunas)
	for j in range(colunas):
		for i in range(linhas):			
			texto = "Elemento (%d, %d): " % (i, j)			
			elemento = int(input(texto))
			matriz[i][j] = elemento
	return matriz

def criar_matriz_vazia(linhas, colunas):
	matriz_vazia = [0]*linhas
	for i in range(linhas):
		linha = [0]*colunas
		matriz_vazia[i] = linha
	return matriz_vazia


def escrever_matriz(matriz):
	linhas = len(matriz)
	colunas = len(matriz[0])
	for i in range(linhas):
		print("%10s" % " ", end="")
		for j in range(colunas):
			if j == colunas -1:
				print(matriz[i][j])
			else:
				print(matriz[i][j], end=" ")


if __name__ == '__main__':
	main()