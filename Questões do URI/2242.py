def main():

	n = input()
	palavra = ""

	for i in n:
		if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
			palavra += i

	if palavra == palavra[::-1]:
		print("S")
	else:
		print("N")


if __name__ == '__main__':
	main()