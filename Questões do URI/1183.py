def main():

	o = input()

	#Geração de vetores
	linha = [0] * 12
	for i in range(len(linha)):
		linha[i] = [0] * 12

	valores_coluna(linha)
	print("%.1f" % operacao(o,linha))


def valores_coluna(linha):
	for i in range(len(linha)):
		for j in range(len(linha[i])):
			linha[i][j] = float(input())
	return linha

def operacao(o,linha):
	if o == "S":
		resultado = 0
		for i in range(len(linha)):
			for j in range(len(linha[i])):
				if i < j:
					resultado += linha[i][j]
	elif o == "M":
		resultado = 0
		cont = 0
		for i in range(len(linha)):
			for j in range(len(linha[i])):
				if i < j:
					resultado += linha[i][j]
					cont +=1

		resultado = resultado / cont
	return resultado

if __name__ == '__main__':
	main()