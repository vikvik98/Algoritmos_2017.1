def main():
	from math import sqrt

	Entrada = input()
	p1 = Entrada.split()
	Entrada_2 = input()
	p2 = Entrada_2.split()

	x1 = float(p1[0])
	y1 = float(p1[1])
	x2 = float(p2[0])
	y2 = float(p2[1])

	Resultado = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

	print('%.4f' % Resultado)

if __name__ == '__main__':
	main()
