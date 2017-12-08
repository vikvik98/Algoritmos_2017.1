# Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
def main():
	
	entrada = input()
	valor = entrada.split()
	a = float(valor[0])
	b = float(valor[1])
	c = float(valor[2])

	if a > b and b > c:
		print("%.1f é o maior numero entre os três" % a)
	elif b > a and a > c:
		print("%.1f é o maior numero entre os três" % b)
	else:
		print("%.1f é o maior numero entre os três" % c)
		
if __name__ == '__main__':
	main()