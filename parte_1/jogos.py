import adivinhacao
import forca


def jogos():
    print()
    print("*******************")
    print("Olá, seja bem vindo")
    print("*******************")
    print()
    print("Escolha o jogo que deseja, (1) Adivinhação ou (2) Forca")
    jogo = int(input())

    if jogo == 1:
        print("Você entrou no jogo de Adivinhação")
        print()
        adivinhacao.jogar()
    elif jogo == 2:
        print("Você entrou no jogo da Forca")
        print()
        forca.jogar()
    else:
        print("Número digitado inválido")


if __name__ == "__main__":
    jogos()

# Utilizando o format para substituir as chaves pelos valores,
# podendo utilizar qualquer string nos parâmetros do format
# print("Total de tentativas {} de {}".format(1, 2))

# Utilizando for para fazer o loop, nesse for é utilizado a funcao range
# para iterar do ponto inicial até o final
# primeiro parâmetro define o ponto de partida, segundo parâmetro define
# o final e o terceiro parâmetro define quantas casas será pulado em cada iteração
# for posicao in range(1, 10, 2):
#     print(posicao)

# Outro exemplo utilizando range é colocar no parâmetro uma sequência de iteração
# for seq in [1, 2, 3, 4, 5]:
#     print(seq)

# Pegar um número randômico
# random.random()
# nr = random.random() * 100
# print(nr)

# Arredondando o resultado
# print(round(nr))

# Nem sempre é possível arredondar o resultado de um número randômico,
# já que é possível que o resultado seja 0, na doc do random explica
# que ele pode retornar valores entre 0.0 e 1.0, sendo assim, caso venha
# 0 o round não consegue arredondar e lança uma exceção

# Sendo assim, existe uma função dentro de random que seria o randrange(),
# nele podemos definir uma série de números que podem vir

# O randrange() também aceita 3 parâmetros bem parecido com a função range()
# rr = random.randrange(1, 101)
# print(rr)
