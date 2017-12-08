def main():

	n = int(input())
	lista = [0] * n
	lista2 = [0] * n 

	#Geração de vetor
	for i in range(n):
		x = int(input())
		lista[i] = x
	print(lista)
	
	#Map
	for i in range(n):
		lista2[i] = lista[i]
		if lista[i] % 2 == 0:
			lista2[i] = lista[i] / 2
	print(lista2)




if __name__ == '__main__':
	main()
