def computador_escolhe_jogada(n, m):
    jogada = False
    i = 1

    while (jogada == False and i != m):
        total = n-i
        if (total % (m+1) == 0 and total >= 0):
            pecas = i
            jogada = True
        else:
            i = i + 1

    if (i == m):
        pecas = m

    return pecas


def usuario_escolhe_jogada(n, m):
    jogada = False

    while (jogada == False):
        pecas = int(input("Quantas peças você vai tirar? "))
        if (pecas <= m and pecas <= n and n - pecas >= 0 and pecas > 0):
            jogada = True
        else:
            print("Opção Inválida! Tente novamente.")
    return pecas


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if (n % (m+1) == 0):
        jogador = 1  # o jogador será o usuário
        print("Você começa!")
    else:
        jogador = 2  # o jogador será o computador
        print("O computador começa!")
    while (n != 0):
        if (jogador == 1):
            pecasRemovidas = usuario_escolhe_jogada(n, m)
            print("Voce tirou " + str(pecasRemovidas) + " peças.")
            jogador = 2
        else:
            pecasRemovidas = computador_escolhe_jogada(n, m)
            print("O computador tirou " + str(pecasRemovidas) + " peças.")
            jogador = 1
        n = n - pecasRemovidas
        print("Agora restam " + str(n) + " peças no tabuleiro.")
    if (jogador == 1):
        jogador = 2
        print("Fim do jogo! O computador ganhou!")
    else:
        jogador = 1
        print("Fim do jogo! Você ganhou!")
    return jogador


def campeonato():
    print("Voce escolheu um campeonato!")
    usuario = 0
    computador = 0
    rodada = 1
    while (rodada <= 3):
        print("***** RODADA " + str(rodada) + " *****")
        if (partida() == 1):
            usuario = usuario + 1
        else:
            computador = computador + 1
        rodada = rodada + 1
    print("Placar: Você " + str(usuario) +
          " X " + str(computador) + " Computador")


def main():
    print("Bem vinda(o) ao jogo do NIM.")
    print("[1] Jogar apenas uma partida isolada")
    print("[2] Jogar apenas um campeonato")
    opcao = int(input("Insira a opção desejada: "))

    if (opcao == 1):
        print("Voce escolheu uma partida isolada!")
        partida()
    else:
        campeonato()


main()
