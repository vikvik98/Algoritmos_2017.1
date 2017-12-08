import os, platform

def main():
	alunos = []

	inicializar(alunos)

	while True:	
		apagar_tela()
		
		opcao = int(input(menu()))
		if opcao == 1:
			apagar_tela()
			criar_aluno(alunos)
		if opcao == 2:
			apagar_tela()
			listar_alunos(alunos)
		if opcao == 3:
			apagar_tela()
			remover_pela_matricula(alunos)
		if opcao == 0:
			salvar(alunos)
			apagar_tela()
			print('BYE...')
			break		
		input('\nContinuar...')


def inicializar(alunos):
	arquivo = open("cadastrodealunos.txt", "a+")
	arquivo.seek(0)

	for linha in arquivo:
		linha.strip()
		aluno = {}
		aluno["nome"] = linha.split("-")[0]
		aluno["matricula"] = int(linha.split("-")[1])
		aluno["curso"] = linha.split("-")[2]

		alunos.append(aluno)


def salvar(alunos):
	arquivo = open('cadastrodealunos.txt', 'w')
	for i in alunos:
		linha = i['nome'] + '-' + str(i['matricula']) + '-' + i['curso'] + '\n'
		arquivo.write(linha)

	arquivo.close()

def remover_pela_matricula(alunos):
	matricula = int(input('digite a matricula: '))
	for i in range(len(alunos)):
		if alunos[i]['matricula'] == matricula:
			del alunos[i]
			break
		
  
def listar_alunos(alunos):
	for aluno in alunos:
		print(aluno)


def criar_aluno(alunos):
	aluno = {}
	print('1 - NOVO ALUNO\n')
	aluno['nome'] = input('Digite o nome: ')
	aluno['matricula'] = int(input('Digite a matricula: '))
	aluno['curso'] = input('Digite o curso: ')

	alunos.append(aluno)


def apagar_tela():
	plataforma = platform.system()
	if plataforma == 'Windows':
		os.system('cls')
	else:
		os.system('clear')	


def menu():
	return '\n ***** SysAlunos ***** \n\
1 - Novo Aluno \n\
2 - Listar Alunos \n\
3 - Remover pela matricula\n\
4 - Buscar pela matricula\n\
5 - Buscar pelo nome\n\
6 - Editar Aluno\n\
0 - Sair\n\nEscolha: '


if __name__ == '__main__':
	main()