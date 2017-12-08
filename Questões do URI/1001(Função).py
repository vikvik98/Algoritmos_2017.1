def main():

	a = int(input())
	b = int(input())
	x = soma(a,b)
	print("X = %d" % x)
	

def soma(a,b):
	x = a+b
	return x


if __name__ == '__main__':
	main()