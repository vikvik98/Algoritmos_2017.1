def main():
	n = input()
	a = int(n.split()[0])
	b = int(n.split()[1])
	c = int(n.split()[2])
	d = int(n.split()[3])
	cont = 1

	l = []
	x = True

	for i in range(1,c-cont):
		if i % a == 0 and i % b != 0 and c % i == 0 and d % i != 0:
			l.append(i)
			x = False
		cont += 1

	resultado = min(l)

	if x:
		print("-1")
	else:
		print(resultado)



if __name__ == '__main__':
	main()