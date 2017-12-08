def main():

	x = [0] * 10

	for i in range(len(x)):
		n = int(input())
		if n <= 0:
			n = 1
			x[i] = n
			print("X[%d] = %d" % (i,n))
		else:
			x[i] = n
			print("X[%d] = %d" % (i,n))


if __name__ == '__main__':
	main()