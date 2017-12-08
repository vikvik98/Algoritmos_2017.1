def main():
	frase = input()
	nova_frase = ""

	for palavra in frase.split():
		nova_frase += palavra
		print(nova_frase)

if __name__ == '__main__':
	main()