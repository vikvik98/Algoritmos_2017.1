def main():

	n = int(input())

	vetor_a = [0] * n
	vetor_b = [0] * n
	cont = n

	# Geração de vetor
	for i in range(n):
		x = int(input())
		vetor_a[i] = x

	for i in range(n):
		vetor_b[i] = vetor_a[cont-1]
		cont -= 1

	print(vetor_a)
	print(vetor_b)






if __name__ == '__main__':
	main()