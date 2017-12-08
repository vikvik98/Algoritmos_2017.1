def main():
	verbo = input("Digite um verbo: ")
	conjugacao(verbo)

def conjugacao(verbo):
	sufixos = "o es e emos eis em"
	pronomes = "Eu Tu Ele Nós Vós Eles"
	pronomes =  pronomes.split()
	sufixos =  sufixos.split()
	radical = ""
	for x in range(0,len(verbo)-2):
		radical += verbo[x]
	for i in range(0,6):
		print("%s %s%s" % (pronomes[i],radical,sufixos[i]))
		

if __name__ == '__main__':
	main()