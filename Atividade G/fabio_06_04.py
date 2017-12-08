def main():
	frase = input()
	nova_frase = ""



	for i in frase:
		nova_frase += i + i
	print(nova_frase)

if __name__ == '__main__':
	main()