# Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
# se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
# verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
# obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau). 
def main():
	
	entrada = input()
	valor = entrada.split()
	a = float(valor[0])
	b = float(valor[1])
	c = float(valor[2])

	if a + b + c == 180:
		if a == 0 or b == 0 or c == 0:
			print("Não existe triângulo com um ângulo igual a 0")
		elif a < 90 and b < 90 and c < 90:
			print("Esse triângulo é um triângulo acutângulo.")
		elif a == 90 or b == 90 or c == 90:
			print("Esse triângulo é um triângulo retângulo.")
		elif a > 90 or b > 90 or c > 90:
			print("Esse triângulo é um triângulo obtusângulo.")
	else:
		print("Não é um triângulo.")

		
if __name__ == '__main__':
	main()
