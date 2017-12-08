print ("Informe quantos metros deseja converter em Km.")
# Entrada
M = float (input ("Valor metros:"))

# Calculos
Km = M // 1000
m = M % 1000

# Saída
print (M, "metros são =", Km, "km", "e", m, "metros")