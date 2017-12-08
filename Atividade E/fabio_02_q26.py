def main():
	
	n = input('Digite os tres lados do triangulo retangulo (L1 L2 L3): ')

	L1_hipotenusa = float(n.split()[0])
	L2_cateto = float(n.split()[1])
	L3_cateto = float(n.split()[2])
	temp = 0
	hipot = 'L1'
	cat1 = 'L2'
	cat2 = 'L3'



	if L1_hipotenusa < L2_cateto:
		temp = L1_hipotenusa
		L1_hipotenusa = L2_cateto
		L2_cateto = temp
		hipot = 'L2'
		cat1 = 'L1'

	if L1_hipotenusa < L3_cateto:
		temp = L1_hipotenusa
		L1_hipotenusa = L3_cateto
		L3_cateto = temp
		cat2 = hipot
		hipot = 'L3'
		


	if L1_hipotenusa**2 == L2_cateto**2 + L3_cateto**2:
			print('%s eh a hipotenusa \n%s e %s sao os catetos' % (hipot, cat1, cat2))


	else:
		print('Nao forma triangulo retangulo')


if __name__=='__main__':
	main()