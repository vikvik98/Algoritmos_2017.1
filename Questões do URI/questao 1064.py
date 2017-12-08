def main():
	z = 0
	c = 0
	for i in range(6):
		n = float(input())
		if n > 0:
			c += 1
			z += n
	resultado = (z / c)
	print("%d valores positivos" % c)
	print("%.1f" % resultado)

	

if __name__ == '__main__':
	main()
