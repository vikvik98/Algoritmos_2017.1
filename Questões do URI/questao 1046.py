def main():

	n = input()
	a = int(n.split()[0])
	b = int(n.split()[1])


	if b <= a:
		b += 24
	resultado = b - a

	print("O JOGO DUROU %d HORA(S)" % resultado)


if __name__ == '__main__':
	main()
