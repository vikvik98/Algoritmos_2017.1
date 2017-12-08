def main():

	x = [0] * 12
	media = 0
	cont = 0

	for i in range(len(x)):
		x[i] = [0] * 12

	n = int(input())

	z = input()

	for i in range(len(x)):
		for j in range(len(x[i])):
			x[i][j] = float(input())

	if z == "S":
		resultado = sum(x[n])
		print("%.1f" % resultado)
	elif z == "M":
		for i in range(len(x)):
			for j in range(len(x[n])):
				media += x[n][j]
				cont += 1
		resultado = media / cont
		print("%.1f" % resultado)

		


if __name__ == '__main__':
	main()