def main():

	data = input("Digite a data (dd/mm/aaaa)")
	
	data_quebrada = data.split("/")

	dia = data_quebrada[0]
	mes = data_quebrada[1]
	ano = data_quebrada[2]

	if mes == "01":
		mes_extenso = "Janeiro"

	elif mes == "02":
		mes_extenso = "Fevereiro"

	elif mes == "03":
		mes_extenso = "Marco"
	
	elif mes == "04":
		mes_extenso = "Abril"
	
	elif mes == "05":
		mes_extenso = "Maio"
	
	elif mes == "06":
		mes_extenso = "Junho"
	
	elif mes == "07":
		mes_extenso = "Julho"
	
	elif mes == "08":
		mes_extenso = "Agosto"
	
	elif mes == "09":
		mes_extenso = "Setembro"
	
	elif mes == "10":
		mes_extenso = "Outubro"

	elif mes == "11":
		mes_extenso = "Novembro"
	
	elif mes == "12":
		mes_extenso = "Dezembro"

	else:
		mes_extenso = "***Invalido***"

	print("%s de %s de %s" % (dia, mes_extenso, ano))
	
	
	

if __name__ == '__main__':
	main()