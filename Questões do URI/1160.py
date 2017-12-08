def main():

	t = int(input())

	for i in range(t):
		x = input()
		pa = int(x.split()[0])
		pb = int(x.split()[1])
		g1 = float(x.split()[2])
		g2 = float(x.split()[3])
		print(crecimento(pa,pb,g1,g2))



def crecimento(pa,pb,g1,g2):
	cont = 0
	while pa <= pb:
		pa = pa + ((pa*g1)//100)
		pb = pb + ((pb*g2)//100)
		cont += 1
	if cont > 100:
		return "Mais de 1 seculo."
	else:
		return "%d anos." % cont




if __name__ == '__main__':
	main()