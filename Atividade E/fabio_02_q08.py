# Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva sua idade exata (em anos).
def main():
	
	data_atual = input("Data atual:")
	valor = data_atual.split()
	dias_atual = int(valor[0])
	mes_atual = int(valor[1])
	ano_atual = int(valor[2])

	data_nasc = input("Data de nascimento:")
	valor2 = data_nasc.split()
	dias_nasc = int(valor2[0])
	mes_nasc = int(valor2[1])
	ano_nasc = int(valor2[2])

	idade_dias = (dias_atual + (mes_atual * 30) + (ano_atual * 365)) - (dias_nasc + (mes_nasc * 30) + (ano_nasc * 365))
	idade_ano = idade_dias // 365

	print("Você tem: %d" % idade_ano, "anos.")

		
if __name__ == '__main__':
	main()
