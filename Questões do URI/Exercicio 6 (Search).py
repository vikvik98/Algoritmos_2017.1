def main():

	alunos = int(input())

	altura = [0] * alunos
	sexo = [0] * alunos
	maior = 0
	menor = 0
	mulheres = 0
	pessoas = 0

	#Geração de vetor
	for i in range(alunos):
		alt_sex = input()
		alt = float(alt_sex.split()[0])
		sex = int(alt_sex.split()[1])
		altura[i] = alt
		sexo[i] = sex

	#Search
	for i in range(alunos):
		maior = altura[0]
		if altura[i] > maior:
			maior = altura[i]

		menor = altura[0]
		if altura[i] < menor:
			menor = altura[i]
	print("O maior tem: %.2f de altura e o menor tem: %.2f de altura." % (maior, menor))

	for i in range(alunos):
		if sexo[i] == 2 and altura[i] > 1.60:
			mulheres += 1
	print("Existem %d mulheres acima da media de altura" % mulheres)

	for i in range(alunos):
		if altura[i] < 1.60:
			pessoas += 1
	print("Existem %d pessoas abaixo da media de altura" % pessoas)






if __name__ == '__main__':
	main()
