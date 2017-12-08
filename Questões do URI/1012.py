def main():

	x = input()
	a = float(x.split()[0])
	b = float(x.split()[1])
	c = float(x.split()[2])
	

	print("TRIANGULO: %.3f" % area_triangulo(a,c))
	print("CIRCULO: %.3f" % area_circulo(c))
	print("TRAPEZIO: %.3f" % area_trapezio(a,b,c))
	print("QUADRADO: %.3f" % area_quadrado(b))
	print("RETANGULO: %.3f" % area_retangulo(a,b))


def area_triangulo(a,c):
	area = (a*c) / 2
	return area


def area_circulo(c):
	area = 3.14159 * (c**2)
	return area


def area_trapezio(a,b,c):
	area = ((a+b)*c)/2
	return area


def area_quadrado(b):
	area = b**2
	return area


def area_retangulo(a,b):
	area = a*b
	return area


if __name__ == '__main__':
	main()