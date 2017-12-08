def main():

	# O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
	
	q_cont = int(input('Digite a quantidade de containers: '))
	x = 1
	peso_carga = 0
	peso_cont = 0
	
	while x <= q_cont :
		peso_cont = float(input('Digite o peso do container %d: ' % x))
		x += 1
		peso_carga += peso_cont

	# O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua bagagem; cada passageiro tem o peso estimado de 70kg e cada volume de bagagem tem peso estimado de 10kg.

	# A seguir devem ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do bilhete seja igual a 0.

	peso_passageiro = 0
	cada_volume = 0
	bilhete = None
	quantidade_passageiros = 0
	volume_bagagem = 0
	
	while bilhete != 0:
		
		bilhete = int(input('Digite o número do bilhete: '))
		
		if bilhete != 0: 
			
			cada_volume = int(input('Digite quantos volumes o passageiro %d tem (Kg): ' % bilhete))
			peso_passageiro += 70 
			volume_bagagem += 10 * cada_volume
			quantidade_passageiros += 1
	print('Quantidade de passageiros é: %d' % quantidade_passageiros)
	print('A quantidade de volume de bagagem é igual a: %d Kg' % volume_bagagem)
	print('Peso dos passageiros: %d Kg' % peso_passageiro)
	print('O peso de carga é de: %.1f Kg' % peso_carga)

	# O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos passageiros; 

	peso_decolagem = peso_carga + peso_passageiro + volume_bagagem	
	peso_combustivel = 500000 - peso_decolagem
	quantidade_combustivel = peso_combustivel / 1.5
	print('A quantidade de combustivel é de: %.1f L' % quantidade_combustivel)

	if (quantidade_combustivel >= 10000) :
		print('O vôo foi liberado. ')
	else :
		print('O vôo não pode acontecer!')

	# O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg


	# A quantidade mínima de combustível para que a aeronave decole é de 10000 l;




if __name__ == '__main__':
	main()