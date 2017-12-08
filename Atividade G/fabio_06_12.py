
def main():
	nome = input("Nome completo: ")
	novo_nome = ""
	espace = 0

	for i in range(len(nome)):
		if nome[i]==" ":
			if espace==False:
				espace = i
			novo_nome = ""
			continue

		novo_nome += nome[i]

	novo_nome += "/"+nome[:espace]


	print("Nome de passageiro >>", novo_nome)


if __name__ == '__main__':
	main()