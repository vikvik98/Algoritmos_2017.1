import os
def main():
	senha = False
	while senha != "asdf123":
		senha = input("Senha: ")
		os.system('cls')
		print("Senha:", "*" * len(senha))
		
		if senha != "asdf123":			
			print("Incorreto. Tente novamente\n")

		else:
			print("Loading....")


if __name__ == '__main__':
	main()