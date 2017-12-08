def main():

	Entrada = input()
	Valor = Entrada.split()

	A = float(Valor[0])
	B = float(Valor[1])
	C = float(Valor[2])

	Triangulo = (A * C) / 2
	Circulo = 3.14159 * (C ** 2)
	Trapezio = (C * (A + B)) / 2
	Quadrado = B ** 2
	Retangulo = A * B

	print('TRIANGULO: %.3f' % Triangulo)
	print('CIRCULO: %.3f' % Circulo)
	print('TRAPEZIO: %.3f' % Trapezio)
	print('QUADRADO: %.3f' % Quadrado)
	print('RETANGULO: %.3f' % Retangulo)

if __name__ == '__main__':
	main()