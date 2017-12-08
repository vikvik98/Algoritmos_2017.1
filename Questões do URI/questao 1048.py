def main():
	
	n = float(input())
	reajuste = 0
	salario = 0

	if n <= 400:
		reajuste = (n*15) / 100
		salario = n + reajuste
		print("Novo salario: %.2f" % salario)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 15 %")
	elif n > 400 and n <= 800:
		reajuste = (n*12) / 100
		salario = n + reajuste
		print("Novo salario: %.2f" % salario)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 12 %")
	elif n > 800 and n <= 1200:
		reajuste = (n*10) / 100
		salario = n + reajuste
		print("Novo salario: %.2f" % salario)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 10 %")
	elif n > 1200 and n <= 2000:
		reajuste = (n*7) / 100
		salario = n + reajuste
		print("Novo salario: %.2f" % salario)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 7 %")
	elif n > 200:
		reajuste = (n*4) / 100
		salario = n + reajuste
		print("Novo salario: %.2f" % salario)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 4 %")			

if __name__ == '__main__':
	main()