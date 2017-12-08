print ("Informe o(s) segundo(s) para que seja convertido em hora(s), minuto(s) e segundo(s)")

# Entrada
Segundos = int (input ("Segundo(s):"))

# Calculos
Horas = Segundos // 3600
Sobra_horas = Segundos % 3600
Minutos = Sobra_horas // 60
Sobra_minutos = Sobra_horas % 60
segundos = Sobra_minutos

# Saída
print (Segundos, "segundo(s) são =", Horas, "hora(s)", Minutos, "minuto(s)", "e", segundos, "segundo(s)")