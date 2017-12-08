#Search
def contem(registro, chave, valor):
	if registro[chave] == valor:
		return True
	return False

#Filter
def filtrar(dados, chave, valor):
	vetor = []
	for registro in dados:
		if contem(registro, chave, valor):
			vetor.append(registro)
	return vetor

#Reduce
def media(dados, chave):
	soma = 0
	for registro in dados:
		soma += registro[chave]
	media = soma / len(dados)
	return media

#Search
def maior_valor(dados, chave):
	maior = dados[0][chave]
	for registro in dados:
		if registro[chave] > maior:
			maior = registro[chave]
	return maior

#Search
def menor_valor(dados, chave):
	menor = dados[0][chave]
	for registro in dados:
		if registro[chave] < menor:
			menor = registro[chave]
	return menor


def filtro_maior_igual(dados, chave, valor):
	vetor = []
	for registro in dados:
		if registro[chave] >= valor:
			vetor.append(registro)
	return vetor
