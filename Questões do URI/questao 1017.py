def main():

	Tempo = int(input())
	Km_h = int(input())
	Km_l = 12
	Resultado = (Tempo * Km_h) / Km_l
	print('%.3f' % Resultado)
	
if __name__ == '__main__':
	main()