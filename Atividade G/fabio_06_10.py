
def main():
	palavra = input("Digite uma palavra: ")

	if inverter(palavra) != palavra:
		print("Nao eh palindroma")
	else:
		print("Eh palindroma")

def inverter(palavra):
	invertida = ""
	for i in range(len(palavra)-1, -1, -1):
		invertida += palavra[i]
	return invertida

if __name__ == '__main__':
	main()