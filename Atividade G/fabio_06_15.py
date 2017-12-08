# Escreva uma sub-rotina de nome vertical, que escreva um texto de até 20 caracteres na vertical. Ex.: vertical (10,'Algoritmos'); escreverá 'Algoritmos' na coluna 10

def main():

	nome = input('Digite um nome: ')
	vertical(nome)

def vertical(nome):
	for letra in nome:
		print(letra)

if __name__ == '__main__':
	main()