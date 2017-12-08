
def main():
	texto = input("Texto:\n")
	qtd_palavras = 1

	for i in texto:
		if i==" ":
			qtd_palavras += 1

	print("Esse texto contem %d palavras" % qtd_palavras)


if __name__ == '__main__':
	main()