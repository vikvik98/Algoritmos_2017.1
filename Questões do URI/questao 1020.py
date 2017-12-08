def main():

	N = int(input())

	Ano = N // 365
	Mes = N % 365 // 30
	Dia = N % 365 % 30

	print('%d ano(s)' % Ano)
	print('%d mes(es)' % Mes)
	print('%d dia(s)' % Dia)

if __name__ == '__main__':
	main()
