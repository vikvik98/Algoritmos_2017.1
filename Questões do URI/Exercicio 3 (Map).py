def main():

	lista = [0] * 20
	c = 1
	
	#Geração de vetor
	for i in range(len(lista)):
		lista[i] = c
		c += 1
	print(lista)

	#Map
	for i in range(len(lista)):
		if lista[i] % 2 != 0:
			lista[i] = lista[i] * lista[i]
	print(lista)

	

if __name__ == '__main__':
	main()
