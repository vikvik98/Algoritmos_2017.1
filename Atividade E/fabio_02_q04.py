# Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente
def main():
	
	entrada = int(input())
	a = (entrada) // 10
	b = (entrada) % 10

	if a == b:
		print("%d é igual de %d" % (a, b))
	else:
		print("%d é diferente de %d" % (a, b))

		
if __name__ == '__main__':
	main()