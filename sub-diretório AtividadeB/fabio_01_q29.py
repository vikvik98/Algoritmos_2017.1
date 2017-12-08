print ("Informe quantos meses deseja transformar em anos.")

# Entrada
Meses = int (input("Meses:"))

# Calculos
Anos = Meses // 12
meses = Meses % 12

# Saída
print (Meses, "meses são =", Anos, "anos", "e", meses, "meses")