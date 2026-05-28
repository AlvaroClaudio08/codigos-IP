def partidas():

    jogadores = {}
    partida = input()

    while partida != "A coletiva vai começar":
        
        partida = partida.split(" ", 1)
        todos_dados = partida[1]
        todos_dados = todos_dados.split(" - ")
        jogador, dados = todos_dados[0], todos_dados[1:]

        dados = tuple([int(i) for i in dados])

        if jogador == "Neymar":
            
            if dados[3] == 0:

                print("O homem jogou! A esperanca do hexa respira.")

            else:

                print("Neymar machucou... Mas deixa ele recuperar, na Copa ele decide!")

        else:

            if dados[3] != 0:

                print(f"Ih, {jogador} foi pro estaleiro. Ancelotti ta preocupado.")

            else:

                if jogador in jogadores:

                    print(f"Mais um jogo pra conta de {jogador}.")

                else:

                    print(f"Vamos ver o que Ancelotti achará de {jogador}.")

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

    print()

jogadores_ordenados = convocacao(jogadores)

print("--- CONVOCADOS PARA O HEXA ---")

regulador = 0
contador = 1
neymar_on = False

for player in jogadores_ordenados:

    if n < vagas:

        dados = jogadores_ordenados[player]
        #(Total_Gols, Total_Assistencias, Total_Dribles, Total_Lesoes).

        #Base: (Gols * 5) + (Assistências * 3) + (Dribles * 1) - (Lesões * 10)
        if player == "Neymar":

            neymar_on = True

            score = 20 + dados[0]*5 + dados[1]*3 + dados[2] - dados[3]

        else:

            score = dados[0]*5 + dados[1]*3 + dados[2] - dados[3]*10

        print(f"{n+1}. {player} - {score} pts (G: {dados[0]}, A: {dados[1]})")

        n += 1

if neymar_on:

    print("Prepara o pagode e a caixa de som, o Ney ta on!")

else:

    print("Eita... Ancelotti bancou a tática e deixou o menino Ney de fora!")

if n+1 < vagas:

    if neymar_on:

        print("A lista não encheu, mas com o camisa 10 lá dentro, Ancelotti já tá com a cabeça no Hexa.")

    else: 
        
        print("Se liga, professor... ainda tem espaço pra o Ney!")