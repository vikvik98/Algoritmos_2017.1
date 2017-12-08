# Leia 3 (três) números e escreva-os em ordem crescente.
def main():
	
	entrada = input()
	valor = entrada.split()
	a = float(valor[0])
	b = float(valor[1])
	c = float(valor[2])

	if a > b and a > c and b > c:
		print("A ordem crescente é: %.1f" % c, b, a)
	elif a < b and a > c and b > c:
		print("A ordem crescente é: %.1f" % c, a, b)
	elif a > b and a > c and b < c:
		print("A ordem crescente é: %.1f" % b, c, a)
	elif a > b and a < c and b < c:
		print("A ordem crescente é: %.1f" % b, a, c)
	elif a < b and a < c and b > c:
		print("A ordem crescente é: %.1f" % a, c, b)
	elif a < b and a < c and b < c:
		print("A ordem crescente é: %.1f" % a, b, c)

		
if __name__ == '__main__':
	main()