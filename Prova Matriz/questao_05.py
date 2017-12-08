from matrizes_utils import *

def main():

	pilotos = int(input())

	matriz = [0] * pilotos

	for i in range(len(matriz)):
		matriz[i] = input("Digite o nome do piloto: \n")
		for j in range(len(matriz[i])):
			tempo = int(input("Digite o tempo em que o piloto terminou a corrida: \n"))
			matriz[i].append(tempo)


	tempo_medio = media(matriz)
	print("O tempo medio da corrida foi de %.2f minutos" % tempo_medio)

	pilotos_abaixo_media = 0

	for i in range(len(matriz)):
		for j in range(matriz[i]):
			if matriz[i][j] < tempo_medio:
				pilotos_abaixo_media += 1
	print("%d pilotos terminaram a corrida abaixo da media." % pilotos_abaixo_media)

	velocidade_media = []
	tempo_medio_piloto = 0

	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			tempo_medio_piloto = 360 / (matriz[i][j] / 60)
			velocidade_media.append(tempo_medio_piloto)

	menor_tempo = matriz[0][0]
	pilotos_campeao = 0
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] < menor_tempo:
				menor_tempo = matirz[i][j]
				pilotos_campeao = i
	print("O piloto campeao é o %s, o seu tempo foi de %d e o seu tempo medio foi de %.2f" % (matriz[pilotos_campeao],menor_tempo,velocidade_media[pilotos_campeao]))

	for i in range(len(matriz)):
		for j in range(matriz[i]):
			print("NOME: %S / TEMPO: %d / VELOCIDADE: %2.f" % (matriz[i]),matriz[i][j],velocidade_media[i])






if __name__ == '__main__':
	main()