
def main():
	nome = input("Nome completo: ")
	iniciais = nome[0]+'. '
	novo_nome = ""

	for i in range(len(nome)):
		if nome[i]==" " and nome[i+1].isupper():
			novo_nome = ""
			iniciais += nome[i+1]+". "
			continue

		novo_nome += nome[i]

	novo_nome += ", "+iniciais[:-4]


	print("Nome em formato de biografia >>", novo_nome)


if __name__ == '__main__':
	main()