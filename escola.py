import os
import platform

def main():
	#banco de dados
	alunos = []

	while True:
		apagar_tela()
		opcao = int(input(menu()))

		if opcao == 1:
			apagar_tela()
			novo_aluno(alunos)
		elif opcao == 2:
			apagar_tela()
			listar_alunos(alunos)
		elif opcao == 0:
			print('Bye..')
			break
		else:
			apagar_tela()
			print('Opcao invalida!')

		input('\nDê um "enter"')
		apagar_tela()


def novo_aluno(alunos):
	print('Novo Aluno...\n')
	aluno = {}
	aluno['nome'] = input('Nome do aluno: ')
	aluno['curso'] = input('Curso: ')
	aluno['matricula'] = int(input('Matricula: '))
	alunos.append(aluno)


def listar_alunos(alunos):
	print('Lista de alunos')
	for i in alunos:	
		print(i)

def apagar_tela():
	so = platform.system()
	if so == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

def menu():
	return '\n ***** SysAlunos ***** \n1 - Novo Aluno \n2 - Listar Alunos \n0 - Sair\n\nEscolha: '

if __name__ == '__main__':
	main()