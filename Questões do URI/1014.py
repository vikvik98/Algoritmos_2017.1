def main():

	x = int(input())
	y = float(input())

	print("%.3f km/l" % litro_km(x,y))

def litro_km(x,y):
	resultado = x/y
	return resultado


if __name__ == '__main__':
	main()