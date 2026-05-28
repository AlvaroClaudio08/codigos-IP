def partidas():

    jogadores = {}
    partida = input()

    while partida != "A coletiva vai começar":
        
        partida = partida.split(" ", 1)
        todos_dados = partida[1]
        todos_dados = todos_dados.split(" - ")
        jogador, dados = todos_dados[0], todos_dados[1:]

        dados = tuple([int(i) for i in dados])

        if jogador == "Neymar" and dados[]

        if jogador not in jogadores:
            jogadores[jogador] = dados
        
        elif jogador in jogadores:
            #(Total_Gols, Total_Assistencias, Total_Dribles, Total_Lesoes).

            antigo = jogadores[jogador]

            atualizada = (antigo[0] + dados[0], antigo[1] + dados[1], antigo[2] + dados[2], antigo[3] + dados[3])

            jogadores[jogador] = atualizada

        partida = input()

    return jogadores

def convocacao(jogadores):

    ordenado = {}
    melhor = ((-1, -1, -1, 9999), "z")
    #Base: (Gols * 5) + (Assistências * 3) + (Dribles * 1) - (Lesões * 10)

    for i in range(len(jogadores)):

        for jogador in jogadores:

            dados_atual = (jogadores[jogador], jogador)

            if jogador == "Neymar":

                anceloti_score_atual = 20 + dados_atual[0][0]*5 + dados_atual[0][1]*3 + dados_atual[0][2] - dados_atual[0][3]

                if melhor[1] == "Neymar":

                    anceloti_score_melhor = 20 + melhor[0][0]*5 + melhor[0][1]*3 + melhor[0][2] - melhor[0][3]

                else:

                    anceloti_score_melhor = melhor[0][0]*5 + melhor[0][1]*3 + melhor[0][2] - melhor[0][3]*10

            else: 

                anceloti_score_atual = dados_atual[0][0]*5 + dados_atual[0][1]*3 + dados_atual[0][2] - dados_atual[0][3]*10

                if melhor[1] == "Neymar":

                    anceloti_score_melhor = 20 + melhor[0][0]*5 + melhor[0][1]*3 + melhor[0][2] - melhor[0][3]

                else:

                    anceloti_score_melhor = melhor[0][0]*5 + melhor[0][1]*3 + melhor[0][2] - melhor[0][3]*10
            
            #criterios:
            # Maior Ancelotti Score.
            # Maior número de Gols totais.
            # Ordem alfabética do nome (A-Z).

            if (anceloti_score_atual > anceloti_score_melhor
                or dados_atual[0][0] > melhor[0][0]
                or dados_atual[1] < melhor[1]
            ):
                
                melhor = dados_atual

        ordenado[melhor[1]] = melhor[0]
        removido = jogadores.pop(melhor[1])

    return ordenado



print("Conexão CBF e CIn-UFPE estabelecida! Processando os dados da convocação rumo ao Hexa...")
print()

vagas = int(input())

if vagas == 0:

    print("Vixe, zero vagas? Parece que a panela já ta formada e o mister já tem os 26 nomes na cabeça.")

else:

    jogadores = partidas()

    while len(jogadores) == 0:
        
        print("Ue, a coletiva começou mas ninguém foi analisado? O professor vai convocar os gandulas?")
        jogadores = partidas()

jogadores_ordenados = convocacao(jogadores)

