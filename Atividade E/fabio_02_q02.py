# Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.
def main():
	
	entrada = input()
	valor = entrada.split()
	a = float(valor[0])
	b = float(valor[1])

	if a == b:
		print("Os numeros são iguais")
	elif a < b:
		print("%.1f é menor que %.1f" % (a, b))
	else:
		print("%.1f é menor que %.1f" % (b, a))

if __name__ == '__main__':
	main()