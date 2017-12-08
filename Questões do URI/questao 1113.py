def main():

	entrada = input()
	valor = entrada.split()
	
	x = int(valor[0])
	y = int(valor[1])

	if x > y:
		print("Decrescente")
	elif x < y:
		print("Crescente")
		
			

if __name__ == '__main__':
	main()
