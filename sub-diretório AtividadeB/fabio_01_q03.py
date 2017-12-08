print ("Digite o valor em minuto(s) na qual você deseja converter em horas e minutos.")

# Entrada
Minutos = float (input ("Minuto(s):"))

# Calculos
Horas = Minutos // 60
minutos = Minutos % 60

# Saída
print (Minutos, "minuto(s) são:", Horas, "hora(s)", "e", minutos, "minuto(s)")
