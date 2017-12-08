def main():

	lista = [0] * 100
	c = 100

	for i in range(len(lista)):
		lista[i] = c
		c -= 1
	print(lista)


if __name__ == '__main__':
	main()
