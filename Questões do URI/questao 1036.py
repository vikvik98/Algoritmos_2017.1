def main():
	
	Entrada = input()
	Valor = Entrada.split()
	a = float(Valor[0])
	b = float(Valor[1])
	c = float(Valor[2])

	d = b ** 2 - (4 * a * c)
	e = 0.0
	if d <= e or a == e:
		print("Impossivel calcular")
	else:
		r = d ** (1/2)
		x1 = ((b *(-1)) - r) / (2 * a)
		x2 = ((b *(-1)) + r) / (2 * a)
		print('R1 = %.5f' % x2)
		print('R2 = %.5f' % x1)

if __name__ == '__main__':
	main()
