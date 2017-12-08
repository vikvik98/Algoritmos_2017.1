def main():

	p1 = input()
	p2 = input()
	x = int(p1.split()[0])
	y = int(p1.split()[1])
	z = float(p1.split()[2])
	x2 = int(p2.split()[0])
	y2 = int(p2.split()[1])
	z2 = float(p2.split()[2])

	print("VALOR A PAGAR: R$ %.2f" % peças(y,z,y2,z2))

def peças(y,z,y2,z2):
	resultado = (y*z) + (y2*z2)
	return resultado


if __name__ == '__main__':
	main()