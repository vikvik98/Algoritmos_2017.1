# Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.
def main():
	
	entrada = input()
	valor = entrada.split()
	n1 = int(valor[0])
	n2 = int(valor[1])
	n3 = int(valor[2])
	n4 = int(valor[3])
	n5 = int(valor[4])

	media = (n1+n2+n3+n4+n5) / 5

	if n1>media:
		maior = "%d " % n1

	if n2>media:
		maior += "%d " % n2

	if n3>media:
		maior += "%d " % n3

	if n4>media:
		maior += "%d " % n4
	
	if n5>media:
		maior += "%d " % n5
	
	print("%d é/sao maiore(s) que a media" % maior)


if __name__ == '__main__':
	main()
