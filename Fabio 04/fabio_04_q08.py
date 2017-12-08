def main():
	N = int(input("Digite um numero:\n"))
	soma = None
	a = 0
	while soma != N :
		b = int(input("Digite outro numero:\n"))
		soma =  a + b
		a = b
	
if __name__ == '__main__':
	main()