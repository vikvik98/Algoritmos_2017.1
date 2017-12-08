#Search
def contem(matriz,elemento):
	for i in vetor:
		for j in i:
			if j == elemento:
				return True
	return False

#Reduce
def media(matriz):
	soma = 0
	cont = 0
	for i in vetor:
		for j in i:
			soma += j
			cont += 1
	media = soma / cont
	return media

#Reduce
def somatorio(matriz):
	somatorio = 0
	for i in vetor:
		for j in i:
			somatorio += j
	return somatorio

#Search
def buscar(matriz,elemento):
	for i in range(len(vetor)):
		for j in range(len(vetor[i])):
			if vetor[i][j] == elemento:
				return i
				return j
				break
