def main():

	a = input()
	b = float(input())
	c = float(input())

	print("TOTAL = R$ %.2f" % salario_bonus(b,c))

def salario_bonus(b,c):
	total = b + ((c*15)/100)
	return total


if __name__ == '__main__':
	main()