def main():

	raio = float(input())

	print("A=%.4f" % area(raio))


def area(raio):
	area = 3.14159 * (raio**2)
	return area



if __name__ == '__main__':
	main()