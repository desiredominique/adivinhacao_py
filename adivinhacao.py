import random

def jogo_adivinhacao():

    print("---------------------------------")
    print("Bem vindo ao Jogo de Adivinhação!")
    print("---------------------------------")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0 #esse numero é só o valor de inicialização, não significa que o total seja 0
    pontos = 1000

    print("Qual o nível de dificuldade? Digite (1) para o nível fácil, (2) para o nível médio e (3) para o nível difícil.")

    nivel = int(input("Defina o nível."))

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 1


    for rodada in range (1,total_de_tentativas + 1):
        print("Tentativa {} de {}". format(rodada, total_de_tentativas))
        chute = input("Digite o seu número entre 1 e 100:")
        chute = int(chute)
        print ("Você digitou ", chute)

        if (chute < 1 or chute > 100):
            print ("Você deve digitar um número entre 1 e 100.")
            continue

        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if(acertou):
            print ("Você acertou e fez {} pontos.". format(pontos))
            break
        else:
            if (menor):
                print ("Você errou.", chute, "é menor do que o número secreto.")
            elif (maior):
                print("Você errou.", chute, "é maior do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #exemplo: o abs foi usado para que não dê um numero negativo
            pontos = pontos - pontos_perdidos

    print("Fim do jogo.")

if (__name__ == "__main__"):
    jogo_adivinhacao()