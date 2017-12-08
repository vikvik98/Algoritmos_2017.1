def main():
# Letra A
	matriz_a = [0] * 2
	for i in range(len(matriz_a)):
		matriz_a[i] = [0] * 4

	cont = 3
	for i in range(len(matriz_a)):
		for j in range(len(matriz_a[i])):
			matriz_a[i][j] = cont
			cont += 3
	print(matriz_a)


# Letra B
	matriz_b = [0] * 3
	for i in range(len(matriz_b)):
		matriz_b[i] = [0] * 4

	cont = 1
	for i in range(len(matriz_b)):
		for j in range(len(matriz_b[i])):
			matriz_b[i][j] = cont
			cont += 2
	print(matriz_b)

# Letra C
	matriz_c = []
	




if __name__ == '__main__':
	main()