def main():
	z = 0
	for i in range(5):
		n = int(input())
		if n % 2 == 0:
			z += 1
	print("%d valores pares" % z)


if __name__ == '__main__':
	main()
