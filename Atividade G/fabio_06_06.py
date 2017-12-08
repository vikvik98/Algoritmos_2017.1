def main():
	#48 a 57
    frase = input("Digite uma frase: \n")
    nova_frase = ""
    for letra in frase:
       if is_number(letra):
       		print(getAlgarismo(letra),end="")
       else:
       		print(letra,end="")
    print("\n")

def is_number(letra):
	return ord(letra) >= 48 and ord(letra) <= 57

def getAlgarismo(algarismo):
	algo = ""
	if(algarismo == "0"):
		algo = "Zero"
	elif(algarismo == "1"):
		algo = "Um"
	elif(algarismo == "2"):
		algo = "Dois"	
	elif(algarismo == "3"):
		algo = "Três"
	elif(algarismo == "4"):
		algo = "Quatro"
	elif(algarismo == "5"):
		algo = "Cinco"
	elif(algarismo == "6"):
		algo = "Seis"
	elif(algarismo == "7"):
		algo = "Sete"
	elif(algarismo == "8"):
		algo = "Oito"
	elif(algarismo == "9"):
		algo = "Nove"

	return algo

if __name__ == '__main__':
	main()