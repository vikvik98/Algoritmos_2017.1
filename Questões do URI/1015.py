def main():

	z = input()
	z2 = input()
	x1 = float(z.split()[0])
	y1 = float(z.split()[1])
	x2 = float(z2.split()[0])
	y2 = float(z2.split()[1])
	

	print("%.4f" % distancia(x1,x2,y1,y2))

def distancia(x1,x2,y1,y2):
	resultado = ((((x2-x1)**2) + ((y2-y1)**2))**0.5)
	return resultado


if __name__ == '__main__':
	main()