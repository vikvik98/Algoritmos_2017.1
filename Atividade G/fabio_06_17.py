# Escreva uma sub-rotina de nome substr, que extraia uma sub-cadeia de uma string. Ex.: substr(texto, 10, 20), extrairá 20 caracteres de texto a partir do caractere na posição 10

def main():

	texto = input('Digite um texto: ')
	caracteres = int(input('Digite a quantidade de caracteres de texto: '))
	posicao = int(input('Digite a posição a começar a tirar: '))
	substr(texto,posicao,caracteres)

def substr(texto, posicao, caracteres):
	if posicao < len(texto) and caracteres <= len(texto):
		final = caracteres + posicao
		texto = texto[posicao+1:final]
		print(texto)
	else:
		print('Impossivel fazer ação.')



if __name__ == '__main__':
	main()