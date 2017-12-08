# Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o valor de num2 se opção for igual a 2; e o valor de num3 se opção for
# igual a 3. Os únicos valores possíveis para a variável opção são 1, 2 e 3.
def main():
	
	entrada = input()
	valor = entrada.split()
	opção = int(valor[0])
	n1 = int(valor[1])
	n2 = int(valor[2])
	n3 = int(valor[3])

	if opção == 1:
		print(n1)
	elif opção == 2:
		print(n2)
	elif opção == 3:
		print(n3)
	else:
		print("Opção não existente.")

if __name__ == '__main__':
	main()
