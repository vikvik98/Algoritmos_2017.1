# Leia uma frase e faça a criptografia, retirando as vogais das palavras.  O programa deverá armazenar estas vogais e suas posições originais, mostrar a frase criptografada, em seguida, descriptografar a frase e mostrá-la na tela.

def main():

	# entrada
	frase = input('Frase: ')
	# da a frase sem consoante (criptografada)
	frase_consoante = retirar(frase)
	print('Essa é a frase criptografada: ',frase_consoante)

# retira a vogal
def retirar(frase):
	nova_frase = ''
	retiradas = ''
	pos = 0
	descrip = ''
	for letra in frase:
		if vogal(letra):
			nova_frase += ''
			# salva a letra na sua posição.
			descrip += letra[pos:pos+1]
		else:
			nova_frase += letra
			# salva qualquer letra q já ta criptografada.
			descrip += letra[pos:pos+1]
	# resultados
	print('Essa é a frase descriptografada:',descrip)
	return (nova_frase)
	

def vogal(letra):
	#ver se é vogal
	vogal = 'AEIOUaeiou'
	return letra in vogal


if __name__ == '__main__':
	main()