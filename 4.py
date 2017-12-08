from fractions import Fraction
def main():

	n = int(input())

	lista = [Fraction(1/n+i) for i in range(n+1)]
	soma = float(sum(lista))
	print(soma)
	print(sumlista(lista))

def sumlista(lista):
	if len(lista) == 1:
		return lista[0]
	else:
		return float(lista[0] + sumlista(lista[1:]))

	



if __name__ == '__main__':
	main()