def main():

	tamanho = int(input('Quantidade de pilotos: '))
	pilotos = [0] * tamanho

	distancia = 360

	for i in range(tamanho):
		coluna = [0] * 3
		
		# Nome .. 
		coluna[0] = input('\nNome: ')

		# Tempo .. 
		coluna[1] = float(input('Tempo de corrida: '))

		# C - Velocidade ..
		hora = coluna[1] / 60
		coluna[2] = distancia / hora

		pilotos[i] = coluna

if __name__ == '__main__':
	main()