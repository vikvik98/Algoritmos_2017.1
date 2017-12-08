def main():

	# Geração de vetor
	frase = input()
	caracteres = list(frase)
	carac_branco = 0
	carac_A = 0

	# Map
	for i in range(len(caracteres)):
		if caracteres[i] == " ":
			carac_branco += 1
	print("Existem %d caracteres em branco na frase." % carac_branco)

	for i in range(len(caracteres)):
		if caracteres[i] == "A" or caracteres[i] == "a":
			carac_A += 1
	print("Existem %d caracteres da letra a na frase." % carac_A)

if __name__ == '__main__':
	main()