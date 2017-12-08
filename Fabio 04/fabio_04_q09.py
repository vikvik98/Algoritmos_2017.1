def main():
	entrada =  input()
	np = int(entrada.split()[0])
	nn = int(entrada.split()[1])
	clube_a = 0
	clube_b = 0
	while np != 0 and nn != 0 :
		nome = input("Digite o nome do nadador:\n")
		clube = input("Digite o clube do nadador: (a ou b)\n")
		
		qtd_prova = 0
		#faz um loop para digitar a pontuação de cada prova
		while qtd_prova < np:
			print("***********************************************")
			print("   DESEMPENHO NA PROVA %d   " % qtd_prova+1)
			print("***********************************************")
			classificacao = int(input("Digite a classificação do nadador:\n"))
			tempo = float(input("Digite o tempo do nadador:\n"))
			if(clube=="a"):
				clube_a = clube_a + getPontuacao(classificacao)
			else:
				clube_b = clube_b + getPontuacao(classificacao)
			qtd_prova = qtd_prova + 1

		nn = nn - 1

	print("***********************************************")
	print("****************  RESULTADO FINAL  ************")
	print("***********************************************")

	print("TIME A: %d pontos" % clube_a)
	print("TIME B: %d pontos" % clube_b)
	
	if(clube_a > clube_b):
		print("O vencedor foi A")
	elif(clube_a < clube_b):
		print("O vencedor foi B")
	else:
		print("Não houve vencedor")



def getPontuacao(classificacao):
	pontos = 0
	if(classificacao == 1):
		pontos = 9
	elif(classificacao == 2):
		pontos = 6
	elif(classificacao == 3):
		pontos = 4
	else:
		pontos = 3
	return pontos


if __name__ == '__main__':
	main()