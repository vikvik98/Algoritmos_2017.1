def main():

	lista = [0] * 20
	a = len(lista)
	x = 19

	for i in range(a):
		n = int(input())
		lista[x-i] = n
	
	for i in range(a):
		print("N[%d] = %d" % (i,lista[i]))





if __name__ == '__main__':
	main()
