def main():

	n = int(input("Digite o tamanho da matriz quadrada.\n"))

	matriz = [0] * n

	for i in range(n):
		matriz[i] = [0] * n
		for j in range(n):
			matriz[i][j] = int(input("Digite os elementos da matriz.\n"))

	somas = []

	soma = 0

	for i in range(len(matriz)):
		soma = sum(matriz[i])
		somas.append(soma)

	maior = 0
	menor = 0
	pos_maior = 0
	pos_menor = 0

	for i in range(len(somas)):
		maior = somas[0]
		if somas[i] > maior:
			maior = somas[i]
			pos_maior = i

	for i in range(len(somas)):
		menor = somas[0]
		if somas[i] < menor:
			menor = somas[i]
			pos_menor = i


	print(matriz)
	print("A linha %d contem a soma maior que é igual a: %d" % (pos_maior,maior))
	print("A linha %d contem a soma menor que é igual a: %d" % (pos_menor,menor))


if __name__ == '__main__':
	main()