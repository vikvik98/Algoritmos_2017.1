# Escreva uma sub-rotina que gere logins para usuários de um sistema de computação baseado na seguinte regra: o login é composto pelas letras iniciais do nome do usuário.

def main():

	nome = input('Digite seu nome: ')
	senha = gerar_login(nome)
	senha1 = input('Digite a senha: ')
	if senha == senha1:
		print('Senha correta!')
	else:
		print('Senha incorreta!')

def gerar_login(nome):
	senha = ''
	for palavra in nome.split():
		inicial = palavra[:1]
		senha += inicial
	return senha

if __name__ == '__main__':
	main()