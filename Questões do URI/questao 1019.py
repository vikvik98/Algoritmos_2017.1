def main():

	N = int(input())

	Horas = N // 3600
	Minutos = N % 3600 // 60
	Segundos = N % 3600 % 60

	print('%d:%d:%d' % (Horas,Minutos,Segundos))

if __name__ == '__main__':
	main()
