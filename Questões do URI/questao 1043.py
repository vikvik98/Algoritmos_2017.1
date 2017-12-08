def main():
	
	n = input()
	a = float(n.split()[0])
	b = float(n.split()[1])
	c = float(n.split()[2])
	perimetro = (a + b + c)
	area = (a + b) * c / 2
	if (a < (b + c)) and (b < (a + c)) and (c < (b + a)):
		print("Perimetro = %.1f" % perimetro)
	else:
		print("Area = %.1f" % area)

if __name__ == '__main__':
	main()
