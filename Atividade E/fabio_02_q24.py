from math import sqrt

def main():
	
	n1 = input('Coeficientes (A, B e C): ')

	A = int(n1.split()[0])
	B = int(n1.split()[1])
	C = int(n1.split()[2])

	delt = (B**2) - (4*A*C)
	
	if A==0:
		print('Coeficientes invalidos')

	else:
		if delt<0:
			print('Sem rais pertencente aos Reais')

		else:
			X1 = (-B + sqrt(delt)) / 2*A
			X2 = (-B - sqrt(delt)) / 2*A

			print("X' = %.1f\nX'' = %.1f" % (X1, X2))


if __name__=='__main__':
	main()