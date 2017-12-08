import os, platform
def main():

	celulares = []
	ler_arquivo(celulares)
	apagar_tela()

	while True:
		
		x = int(input(menu()))
		

		if x == 0:
			apagar_tela()
			saida_arquivo(celulares)
			print('Falloouuu.')
			break
		if x == 1:
			apagar_tela()
			novo_celular(celulares)
		if x == 2:
			apagar_tela()
			listar_celulares(celulares)
		if x == 3:
			apagar_tela()
			filtra_fabricante_so(celulares)
		if x == 4:
			apagar_tela()
			filtrar_valor(celulares)
		if x == 5:
			apagar_tela()
			media_valores(celulares)
		if x == 6:
			apagar_tela()
			media_valores_marca(celulares)
		if x == 7:
			apagar_tela()
			menor_maior(celulares)

		input('De um "enter"!')
		apagar_tela()


def saida_arquivo(celulares):
	arquivo = open('arquivo.txt', 'w')
	for i in celulares:
		linha = i['fabricante'] + '-' + i['modelo'] + '-' + i['so'] + '-' + str(i['ram']) + '-' + str(i['armazenamento']) + '-' + str(i['frequencia']) + '-' + str(i['preço']) + "\n"
		arquivo.write(linha)
	arquivo.close()



def ler_arquivo(celulares):
	arquivo = open('arquivo.txt', 'a+')
	arquivo.seek(0)	
	for linha in arquivo:
		celular = {}
		linha = linha.strip().split('-')
		celular['fabricante'] = linha[0]
		celular['modelo'] = linha[1]
		celular['so'] = linha[2]
		celular['ram'] = int(linha[3])
		celular['armazenamento'] = int(linha[4])
		celular['frequencia'] = float(linha[5])
		celular['preço'] = float(linha[6])
		celulares.append(celular)


def menor_maior(celulares):
	maior = celulares[0]['preço']
	menor = celulares[0]['preço']
	for i in range(len(celulares)):
		if celulares[i]['preço'] < menor:
			menor = celulares[i]['preço']
		if celulares[i]['preço'] > maior:
			maior = celulares[i]['preço']
	print('O celular mais caro custa = %2.f' % maior)
	print('O celular mais barato custa = %2.f' % menor)


def media_valores_marca(celulares):
	z = input('Digite a fabricante para saber a media de valores dele:\n')
	soma = 0
	cont = 0
	for i in range(len(celulares)):
		if celulares[i]['fabricante'] == z:
			soma += celulares[i]['preço']
			cont += 1
	print('A media de preço para esta marca eh = %2.f' % (soma/cont))


def media_valores(celulares):
	soma = 0
	for i in range(len(celulares)):
		soma += celulares[i]['preço']
	print('A media de valores dos celulares eh = %2.f' % (soma/len(celulares)))


def filtrar_valor(celulares):
	if len(celulares) == 0:
		print('Nao existe celulares cadastrados.')
		return
	z = int(input('Digite o valor:\n'))
	for i in range(len(celulares)):
		if celulares[i]['preço'] == z:
			print(celulares[i])


def filtra_fabricante_so(celulares):
	if len(celulares) == 0:
		print('Nao existe celulares cadastrados.')
		return
	z = input('Digite a fabricante ou S.O:\n')
	for i in range(len(celulares)):
		if celulares[i]['fabricante'] == z or celulares[i]['so'] == z:
			print(celulares[i])


def apagar_tela():
	so = platform.system()
	if so == 'Windows':
		os.system('cls')
	else:
		os.system('clear')


def listar_celulares(celulares): 
	for i in range(len(celulares)):
		print('Celular: %d' % (i+1))
		print('Fabricante: %s' % celulares[i]['fabricante'])
		print('Modelo: %s' % celulares[i]['modelo'])
		print('S.O: %s' % celulares[i]['so'])
		print('Memoria Ram: %s' % celulares[i]['ram'])
		print('Armazenamento: %s' % celulares[i]['armazenamento'])
		print('Frequencia: %s' % celulares[i]['frequencia'])
		print('Preço medio: %s\n' % celulares[i]['preço'])


def novo_celular(celulares):
	celular = {}
	print('Novo celular')
	celular['fabricante'] = input('Fabricante:\n')
	celular['modelo'] = input('Modelo:\n')
	celular['so'] = input('S.O:\n')
	celular['ram'] = int(input('Memoria Ram:\n'))
	celular['armazenamento'] = int(input('Armazenamento:\n'))
	celular['frequencia'] = float(input('Frequencia do processador:\n'))
	celular['preço'] = float(input('Preço medio:\n'))
	celulares.append(celular)
	print('Celular cadastrado com sucesso...')


def menu():
	return ('\n_______Sistema de cadastro________\n\
1) Novo celular.\n\
2) Listar celular.\n\
3) Filtrar celulares por: Fabricante e SO.\n\
4) Filtrar celular por: valor.\n\
5) Media de valores.\n\
6) Media de valores de uma marca escolhida.\n\
7) Celular mais caro e mais barato.\n\
0) Sair.\n\
Opção:\n')





if __name__ == '__main__':
	main()