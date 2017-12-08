def main():

	par = []
	impar = []
	par_total = 0
	impar_total = 0
	par_media = 0
	impar_media = 0
	par_maior = 0
	impar_menor = 0
	cont_par = 0
	cont_impar = 0

	# Geração de vetor
	while True:

		numeros = int(input())
		if numeros == 0:
			break
		else:
			if numeros % 2 == 0:
				par.append(numeros)
				cont_par += 1
			else:
				impar.append(numeros)
				cont_impar += 1
				
	# Reduce
	for i in range(len(par)):
		par_total += par[i]
	par_media = par_total / cont_par
	print("A media de numeros pares foi de %.2f" % par_media)

	for i in range(len(impar)):
		impar_total += impar[i]
	impar_media = impar_total / cont_impar
	print("A media de numeros impares foi de %.2f" % impar_media)

	# Search
	for i in range(len(par)):
		par_maior = par[0]
		if par[i] > par_maior:
			par_maior = par[i]
	print("O maior par digitado foi de valor %d" % par_maior)

	for i in range(len(impar)):
		impar_menor = impar[0]
		if impar[i] < impar_menor:
			impar_menor = impar[i]
	print("O menor impar digitado foi de valor %d" % impar_menor)

	# Filter
	print("Esses são os pares maiores que a media dos pares:", end="\n")
	for i in range(len(par)):
		if par[i] > par_media:
			print(par[i])

	print("Esses são os impares menores que a media dos impares:", end="\n")
	for i in range(len(impar)):
		if impar[i] < impar_media:
			print(impar[i])



if __name__ == '__main__':
	main()