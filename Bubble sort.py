lista = [5, 3, 7, 4, 2, 1, 6]

while True:
    troca = False
    for i in range(1,len(lista)):
        for j in range(len(lista)-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                troca = True
    if not troca:
        break
        

print(lista)
