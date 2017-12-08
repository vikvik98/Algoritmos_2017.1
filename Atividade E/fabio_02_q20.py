def main():
 
	angulo = int(input('Angulo de 0 a 360 graus: '))

	if angulo<91:
		print('Primeiro quadrante')

	elif 90<angulo<181:
		print('Segundo quandrante')

	elif 180<angulo<270:
		print('Terceiro quadrante')

	else:
		print('Quarto quandrante')


if __name__ == '__main__':
	main()