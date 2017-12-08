def main():

	n = int(input())

	#Geração de vetor
	while n < 2:
		n = int(input())

	vetor = [0] * n

	vetor[0] = 0
	vetor[1] = 1

	for i in range(2, n):
		vetor[i] = vetor[i - 1] + vetor[i - 2]
	print(vetor)



if __name__ == '__main__':
	main()
