def main():

	n = int(input("Digite o tamanho da matriz quadrada.\n"))

	matriz = [0] * n

	for i in range(n):
		matriz[i] = [0] * n
		for j in range(n):
			matriz[i][j] = int(input("Digite os elementos da matriz.\n"))

	soma_pos = 0
	soma_neg = 0

	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] < 0:
				soma_neg += matriz[i][j]
			else:
				soma_pos += matriz[i][j]

	print("A soma dos positivos é: %d" % soma_pos)
	print("A soma dos negativos é: %d" % soma_neg)
	


if __name__ == '__main__':
	main()