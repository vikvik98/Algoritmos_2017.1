print ("Informe o numero de minuto(s) para que seja convertido para dia(s), hora(s) e minuto(s) ")

#Entrada
Minuto = int (input ("Minutos(s):"))

# Calculos
Dia = Minuto // 1440
Sobra_dia = Minuto % 1440
Hora = Sobra_dia // 60 
Sobra_hora = Sobra_dia % 60
minuto = Sobra_hora 



# Saída
print (Minuto, "minutos(s) são =", Dia, "dia(s)", Hora, "hora(s)", "e", minuto, "minutos(s)")