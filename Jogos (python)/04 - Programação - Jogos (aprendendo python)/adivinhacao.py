import random

def jogar():

    print("***********************************")
    print("*Bem vindo ao jogo de Adivinhação!*")
    print("***********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    nivel = 0



    while (nivel != 1 and nivel !=2 and nivel != 3):
        print("Qual o nivel de dificuldade? ")
        print("(1)Fácil (2)Médio (3)Difícil")
        nivel = int(input("Defina o nível: "))

        if (nivel == 1):
            print("Nivel facil escolhido")
            total_de_tentativas = 20
            break
        elif (nivel == 2):
            print("Nivel medio escolhido")
            total_de_tentativas = 10
            break
        elif (nivel == 3):
            print("Nivel dificil escolhido")
            total_de_tentativas = 5
            break
        else:
            print("numero invalido")
            continue


    for rodada in range (1, total_de_tentativas + 1 ):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        menor   = numero_secreto > chute
        maior   = numero_secreto < chute

        if (acertou):
            print("você acertou e fez {} pontos!".format(pontos) )
            break
        else:
            if (menor):
                print("você errou, tente um numero maior")
            elif (maior):
                print("você errou, tente um numero menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()