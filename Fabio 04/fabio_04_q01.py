def main():
	n = 1

	while n:
		n =  int(input("Digite um numero:\n"))
		getDivisores(n)

#mostra os divisores de N
def getDivisores(n):
	c = n
	while c > 0:
		if(n % c == 0):
			print("%d eh divisor de %d" % (c,n))
		c =  c - 1 

if __name__ == '__main__':
	main()