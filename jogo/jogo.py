import ganhar
import desenho
import saudacao
import random
import jogador


def jogar():

    saudacao.boas_vindas()

    todas_casas = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

    jogador1_ganhou = False
    jogador2_ganhou = False

    jogadas = random.randrange(0, 2)

    if jogadas == 0:
        total_de_rodadas = 8
    else:
        total_de_rodadas = 9

    todas_jogadas_jogador1 = set({})
    todas_jogadas_jogador2 = set({})

    desenho.desenha_jogo(todas_casas)

    while jogadas <= total_de_rodadas or jogador1_ganhou is True or jogador2_ganhou is True:

        if jogadas % 2 == 0:
            jogador.vez_playx(todas_casas, todas_jogadas_jogador1)
        else:
            jogador.vez_playo(todas_casas, todas_jogadas_jogador2)

        desenho.desenha_jogo(todas_casas)

        jogador1_ganhou = ganhar.todas_verificacoes(todas_jogadas_jogador1, jogador1_ganhou)
        jogador2_ganhou = ganhar.todas_verificacoes(todas_jogadas_jogador2, jogador2_ganhou)

        if jogador1_ganhou:
            print("Jogador X venceu!")
            break
        elif jogador2_ganhou:
            print("Jogador O venceu!")
            break

        jogadas += 1

        if jogadas > total_de_rodadas:
            print("Deu empate entre os dois jogadores.")

    print("Fim de jogo!")


if __name__ == '__main__':
    jogar()
