def main():
	n =  int(input("Digite um numero:\n"))
	while n >= 1:
		q = n // 2
		
		if(q >= 1):
			n = q
		else:
			break

	print("Resultado da última divisão: %d" % n)
	
if __name__ == '__main__':
	main()