# Escreva uma sub-rotina de nome diagonal, que escreva um texto de até 20 caracteres na diagonal. Ex.: diagonal ('Algoritmos '); escreverá 'Algoritmos' na diagonal.

def main():
	
	nome = input('Digite um nome: ')
	diagonal(nome)

def diagonal(nome):
	cont = 0
	for letra in nome:
		print(' ' * cont,letra)
		cont += 1

if __name__ == '__main__':
	main()