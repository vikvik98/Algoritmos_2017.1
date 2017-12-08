def main():

	n = int(input())
	vetor_a = [0] * n
	vetor_b = [0] * n
	vetor_c = [0] * (2*n)

	#Geração de vetor
	for i in range(len(vetor_a)):
		x = int(input())
		vetor_a[i] = x

	for i in range(len(vetor_b)):
		y = int(input())
		vetor_b[i] = y

	for i in range(len(vetor_a)):
		vetor_c[i] = vetor_a[i]

	for i in range(len(vetor_b)):
		vetor_c[i+n] = vetor_b[i]

	print(vetor_a)
	print(vetor_b)
	print(vetor_c)


if __name__ == '__main__':
	main()