def main():
	
	Entrada = input()
	Valor = Entrada.split()

	A = int(Valor[0])
	B = int(Valor[1])

	if A == 1:
		A == 4.00
	if B == 1:
		B == 4.00
	if A ==  2:
		A == 4.50
	if B == 2:
		B == 4.50
	if A == 3:
		A == 5.00
	if B == 3:
		B == 5.00
	if A == 4:
		A == 2.00
	if B == 4:
		B == 2.00
	if A == 5:
		A == 1.50
	if B == 5:
		B == 1.50

	Resultado = A + B

	print('Total: R$ %.2f' % Resultado)	

if __name__ == '__main__':
	main()
