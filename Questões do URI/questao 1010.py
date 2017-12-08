
def main():

	Entrada = input()
	Entrada_2 = input()

	Valor = Entrada.split()
	Valor_2 = Entrada_2.split()

	A = int(Valor[0])
	B = int(Valor[1])
	C = float(Valor[2])
	D = int(Valor_2[0])
	E = int(Valor_2[1])
	F = float(Valor_2[2])

	Resultado = (B * C) + (E * F)
	print('VALOR A PAGAR: R$ %.2f' % Resultado)

if __name__ == '__main__':
	main()