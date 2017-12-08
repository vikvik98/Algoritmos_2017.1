# Converta um numero do sistema binário, dado como uma cadeia de zeros e uns, para o sistema decimal de numeração. 

def main():

	binario = input('Binário: ')

	cont = 0
	deci = 0
	multi = 0
	for num in (len(binario), -1, -1):
		multi = 2 ** cont
		cont += 1
		if int(num) == 1:
			deci = deci + (multi * 1)
		elif int(num) == 0:
			deci = deci + (multi * 0)
	print(deci)
		

if __name__ == '__main__':
	main()