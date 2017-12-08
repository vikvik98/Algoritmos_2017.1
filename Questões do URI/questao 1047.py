def main():

	n = input()
	hora_ini = int(n.split()[0])
	minuto_ini = int(n.split()[1])
	hora_fin = int(n.split()[2])
	minuto_fin = int(n.split()[3])

	if hora_fin <= hora_ini:
		hora_fin += 24

	horas_inicial = (hora_ini*60) + (minuto_ini)
	horas_final = (hora_fin*60) + (minuto_fin)
	horas = (horas_final - horas_inicial) / 60
	minutos = (horas_final - horas_inicial) % 60

	print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (horas, minutos))


	


if __name__ == '__main__':
	main()
