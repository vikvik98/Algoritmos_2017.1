def main():
	X = int(input("Digite o numero X:\n"))
	N = int(input("Digite o numero N:\n"))

	while N > 2:
		resultado =  X // N
		print(" Resultado da divisão de %d / %d  = %d" % (X,N,resultado))
		X = resultado
		N =  N - 1

if __name__ == '__main__':
	main()