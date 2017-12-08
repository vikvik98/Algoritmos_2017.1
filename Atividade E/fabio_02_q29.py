from math import sqrt

def main():
	
	n = int(input('Digite um numero de 4 digitos '))

	dezena1 = n//100
	dezena2 = n%100
	
	if sqrt(n)==(dezena1+dezena2):
		print('Quadrado perfeito')

	else:
		print('Qadrado imperfeito')


if __name__=='__main__':
	main()