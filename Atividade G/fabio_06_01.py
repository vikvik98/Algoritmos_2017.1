def main():
    frase = input('Digite uma frase: ')
    frase_invertida = inverter(frase)
    frase_substituida = substituir_consoante(frase_invertida)
    print('Resposta >> ', frase_substituida)


def substituir_consoante(frase):
    nova_frase = ''
    for letra in frase:
        if eh_vogal(letra):
           nova_frase += letra
        else:
           nova_frase += '#'
    return nova_frase

def eh_vogal(letra):
    vogais = 'AEIOUaeiou '
    return letra in vogais

def inverter(frase):
    invertida = ''
    for i in range(len(frase) -1, -1, -1):
        invertida += frase[i]
    return invertida


if __name__ == '__main__':
	main()