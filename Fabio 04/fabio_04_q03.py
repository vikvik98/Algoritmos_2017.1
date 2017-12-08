def main():
	n = input("Digite dois numeros (A B):\n")
	A  =  int(n.split()[0])
	B  =  int(n.split()[1])
	mdc = getMDC(A,B)
	print("MDC = %d" % mdc)

def getMDC(num1,num2):
	
	# pega o maior de dois numeros
	a = getMaior(num1,num2)

	#pega o menor -  soma os dois e subtrai o maior
	b =  num1 + num2 - a

	#define uma variavel indefinida
	resto = None

	#pega o MDC que será a variavel a
	while resto != 0:
		resto = a % b
		a = b
		b = resto

	return a

		
def getMaior(a,b):
	maior =  (a + b + abs(a-b)) // 2
	return maior


if __name__ == '__main__':
	main()