def main():

	n = input()

	a = int(n.split()[0])
	b = int(n.split()[1])
	c = int(n.split()[2])
	x = False

	if a < b:
		a, b = b , a
	if a < c:
		a, c = c, a
	if b < c:
		b, c = c, b

	if a==b+c or a==b or a==c or b==c:
		x = True

	if x:
		print("S")
	else:
		print("N")

if __name__ == '__main__':
	main()