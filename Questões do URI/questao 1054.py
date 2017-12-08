def main():

	r = 0
	m = 0
	while True:
		n = int(input())
		if n < 0:
			break
		else:
			r += n
			m += 1
		resultado = (r / m)
	print("%.2f" % resultado)


if __name__ == '__main__':
	main()