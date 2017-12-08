def main():

	a = int(input())
	b = int(input())
	c = float(input())

	print("NUMBER = %d" % a)
	print("SALARY = U$ %.2f" % salario(b,c))

def salario(b,c):
	salario = b * c
	return salario


if __name__ == '__main__':
	main()