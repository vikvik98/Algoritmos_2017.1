# Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.
def main():
	
	entrada = input()
	valor = entrada.split()
	a = float(valor[0])
	b = float(valor[1])
	c = float(valor[2])

	if a == b and b == c:
		print("Os três numeros são iguais.")
	elif a == b or b == c or c == a:
		print("Existem dois numeros iguais.")
	else:
		print("Não existe numeros iguais")

if __name__ == '__main__':
	main()