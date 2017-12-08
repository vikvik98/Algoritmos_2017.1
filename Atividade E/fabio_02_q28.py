def main():
	
	ponto1 = input('Ponto 1: ')
	ponto2 = input('Ponto 2: ')

	X1 = int(ponto1.split()[0])
	Y1 = int(ponto1.split()[1])
	X2 = int(ponto2.split()[0])
	Y2 = int(ponto2.split()[1])

	if X1==X2 or Y1==Y2:
		print('Coordenadas incorretas')

	else:
		if Y1<Y2 and X1<X2:
			altura = Y2 - Y1
			largura = X2 - X1

		elif Y1<Y2 and X1>X2:
			altura = Y2 - Y1
			largura = X1 - X2

		elif Y1>Y2 and X1<X2:
			altura = Y1 - Y2
			largura = X2 - X1
			area = altura*largura

		else:
			altura = Y1 - Y2
			largura = X1 - X2
			
		area = altura*largura

		print('Area do retangulo igual a', area)


if __name__=='__main__':
	main()