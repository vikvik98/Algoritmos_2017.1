# Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes.
def main():
	
	entrada = input()
	valor = entrada.split()
	n1 = int(valor[0])
	n2 = int(valor[1])
	n3 = int(valor[2])
	n4 = int(valor[3])
	n5 = int(valor[4])

	if n1!=n2!=n3!=n4!=n5:
		if n1>n2 and n1>n3 and n1>n4 and n1>n5:
			maior = n1
		elif n1<n2 and n1<n3 and n1<n4 and n1<n5:
			menor = n1

		if n2>n1 and n2>n3 and n2>n4 and n2>n5:
			maior = n2
		elif n2<n1 and n2<n3 and n2<n4 and n2<n5:
			menor = n2

		if n3>n1 and n3>n2 and n3>n4 and n3>n5:
			maior = n3
		elif n3<n1 and n3<n2 and n3<n4 and n3<n5:
			menor = n3

		if n4>n1 and n4>n2 and n4>n3 and n4>n5:
			maior = n4
		elif n4<n1 and n4<n2 and n4<n3 and n4<n5:
			menor = n4

		if n5>n1 and n5>n2 and n5>n3 and n5>n4:
			maior = n5
		elif n5<n1 and n5<n2 and n5<n3 and n5<n4:
			menor = n5

		print('%d é o maior e %d é o menor' % (maior, menor))


if __name__ == '__main__':
	main()
