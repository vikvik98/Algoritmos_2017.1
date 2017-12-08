def main():
	n = input("DIDITE 3 NUMEROS: \n")
	a = int(n.split()[0])
	b = int(n.split()[1])
	c = int(n.split()[2])
	mmc = getMMC(a,b,c)
	mdc = getMDC(a,b,c)
	print("MMC = ", mmc)
	print("MDC = ", mdc)


# função responsável para calcular o MMC de 3 numeros
def getMMC(a,b,c):
	lista = []
	maior =  getMaior(a,b,c)
	i = 2
	while i <= maior:
			# faz a decomposição dos 3 valores
			if(a <= 1 and b <= 1 and c<=1):
				break
			if(a % i == 0 and b % i == 0 and c % i == 0 and a > 1 and b > 1 and c > 1):
				a = a // i
				b = b // i
				c = c // i
				lista.append(i)
			elif(a % i == 0 and  b % i == 0 and a > 1 and b > 1):
				a = a // i
				b = b // i
				lista.append(i)
			elif(a % i == 0 and  c % i == 0 and a > 1 and c > 1):
				a = a // i
				c = c // i
				lista.append(i)
			elif(b % i == 0 and  c % i == 0 and b > 1 and c > 1):
				b = b // i
				c = c // i
				lista.append(i)
			elif(a % i == 0 and a > 1):
				a = a // i
				lista.append(i)
			elif(b % i == 0 and b > 1):
				b = b // i
				lista.append(i)
			elif(c % i == 0 and c > 1):
				c = c // i
				lista.append(i)
			else:
				i = i + 1

	x = 1
	for num in lista:
		x = num * x

	return x


# função responsável para calcular o MDC de 3 numeros
def getMDC(a,b,c):
	menor =  getMenor(a,b,c)
	max_div = 1
	for i in range(1,menor+1):
		
		if(a % i == 0 and b % i == 0 and c % i == 0):
			max_div =  i
		i = i + 1

	return max_div
				


# pega o maior 
def getMaior(a,b,c):
	maior =  (a + b + abs(a-b))//2
	maior =  (maior + c + abs(maior-c))//2
	return maior

#pega o menor
def getMenor(a,b,c):
	menor = (a+b) - (a + b + abs(a-b))//2
	menor = (menor+c) - (menor + c + abs(menor-c))//2
	return menor


if __name__ == '__main__':
	main()