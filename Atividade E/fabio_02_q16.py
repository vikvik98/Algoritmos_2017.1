def main():

	nota1 = float(input('Primeira nota: '))
	nota2 = float(input('Segunda nota: '))

	media = (nota1+nota2) / 2

	if media<7:
		exame = float(input('Nota do exame final:'))

		media2 = (media+exame) / 2

		if media2>=5:
			print('Aprovado')
		else:
			print('Reprovado')

	else:
		print('Aprovado')


if __name__ == '__main__':
	main()