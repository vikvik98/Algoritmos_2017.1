def main():

	n = int(input("Qual o tamanho da matriz? \n"))

	matriz = [0] * n

	for i in range(n):
		matriz[i] = [0] * n
		for j in range(n):
			matriz[i][j] = int(input("Dê um valor para os elementos da matriz.\n"))

	print("Matriz: ", matriz)

	menor = matriz[0][0]
	maior = matriz[0][0]
	pos_maior_linha = 0
	pos_maior_coluna = 0
	pos_menor_linha = 0
	pos_menor_coluna = 0

	for i in range(len(matriz)):
		for j in range(len(matriz[i])):			
			if matriz[i][j] < menor:
				menor = matriz[i][j]
				pos_menor_linha = i
				pos_menor_coluna = j


	for i in range(len(matriz)):
		for j in range(len(matriz[i])):			
			if matriz[i][j] > maior:
				maior = matriz[i][j]
				pos_maior_linha = i
				pos_maior_coluna = j

	print("O maior elemento da matriz é: %d e esta na linha:%d coluna:%d" % (maior, pos_maior_linha, pos_maior_coluna))
	print("O menor elemento da matriz é: %d e esta na linha:%d coluna:%d" % (menor, pos_menor_linha, pos_menor_coluna))


if __name__ == '__main__':
	main()