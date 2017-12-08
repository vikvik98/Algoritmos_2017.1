import os, platform
def main():

	jogadores = []
	ler_arquivo(jogadores)
	limpar_tela()
	while True:
		opção = int(input(menu()))
		if opção == 0:
			saida_arquivo(jogadores)
			print("Até uma outra hora.")
			break
		if opção == 1:
			limpar_tela()
			cadastrar_jogador(jogadores)
		if opção == 2:
			limpar_tela()
			listar_jogadores(jogadores)
		if opção == 3:
			limpar_tela()
			alterar_cadastro(jogadores)
		input("Dê um 'enter'.")
		limpar_tela()


def saida_arquivo(jogadores):
	arquivo = open('jogadores.txt', 'w')
	for i in jogadores:
		linha = i['nome'] + '-' + i['raça'] + '-' + i['classe'] + '\n'
		arquivo.write(linha)
	arquivo.close()


def ler_arquivo(jogadores):
	arquivo = open('jogadores.txt', 'a+')
	arquivo.seek(0)
	for linha in arquivo:
		jogador = {}
		linha = linha.strip().split("-")
		jogador['nome'] = linha[0]
		jogador['raça'] = linha[1]
		jogador['classe'] = linha[2]
		jogadores.append(jogador)


def alterar_cadastro(jogadores):
	x = input("Digite o que você deseja alterar no personagem:\n")
	if x == 'nome':
		x = input("Digite o nome do personagem que você quer alterar o nome:\n")
		for i in range(len(jogadores)):
			if x == jogadores[i]['nome']:
				jogadores[i]['nome'] = input("Digite o novo nome do personagem:\n")
	if x == 'raça':
		x = input("Digite o nome do personagem que você quer alterar a raça:\n")
		for i in range(len(jogadores)):
			if x == jogadores[i]['nome']:
				jogadores[i]['raça'] = input("Digite a nova raça do personagem:\n")
	if x == 'classe':
		x = input("Digite o nome do personagem que você quer alterar a classe:\n")
		for i in range(len(jogadores)):
			if x == jogadores[i]['nome']:
				jogadores[i]['classe'] = input("Digite a nova classe do personagem:\n")
	else:
		print("Você digitou uma opção invalida.")


def listar_jogadores(jogadores):
	for i in range(len(jogadores)):
		print("Personagem %d" % (i+1))
		print("Nome: %s" % jogadores[i]['nome'])
		print("Raça: %s" % jogadores[i]['raça'])
		print("Classe: %s" % jogadores[i]['classe'])
		print("\n")


def cadastrar_jogador(jogadores):
	jogador = {}
	print("Cadastre um novo personagem\n")
	jogador['nome'] = input("Nome do personagem:\n")
	jogador['raça'] = input("Raça do personagem:\n")
	jogador['classe'] = input("Classe do personagem:\n")
	print("Cadastro realizado com sucesso!")
	jogadores.append(jogador)


def limpar_tela():
	SO = platform.system()
	if SO == 'Windows':
		os.system('cls')
	else:
		os.system('clear')


def menu():
	return ('___________CADASTRO____________\n\
1) Cadastrar jogador.\n\
2) Listar jogadores.\n\
3) Alterar cadastro do jogador.\n\
0) Sair do cadastro\n\
Digite a opção aqui:')



if __name__ == '__main__':
	main()