def main():

	vetor1 = [0] * 5
	vetor2 = [0] * 5
	m = 0
	p = 0

	for i in range(15):
		n = int(input())
		if n % 2 == 0:
			vetor1[m] = n
			m += 1
			if m > 4:
				print("par[%d] = %d" % (0, vetor1[0]))
				print("par[%d] = %d" % (1, vetor1[1]))
				print("par[%d] = %d" % (2, vetor1[2]))
				print("par[%d] = %d" % (3, vetor1[3]))
				print("par[%d] = %d" % (4, vetor1[4]))
				m = 0
		else:
			vetor2[p] = n
			p += 1
			if p > 4:
				print("impar[%d] = %d" % (0, vetor2[0]))
				print("impar[%d] = %d" % (1, vetor2[1]))
				print("impar[%d] = %d" % (2, vetor2[2]))
				print("impar[%d] = %d" % (3, vetor2[3]))
				print("impar[%d] = %d" % (4, vetor2[4]))
				p = 0

	for i in range(p):
		print("impar[%d] = %d" % (i, vetor2[i]))

	for i in range(m):
		print("par[%d] = %d" % (i, vetor1[i]))

if __name__ == '__main__':
	main()