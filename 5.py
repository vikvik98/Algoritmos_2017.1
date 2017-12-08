import os, platform
def main():
	apartamentos = []
	while True:
		limpar_tela()
		opção = int(input(menu()))
		if opção == 0:
			limpar_tela()
			print("Até outra hora.")
			break
		if opção == 1:
			limpar_tela()
			novo_apartamento(apartamentos)
		if opção == 2:
			limpar_tela()
			listar_apartamentos(apartamentos)
		if opção == 3:
			limpar_tela()
			filtrar_apartamento(apartamentos)
		if opção == 4:
			limpar_tela()
			ordenar_apartamento(apartamentos)
		input("Dê um enter...")


def ordenar_apartamento(apartamentos):
	z = input("Digite o item que você deseja ver ordenado:\n")
	print(sorted(apartamentos, key=lambda x:x[z]), "\n")


def filtrar_apartamento(apartamentos):
	x = input("Digite o item que você deseja filtrar:\n")
	for i in range(len(apartamentos)):
		print("Apartamento %d" % (i+1))
		print(apartamentos[i][x])


def listar_apartamentos(apartamentos):
	for i in range(len(apartamentos)):
		print("Apartamento %d" % (i+1))
		print("Área %f" % apartamentos[i]['area'])
		print("Quarto(s) %d" % apartamentos[i]['quarto'])
		print("Suite(s) %d" % apartamentos[i]['suite'])
		print("Valor = %f \n" % apartamentos[i]['valor'])


def novo_apartamento(apartamentos):
	apartamento = {}
	print("Novo apartamento.")
	apartamento['area'] = float(input("Digite a área do apartamento:\n"))
	apartamento['quarto'] = int(input("Digite quantos quartos tem o apartamento:\n"))
	apartamento['suite'] = int(input("Digite a quantidade de suites no apartamento:\n"))
	apartamento['valor'] = float(input("Digite o valor do apartamento:\n"))
	apartamentos.append(apartamento)
	print("Apartamento cadastrado com sucesso...")


def limpar_tela():
	SO = platform.system()
	if SO == "Windows":
		os.system("cls")
	else:
		os.system("clear")


def menu():
	return ('_____Cadastro______\n\
1)Novo Apartamento\n\
2)Listar Apartamento\n\
3)Filtrar Apartamento\n\
4)Ordenar Apartamento\n\
0)Sair\n\
Opção:')


if __name__ == '__main__':
	main()