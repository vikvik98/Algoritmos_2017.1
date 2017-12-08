print ("Digite um valor com 3 digitos para que a centena, dezena e unidade sejam somados.")

# Entrada
Valor = int (input ("Valor:"))

# Calculos
C = Valor // 100 * 100
D = (Valor - C) // 10 * 10
U = (Valor - C - D) 


# Saída
print ("Centena =", C, "Dezena =", D, "e", "Unidade =", U, "e a soma da centena + dezena + unidade é =", C + D + U)