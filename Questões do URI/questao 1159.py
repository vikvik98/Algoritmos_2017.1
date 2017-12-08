def main():

	while True:
		x = int(input())
		if x == 0:
			break
		pares = []

		
		for i in range(x,x+5):
			if x % 2 != 0:
				x = x+1
			if x % 2 == 0:
				pares.append(x)
				x += 2

		soma = sum(pares)
		print(soma)
		pares = []


if __name__ == '__main__':
	main()