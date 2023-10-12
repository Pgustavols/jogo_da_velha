
def verifica_se_ganhou_vertical(jogadas, ganhador):
    if "a1" in jogadas and "a2" in jogadas and "a3" in jogadas:
        ganhador = True
    elif "b1" in jogadas and "b2" in jogadas and "b3" in jogadas:
        ganhador = True
    elif "c1" in jogadas and "c2" in jogadas and "c3" in jogadas:
        ganhador = True

    return ganhador


def verifica_se_ganhou_horizotal(jogadas, ganhador):
    if "a1" in jogadas and "b1" in jogadas and "c1" in jogadas:
        ganhador = True

    elif "a2" in jogadas and "b2" in jogadas and "c2" in jogadas:
        ganhador = True

    elif "a3" in jogadas and "b3" in jogadas and "c3" in jogadas:
        ganhador = True

    return ganhador


def verifica_se_ganhou_diagonal(jogadas, ganhador):
    if "a1" in jogadas and "b2" in jogadas and "c3" in jogadas:
        ganhador = True

    elif "c1" in jogadas and "b2" in jogadas and "a3" in jogadas:
        ganhador = True

    return ganhador


def todas_verificacoes(jogadas, ganhador):
    primeira_vericacao = verifica_se_ganhou_vertical(jogadas, ganhador)
    segunda_vericacao = verifica_se_ganhou_horizotal(jogadas, ganhador)
    terceira_vericacao = verifica_se_ganhou_diagonal(jogadas, ganhador)

    ganhador = primeira_vericacao or segunda_vericacao or terceira_vericacao
    return ganhador


