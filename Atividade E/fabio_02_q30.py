def main():
	
	n = int(input('Digite um numero de 1000 a 9999 \n'))

	dezena1 = n//100
	dezena2 = n%100
	
	if (dezena1+dezena2)**2 == n:
		print('Esse numero se encaixa a regra')

	else:
		print('Esse numero nao se encaixa a regra')


if __name__=='__main__':
	main()