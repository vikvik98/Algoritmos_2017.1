def main():

	a = int(input())
	b = int(input())
	c = int(input())
	d = int(input())
	print("DIFERENCA = %d" % diferenca(a,b,c,d))

def diferenca(a,b,c,d):
	diferenca = (a*b) - (c*d)
	return diferenca


if __name__ == '__main__':
	main()