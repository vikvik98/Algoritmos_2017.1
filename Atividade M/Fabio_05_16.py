def main():

	n = int(input("Digite o tamanho da matriz quadrada.\n"))

	matriz = [0] * n

	for i in range(n):
		matriz[i] = [0] * n
		for j in range(n):
			if j == i:
				matriz[i][j] = 1
			else:
				matriz[i][j] = 0

	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			print(matriz[i][j], end=' ')
		print()


if __name__ == '__main__':
	main()