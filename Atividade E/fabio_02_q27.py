def main():
	
	data_nasc = input('Data de nascimento: ')
	data_atual = input('Data atual: ')

	dia_nasc = int(data_nasc.split()[0])
	mes_nasc = int(data_nasc.split()[1])
	ano_nasc = int(data_nasc.split()[2])

	dia_atual = int(data_atual.split()[0])
	mes_atual = int(data_atual.split()[1])
	ano_atual = int(data_atual.split()[2])

	
	if mes_atual==mes_nasc:
		if dia_atual<dia_nasc:
			dia_atual += 30
			mes_atual += 12 - 1
			ano_atual -= 1

	elif mes_atual<mes_nasc:
		if dia_atual<dia_nasc:
			dia_atual += 30
			mes_atual += 12 - 1

		else:
			mes_atual += 12

		ano_atual -= 1

	elif dia_atual<dia_nasc:
		dia_atual += 30
		mes_atual -= 1

	idade_ano = ano_atual-ano_nasc
	idade_dias =  dia_atual-dia_nasc
	idade_meses = mes_atual-mes_nasc


	print('Sua idade eh %d anos %d meses e %d dias' % (idade_ano, idade_meses, idade_dias))


if __name__=='__main__':
	main()