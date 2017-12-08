def main():

	n = input()
	a = int(n.split()[0])
	b = int(n.split()[1])

	media = a/b

	print("%.2f" % media)

if __name__ == '__main__':
	main()