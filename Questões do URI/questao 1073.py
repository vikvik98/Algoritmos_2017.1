def main():

	n = int(input())
	soma = 0
	for i in range(n+1):
		if i != 0 and i % 2 == 0:
			print("%d^2 = %d" % (i, (i**2)))



if __name__ == '__main__':
	main()
