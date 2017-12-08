print ("Forneça dois numeros para que possamos dividir a soma dos numeros pela subtração dos mesmos.")

# Entrada
Primeiro_numero = float (input ("Primeiro numero:"))
Segundo_numero = float (input ("Segundo numero:"))

# Calculos
Soma = Primeiro_numero + Segundo_numero
Resultado = Soma / (Primeiro_numero - Segundo_numero)

# Saída
print ("A divisão da soma pela diferença dos numeros é = ", Resultado)