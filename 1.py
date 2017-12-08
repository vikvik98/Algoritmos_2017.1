from fractions import Fraction
def main():
# Letra A
	n = int(input())
	soma = 0
	for i in range(n):
		soma += (1+i)/(n-i)
		
	print(soma)


# Letra B
	
	soma2 = float(sum([Fraction((1+i)/(n-i)) for i in range(n)]))
	print(soma2)

if __name__ == '__main__':
	main()