def main():
	X = int(input("Digite o numero X:\n"))
	
	contaDigito = 0

	resultado =  X // 10
	if(resultado == 0):
		contaDigito = 1
	else:
		while resultado > 0:
			resultado = X // 10
			X = resultado
			contaDigito += 1

	print("total de %d digitos" % contaDigito)

if __name__ == '__main__':
	main()