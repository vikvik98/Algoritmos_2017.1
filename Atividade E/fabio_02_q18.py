def main():
 
	valor1 = int(input('Valor 1: '))
	valor2 = int(input('Valor 2: '))
	operacao = int(input('Operacao a ser executada: \n1 – Adicao \n2 – Subtracao \n3 – Multiplicacao \n4 – Divisao\n'))

	if operacao==1:
		soma = valor2 + valor1
		print(soma)

	if operacao==2:
		Subtracao = valor1-valor2
		print(Subtracao)

	if operacao==3:
		multiplicacao = valor1*valor2
		print(multiplicacao)

	if operacao==4:
		divisao = valor1/valor2
		print(divisao)


if __name__ == '__main__':
	main()