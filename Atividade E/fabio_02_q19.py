def main():
 
	altura = float(input('Digite sua altura em metros '))
	massa = float(input('Digite seu peso em kg '))
	
	IMC = massa / altura**2

	if IMC<=25:
		print('Peso normal')

	elif 25<IMC<=30:
		print('Obeso')

	else:
		print('Obesidade morbida')


if __name__ == '__main__':
	main()