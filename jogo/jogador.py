def vez_playx(todas_casas, todas_jogadas_jogador1):
    playx = input("Jogador X informe a casa que você quer jogar: ").strip().lower()
    for index in range(0, len(todas_casas)):
        if playx == todas_casas[index]:
            todas_casas[index] = "X "
    todas_jogadas_jogador1.add(playx)

def vez_playo(todas_casas, todas_jogadas_jogador2):
    playo = input("Jogador O informe a casa que você quer jogar: ").strip().lower()
    for index in range(0, len(todas_casas)):
        if playo == todas_casas[index]:
            todas_casas[index] = "O "
    todas_jogadas_jogador2.add(playo)