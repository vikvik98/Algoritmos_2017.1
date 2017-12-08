def main():
    frase = input('Digite uma frase:')
    carct = input('Digite uma palavra a ser substituida:')
    subs = input('Digite um substituto para a palavra:')

    nova_frase = ''

    for i in frase.split():
        if i == carct:
            i = subs

        nova_frase = nova_frase + i + ' '


    print(nova_frase)


if __name__ == '__main__':
    main()
    
    
