# Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.
def main():
	
	entrada = int(input("Digite um numero de 0 a 100:"))

	if entrada == 2:
		print("%d É primo." % entrada)
	elif entrada % entrada == 0 and entrada % 2 != 0:
		print("%d É primo." % entrada)		
	else:
		print("%d Não é primo." % entrada)

		
if __name__ == '__main__':
	main()
