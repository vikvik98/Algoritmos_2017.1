def main():
	
	n = input()
	a = float(n.split()[0])
	b = float(n.split()[1])
	c = float(n.split()[2])


	if a < c:
		a, c = c, a
	if a < b:
		a, b = b, a
	if b < c:
		b, c = c, b



	if a >= (b+c):
		print("NAO FORMA TRIANGULO")
	else:
		if (a**2) > (b**2) + (c**2):
			print("TRIANGULO OBTUSANGULO")
	if (a**2) == (b**2) + (c**2):
		print("TRIANGULO RETANGULO")	
	if a**2 < b**2 + c**2:
		print("TRIANGULO ACUTANGULO")
	if a == b and b == c:
		print("TRIANGULO EQUILATERO")
	if a == b and b != c or a == c and c != b or b == c and b != a:
		print("TRIANGULO ISOSCELES")


if __name__ == '__main__':
	main()
