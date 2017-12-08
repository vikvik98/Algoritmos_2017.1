def main():
	Entrada = input()
	Valor = Entrada.split()

	A = int(Valor[0])
	B = int(Valor[1])
	C = int(Valor[2])

	Maior = (A + B + abs(A - B)) / 2
	Resultado = (Maior + C + abs(Maior - C)) / 2
	print ('%d eh o maior' % Resultado)

if __name__ == '__main__':
    main()