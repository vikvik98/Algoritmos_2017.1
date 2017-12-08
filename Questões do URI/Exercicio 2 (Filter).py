def main():

	lista = [0] * 500
	c = 1
	s = 0
	x = 0

	#Geração de vetor
	for i in range(len(lista)):
		lista[i] = c
		c += 1
	print(lista)

	# Filter
	for i in range(len(lista)):
		if lista[i] % 5 == 0:
			s += 1

	lista2 = [0] * s

	for i in range(len(lista)):
		if lista[i] % 5 == 0:
			lista2[x] = lista[i]
			x += 1
	print(lista2)


if __name__ == '__main__':
	main()
