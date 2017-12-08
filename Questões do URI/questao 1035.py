def main():

	Entrada = input()
	Valor = Entrada.split()

	A = int(Valor[0])
	B = int(Valor[1])
	C = int(Valor[2])
	D = int(Valor[3])

	if B > C and D > A and (C + D) > (A + B) and C >= 0 and D >= 0 and A % 2 == 0:
		print('Valores nao aceitos')
	else:
		print('Valores aceitos')

if __name__ == '__main__':
	main()
