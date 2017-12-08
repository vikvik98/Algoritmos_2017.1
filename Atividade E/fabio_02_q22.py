def main():

	num = float(input('Numero: '))

	parte_decimal = num - int(num)
	parte_int = int(num)


	if parte_decimal>=0.5:
		parte_int += 1


	print(parte_int)



if __name__ == '__main__':
	main()