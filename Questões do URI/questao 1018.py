def main():

	N = int(input())

	A = (N // 100)
	B = ((N % 100) // 50)
	C = (((N % 100) % 50) // 20)
	D = ((((N % 100) % 50) % 20) // 10)
	E = (((((N % 100) % 50) % 20) % 10) // 5)
	F = ((((((N % 100) % 50) % 20) % 10) % 5) // 2)
	G = (((((((N % 100) % 50) % 20) % 10) % 5) % 2) // 1)

	print ('%d' % N)
	print ('%.d nota(s) de R$ 100.00' % A)
	print ('%d nota(s) de R$ 50.00' % B)
	print ('%d nota(s) de R$ 20.00' % C)
	print ('%d nota(s) de R$ 10.00' % D)
	print ('%d nota(s) de R$ 5.00' % E)
	print ('%d nota(s) de R$ 2.00' % F)
	print ('%d nota(s) de R$ 1.00' % G)


if __name__ == '__main__':
    main()
