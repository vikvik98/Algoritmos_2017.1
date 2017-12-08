def main():
	
	horario = input("Digite as horas: ")

	hora = horario.split(":")[0]
	minuto = horario.split(":")[1]
	seg = horario.split(":")[2]

	print("%s hora(s), %s minuto(s) e %s segundo(s)" % (hora, minuto, seg))


if __name__ == '__main__':
	main()