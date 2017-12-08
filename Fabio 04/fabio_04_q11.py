def main():

	# Leia informações de alunos (matrícula, nota1, nota2, nota3) com o fim das informações indicado por matrícula = 0.

	matricula = 1
	nota1 = None
	nota2 = None
	nota3 = None
	aprovado = 0
	reprovado = 0

	while matricula != 0 :

		matricula = int(input('Digite a matricula: '))
		
		if matricula != 0 :
			
			nota1 = float(input('Digite a primeira nota: '))
			nota2 = float(input('Digite a segunda nota: '))
			nota3 = float(input('Digite a terceira nota: '))

			media_final = ((2 * nota1) + (3 * nota2) + (5 * nota3)) / 10
			
			if media_final >= 7 :
				aprovado += 1
		
			else :
				reprovado += 1
	
	print('O total de aprovados é igual a: %d' % aprovado)
	print('O total de reprovados é igual a: %d' % reprovado)

	 # Para cada aluno deve ser calculada a média final de acordo com a seguinte fórmula: Média Final =   (2 * nota1) + (3 * nota2) + (5 * nota3) 10.
	 # Se a média final for igual ou superior a 7, o aluno está  aprovado; se a média final for inferior a 7, o aluno está reprovado. Ao final devem ser mostrados o total de aprovados, o total de reprovados e o total de alunos da turma. 

if __name__ == '__main__':
	main()