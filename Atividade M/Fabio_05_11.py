def main():

	n = int(input("Qual o tamanho da matriz? \n"))

	matriz = [0] * n

	for i in range(n):
		matriz[i] = [0] * n
		for j in range(n):
			matriz[i][j] = int(input("Dê um valor para os elementos da matriz.\n"))

	print("Matriz: ", matriz)

	for x in range(len(matriz)):
		coluna = []
		for y in range(len(matriz)):
			for z in range(len(matriz[y])):
				if z == x:
					coluna.append(matriz[y][z])
		matriz[x] = coluna

	print('Matriz transposta: ', matriz)
	


		



if __name__ == '__main__':
	main()