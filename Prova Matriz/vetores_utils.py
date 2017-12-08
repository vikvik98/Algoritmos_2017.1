def main():

#Search
def contem(vetor,elemento):
	for i in vetor:
		if i == elemento:
			return True
	return False

#Reduce
def media(vetor):
	soma = 0
	for i in vetor:
		soma += i
	media = soma / len(vetor)
	return media

#Reduce
def somatorio(vetor):
	somatorio = 0
	for i in vetor:
		somatorio += i
	return somatorio

#Search
def buscar(vetor,elemento):
	for i in range(len(vetor)):
		if vetor[i] == elemento:
			return i
			break


if __name__ == '__main__':
	main()