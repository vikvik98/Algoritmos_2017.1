# Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.
def main():
	
	data_atual = input("Data:")
	valor = data_atual.split()
	dias_atual = int(valor[0])
	mes_atual = int(valor[1])
	ano_atual = int(valor[2]) 

	if dias_atual <= 31 and mes_atual <= 12:
		print("Essa data é valida.")
	else:
		print("Essa data não é valida.") 

		
if __name__ == '__main__':
	main()
