def main():

	temperaturas = [0] * 121
	menor = 0
	maior = 0
	media = 0
	cont = 0
	total_temp = 0
	dias = 0

	#Geração de vetor
	for i in range(len(temperaturas)):
		temperatura_dia = float(input())
		temperaturas[i] = temperatura_dia

	#Search
	for i in range(len(temperaturas)):
		menor = temperaturas[0]
		if temperaturas[i] < menor:
			menor = temperaturas[i]
	print("A menor temperatura neste periodo foi de %.2f graus" % menor)

	for i in range(len(temperaturas)):
		maior = temperaturas[0]
		if temperaturas[i] < maior:
			maior = temperaturas[i]
	print("A maior temperatura neste periodo foi de %.2f graus" % menor)

	#Reduce
	for i in range(len(temperaturas)):
		total_temp += temperaturas[i]
		cont += 1
	media = total_temp / cont
	print("A media das temperaturas é de %.2f" % media)

	for i in range(len(temperaturas)):
		if temperaturas[i] < media:
			dias += 1
	print("Em %d dias a temperatura foi abaixo da media." % dias)



if __name__ == '__main__':
	main()