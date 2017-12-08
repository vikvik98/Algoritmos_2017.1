def main():

	x = input()
	a = int(x.split()[0])
	b = int(x.split()[1])
	c = int(x.split()[2])

	print("%d eh o maior" % maior(a,b,c))

def maior(a,b,c):
	maior = (a+b+abs(a-b))/2
	if c > maior:
		maior = c
	return maior


if __name__ == '__main__':
	main()