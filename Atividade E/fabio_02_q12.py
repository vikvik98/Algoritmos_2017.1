# Leia 1 (um) número inteiro e escreva se este número é par ou impar.
def main():
	
	numero = int(input())

	if numero % 2 == 0:
		print("%d É par." % numero)
	else:
		print("%d É impar" % numero)
	

if __name__ == '__main__':
	main()
