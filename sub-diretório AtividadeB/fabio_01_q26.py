print ("Informe o(s) dia(s) para que converta para semana(s)")

# Entrada
Dias = int (input ("Dias:"))

# Calculos
Semanas = Dias // 7 
dias = Dias % 7

# Saída
print (Dias, "dia(s) são =", Semanas, "semana(s)", "e", dias, "dia(s)")