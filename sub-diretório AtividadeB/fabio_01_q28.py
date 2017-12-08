print ("Informe o numero de hora(s) para que seja convertido para semana(s), dia(s) e hora(s) ")

#Entrada
Horas = int (input ("Hora(s):"))

# Calculos
Semanas = Horas // 168
Sobra_semanas = Horas % 168
Dia = Sobra_semanas // 24
Sobra_dia = Sobra_semanas % 24
horas = Sobra_dia

# Saída
print (Horas, "hora(s) são =", Semanas, "semana(s)", Dia, "dias", "e", horas, "hora(s)")