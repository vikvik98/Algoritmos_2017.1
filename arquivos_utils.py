def novo_arquivo(nome):
	arquivo = open(nome, "x")
	return arquivo


def abrir_arquivo(nome):
	arquivo = open(nome, "r")
	return arquivo


def abrir_ou_criar(nome):
	arquivo = open(nome, "a+")
	arquivo.seek(0)
	return arquivo


def gravar_em_arquivo(linhas, nome):
	arquivo = open(nome, "w")
	for linha in linhas:
		arquivo.write(linha)
	arquivo.close()


