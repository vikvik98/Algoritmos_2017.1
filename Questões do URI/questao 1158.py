def main():

	n = int(input())
	impares = []

	for i in range(n):
		z = input().split()
		x = int(z[0])
		y = int(z[1])

		for j in range(y):
			if x % 2 == 0:
				x = x+1
			if x % 2 != 0:
				impares.append(x)
				x += 2

		soma = sum(impares)
		print(soma)
		impares = []

if __name__ == '__main__':
	main()