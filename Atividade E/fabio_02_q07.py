# Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
# (três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
# formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
# escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).
def main():
	
	entrada = input()
	valor = entrada.split()
	a = float(valor[0])
	b = float(valor[1])
	c = float(valor[2])

	if a + b >= c:
		if a == 0 or b == 0 or c == 0:
			print("Não existe triângulo com um ângulo igual a 0")
		elif a == b and a == c and b == c:
			print("Esse triângulo é um triângulo equilátero.")
		elif a == b or a == c or b == c:
			print("Esse triângulo é um triângulo isósceles.")
		elif a != b and a != c and b != c:
			print("Esse triângulo é um triângulo escaleno.")
	else:
		print("Não é um triângulo.")

		
if __name__ == '__main__':
	main()
