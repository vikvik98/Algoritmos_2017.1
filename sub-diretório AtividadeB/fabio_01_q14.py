print ("Digite as 3 ultimas notas do aluno e decida o peso para as 3 para que possa ser tirada a media ponderada.")

# Entrada
Nota_1 = float (input ("Nota 1:"))
Peso_nota_1 = float (input ("Peso para a nota 1:"))
Nota_2 = float (input ("Nota 2:"))
Peso_nota_2 = float (input ("Peso para a nota 2:"))
Nota_3 = float (input ("Nota 3:"))
Peso_nota_3 = float (input ("Peso para a nota 3:"))

# Calculos
Media_ponderada = (Nota_1 * Peso_nota_1 + Nota_2 * Peso_nota_2 + Nota_3 * Peso_nota_3) / (Peso_nota_1 + Peso_nota_2 + Peso_nota_3)

# Saída
print ("A media ponderada do aluno é =", Media_ponderada)