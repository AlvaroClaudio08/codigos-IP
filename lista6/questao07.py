def partidas():

    jogadores = {}
    partida = input()

    while partida != "A coletiva vai começar":
        
        partida = partida.split(" ", 1)
        todos_dados = partida[1]
        todos_dados = todos_dados.split(" - ")
        jogador, dados = todos_dados[0], todos_dados[1:]

        dados = tuple([int(i) for i in dados])

        if jogador not in jogadores:
            jogadores[jogador] = dados
        
        elif jogador in jogadores:
            #(Total_Gols, Total_Assistencias, Total_Dribles, Total_Lesoes).

            antigo = jogadores[jogador]

            atualizada = (antigo[0] + dados[0], antigo[1] + dados[1], antigo[2] + dados[2], antigo[3] + dados[3])

            jogadores[jogador] = atualizada

        partida = input()

    return jogadores

def convocacao():

    



print("Conexão CBF e CIn-UFPE estabelecida! Processando os dados da convocação rumo ao Hexa...")

vagas = int(input())

if vagas == 0:

    print("Vixe, zero vagas? Parece que a panela já ta formada e o mister já tem os 26 nomes na cabeça.")

else:

    jogadores = partidas()

    while len(jogadores) == 0:
        
        print("Ue, a coletiva começou mas ninguém foi analisado? O professor vai convocar os gandulas?")
        jogadores = partidas()

convocacao()

