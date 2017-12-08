def main():

	valor1 = int(input('Valor 1: '))
	valor2 = int(input('Valor 2: '))

	if valor1%valor2==1:
		soma = valor2 + valor1 + valor1%valor2
		print(soma)

	elif valor1%valor2==2:
		if valor1%2==0:
			print('Valor 1 é par')
		else:
			print('Valor 1 é impar')

		if valor2%2==0:
			print('Valor 2 é par')
		else:
			print('Valor 2 é impar')

	elif valor1%valor2==3:
		multiplicacao = (valor1+valor2) * valor1
		print(multiplicacao)

	elif valor1%valor2==4 and valor2!=0:
		divisao = (valor1+valor2) / valor2
		print(divisao)

	else:
		quadrado1 = valor1**2
		quadrado2 = valor2**2
		print('Quadrado do valor 1 é %d; quadrado do valor 2 é %d' % (quadrado1, quadrado2))


if __name__ == '__main__':
	main()