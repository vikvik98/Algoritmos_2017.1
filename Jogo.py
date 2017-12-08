import random
def main():

	input("Bem-vindo ao mundo em que você não desejaria estar...")
	nome = input("Me diga seu nome. \n")
	input("Você está em um caminho sem volta, %s." % nome)
	input("Agora vamos definir a sua classe. Escolha entre um guerreiro ou um mago.")
	classe = input("Qual será sua classe? \n")

	if classe == "guerreiro":
		vida = 100
		mana = 50
	if classe == "mago":
		vida = 50 
		mana = 100

	input("Humm... Então você é um %s..." % classe)
	input("Tenho pena da sua alma. HAHAHAHA!!!")
	input("Agora que você é um %s, devo-lhe informar o quanto você tem de vida e de mana." % classe)
	input("Sua vida é: %d e sua mana é: %d" % (vida, mana))
	input("É melhor administrar bem sua vida e sua mana se não vai morrer mais depressa. HEHEHEHE!!!")
	input("Vamos começar com a sua jornada...")
	input("Faça um movimento sendo que 'w' você vai para frente, 's' volta para aonde você estava, 'a' você vai para esquerda e 'd' você vai para a direita")
	input("Faça seu movimento sabiamente. Então, para aonde deseja ir?")
	movitentação(vida,mana)


	

def movitentação(vida,mana):
	direcional = input("Informe para qual direção deseja ir:\n")

	if direcional == "w":
		input("Humm... Você acabou de entrar na floresta proibida, tome cuidado com os perigos que ela oferece.")
	elif direcional == "s":
		input("Então que dizer que você quer voltar para a casa? HAHAHAHA... Como eu disse, você entrou em um caminho sem volta...")
		input("Vou lhe punir por tentar voltar.")
		dano = random.randrange(0,10)
		input("O dano que eu vou lhe dar será de %d" % dano)
		input("Recebaaaa...")
		vida = vida - dano
		input("Agora você tem %d pontos de vida. HAHAHAHA..." % vida)
	elif direcional == "a":
		input("Humm... Você descobriu um item que aumenta a mana.")
		item_mana = random.randrange(1,10)
		mana = mana + item_mana
		input("Sua nova mana é: %d" % mana)
		input("Aproveite a sorte enquanto está com ela. HAHAHAHA...")
	elif direcional == "d":
		input("Você descobriu um item de cura.")
		item_vida = random.randrange(1,10)
		vida = vida + item_vida
		input("Agora sua vida tem %d pontos." % vida)
		input("Espero que sua sorte não mude derepente... HAHAHAHHA...")
	else:
		input("Você digitou algo errado...")
		input("Vou lhe matar por sua burrice. :)")
		input("Game Over.")
				
		

if __name__ == '__main__':
	main()
