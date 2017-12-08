def main():
	par = 0
	impar = 0
	posi = 0
	nega = 0

	for i in range(5):
		n = int(input())
		if n % 2 == 0:
			par += 1
		else:
			impar += 1
		if n > 0:
			posi += 1
		else:
			if n < 0:
				nega += 1

	print("%d valor(es) par(es)" % par)
	print("%d valor(es) impar(es)" % impar)
	print("%d valor(es) positivo(s)" % posi)
	print("%d valor(es) negativo(s)" % nega)



if __name__ == '__main__':
	main()
