def main():
	n = input()
	a = int(n.split()[0])
	b = int(n.split()[1])
	c = int(n.split()[2])
	d = int(n.split()[3])
	cont = 1

	l = [i for i in range(1,c+1) if i % a == 0 and i % b != 0 and c % i == 0 and d % i != 0]
	resultado = min(l)

	print(resultado)




if __name__ == '__main__':
	main()