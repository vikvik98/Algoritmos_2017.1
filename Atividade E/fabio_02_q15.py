def main():
 
	horas_prof1 = int(input('Horas aulas professor 1: '))
	valor_prof1 = float(input('Valor por hora: '))
	horas_prof2 = int(input('Horas aulas professor 2: '))
	valor_prof2 = float(input('Valor por hora: '))

	salario_prof1 = valor_prof1*horas_prof1
	salario_prof2 = valor_prof2*horas_prof2

	if salario_prof1 == salario_prof2:
		print('Salarios iguais')
	elif salario_prof1>salario_prof2:
		print('O primeiro ganha mais')

	else:
		print('O segundo ganha mais')


if __name__ == '__main__':
	main()