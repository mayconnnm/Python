import random


def jogar():
    numero_secreto = random.randrange(1, 101)

    print("Qual nível de dificuldade deseja?")
    print("(1) Fácil, (2) Médio e (3) Difícil")
    nivel = int(input())

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    elif nivel == 3:
        tentativas = 5
    else:
        print("Opção inválida, fim de jogo")
        exit(0)

    for r in range(tentativas):
        print("Digite um número")
        numero = int(input())

        if numero == numero_secreto:
            print("Você acertou!")
            break
        else:
            if numero > numero_secreto:
                print("Seu chute foi maior que o número secreto")
            elif numero < numero_secreto:
                print("Seu chute foi menor que o número secreto")

    print("Fim de jogo")


if __name__ == "__main__":
    jogar()
