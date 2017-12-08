def main():

	n = int(input())
	
	vetor = [0] * n
	repetidos = 0
	
	#Geração de vetor
	for i in range(len(vetor)):
		x = int(input())
		vetor[i] = x


	#Search
	for i in range(len(vetor)-1):
		for j in range(i+1,len(vetor)):
			if vetor[i] == vetor[j]:
				repetidos += 1
	if repetidos > 0:
		print("Há numeros repetidos.")
	else:
		print("Não há numeros repetidos.")



if __name__ == '__main__':
	main()
