from utils import *
from arquivos_utils import *
import os, platform, time

def main():
	celulares = []
	inicializar(celulares)

	while True:
		apagar_tela()
		opcao = int(input(menu()))

		if opcao == 1:
			novo_celular(celulares)
		elif opcao == 2:
			listar_celulares(celulares)
		elif opcao == 3:
			apagar_tela()
			opcao_filtrar = int(input(menu_filtrar()))
			if opcao_filtrar == 1:
				filtrar_fabricante(celulares)
			if opcao_filtrar == 2:
				filtrar_ram(celulares)
			if opcao_filtrar == 3:
				filtrar_armazenamento(celulares)
			if opcao_filtrar == 4:
				filtrar_valor(celulares)
		elif opcao == 4:
			apagar_tela()
			media_valores = media(celulares, "preco")
			print("Media dos valores: %.2f R$" % media_valores)
		elif opcao == 5:
			apagar_tela()
			marca = input()
			filtro_marca = filtrar(celulares, "fabricante", marca)
			if len(filtro_marca) == 0:
				print("Marca nao cadastrada")
			else:
				media_preco = media(filtro_marca, "preco")
				print("Media dos celulares %s: %.2f R$" % (marca, media_preco))
		elif opcao == 6:
			index = indice_maior_valor(celulares, "preco")
			mais_caro = [celulares[index]]
			listar_celulares(mais_caro)
			print("Celular mais caro.\n")
			input("Continuar...")
			index = indice_menor_valor(celulares, "preco")
			mais_barato = [celulares[index]]
			listar_celulares(mais_barato)
			print("Celular mais barato.\n")

		elif opcao == 0:
			linhas = []
			for celular in celulares:
				linha = celular["fabricante"]+"$"+celular["modelo"]+"$"+celular["o.s."]+"$%1.f"%celular["ram"]\
				+"$%d" % celular["memoria"] + "$%.2f" % celular["cpu"] + "$%.2f" % celular["preco"]+ "$\n"
				linhas.append(linha)

			gravar_em_arquivo(linhas, "celulares.bd")
			print('Saindo....')
			time.sleep(1)
			break
		else:
			print('Opcao invalida!')

		input('continuar...')



def filtrar_valor(celulares):
	apagar_tela()
	preco = int(input("Digite o preco minimo: "))
	filtro_celulares = filtro_maior_igual(celulares, "preco", preco)
	print("Filtro por Preco:")
	listar_celulares(filtro_celulares)


def filtrar_armazenamento(celulares):
	apagar_tela()
	memoria = int(input("Digite a quantidade minima de espaco interno: "))
	filtro_celulares = filtro_maior_igual(celulares, "memoria", memoria)
	print("Filtro por Armazenamento:")
	listar_celulares(filtro_celulares)


def filtrar_ram(celulares):
	apagar_tela()
	ram = float(input("Digite a quantidade minima de RAM que deseja: "))
	filtro_celulares = filtro_maior_igual(celulares, "ram", ram)
	print("Filtro por memoria:")
	listar_celulares(filtro_celulares)


def filtrar_fabricante(celulares):
	apagar_tela()
	marca = input("Digite a fabricante do cell: ")
	filtro_celulares = filtrar(celulares, "fabricante", marca)
	print("Filtro por marca:")
	listar_celulares(filtro_celulares)


def listar_celulares(celulares):
	apagar_tela()
	for celular in celulares:
		print("Fab. - %s" % celular["fabricante"], end=" // ")
		print("Mod. - %s" % celular["modelo"], end=" // ")
		print("O.S. - %s" % celular["o.s."], end=" // ")
		print("RAM - %.1f" % celular["ram"], end=" // ")
		print("Arm. - %d Gb" % celular["memoria"], end=" // ")
		print("CPU - %.2f GHz" % celular["cpu"], end=" // ")
		print("R$ - %.2f" % celular["preco"])


def novo_celular(celulares):
	celular = {}
	celular["fabricante"] = input("Fabricante: ")
	celular["modelo"] = input("Modelo: ")
	celular["o.s."] = input("Sistema Operacional: ")
	celular["ram"] = float(input("Memoria RAM: "))
	celular["memoria"] = int(input("Armazenamento: "))
	celular["cpu"] = float(input("Clock CPU: "))
	celular["preco"] = float(input("Preco: "))
	
	celulares.append(celular)




def inicializar(celulares):
	banco_cell = abrir_ou_criar("celulares.bd")

	for linha in banco_cell:
		#linha.strip()
		linha = linha.split("$")
		celular = {}
		celular["fabricante"] = linha[0]
		celular["modelo"] = linha[1]
		celular["o.s."] = linha[2]
		celular["ram"] = float(linha[3])
		celular["memoria"] = int(linha[4])
		celular["cpu"] = float(linha[5])
		celular["preco"] = float(linha[6])

		celulares.append(celular)


def apagar_tela():
	SO = platform.system()
	if SO == 'Windows':
		os.system('cls')
	else:
		os.system('clear')


def menu():
	return '\n ***** SysCell ***** \n\
1 - Novo celular \n\
2 - Listar celulares \n\
3 - Filtrar celulares\n\
4 - Media valores\n\
5 - Media de valores para uma devida marca\n\
6 - Mais caro e mais barato\n\
7 - Melhor opcao\n\
0 - Sair\n\n >>> '


def menu_filtrar():
	return '\n Filtrar por:\n\
1 - Fabricante \n\
2 - MEMORIA RAM \n\
3 - Armazenamento\n\
4 - Valor\n\n >>> '

if __name__ == '__main__':
	main()