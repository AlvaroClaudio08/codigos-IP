def sistema_ordenacao(jogadores):

#Mais gols marcados.
# Em caso de empate, mais assistências.
# Em caso de novo empate, MENOS cartões vermelhos.
# Se o empate persistir, MENOS cartões amarelos.
# Ainda empatados? Mais passes certos.
# Se o empate persistir, ordem alfabética do nome da Seleção.
# Por fim, ordem alfabética do nome do Jogador.

    lista_jogadores_selecao = list(jogadores.items())

    #(Seleção, Gols, Assistências, Passes Certos, Cartões Amarelos, Cartões Vermelhos)
    for i in range(len(lista_jogadores_selecao)):
        for j in range(len(lista_jogadores_selecao)-1):

            if (lista_jogadores_selecao[j][1][1] < lista_jogadores_selecao[j+1][1][1]
                or lista_jogadores_selecao[j][1][1] == lista_jogadores_selecao[j+1][1][1] and lista_jogadores_selecao[j][1][2] < lista_jogadores_selecao[j+1][1][2]
                or lista_jogadores_selecao[j][1][1] == lista_jogadores_selecao[j+1][1][1] and lista_jogadores_selecao[j][1][2] == lista_jogadores_selecao[j+1][1][2] and lista_jogadores_selecao[j][1][5] > lista_jogadores_selecao[j+1][1][5]
                or lista_jogadores_selecao[j][1][1] == lista_jogadores_selecao[j+1][1][1] and lista_jogadores_selecao[j][1][2] == lista_jogadores_selecao[j+1][1][2] and lista_jogadores_selecao[j][1][5] == lista_jogadores_selecao[j+1][1][5] and lista_jogadores_selecao[j][1][4] > lista_jogadores_selecao[j+1][1][4]
                or lista_jogadores_selecao[j][1][1] == lista_jogadores_selecao[j+1][1][1] and lista_jogadores_selecao[j][1][2] == lista_jogadores_selecao[j+1][1][2] and lista_jogadores_selecao[j][1][5] == lista_jogadores_selecao[j+1][1][5] and lista_jogadores_selecao[j][1][4] == lista_jogadores_selecao[j+1][1][4] and lista_jogadores_selecao[j][1][3] < lista_jogadores_selecao[j+1][1][3]
                or lista_jogadores_selecao[j][1][1] == lista_jogadores_selecao[j+1][1][1] and lista_jogadores_selecao[j][1][2] == lista_jogadores_selecao[j+1][1][2] and lista_jogadores_selecao[j][1][5] == lista_jogadores_selecao[j+1][1][5] and lista_jogadores_selecao[j][1][4] == lista_jogadores_selecao[j+1][1][4] and lista_jogadores_selecao[j][1][3] == lista_jogadores_selecao[j+1][1][3] and lista_jogadores_selecao[j][1][0] > lista_jogadores_selecao[j+1][1][0]
                or lista_jogadores_selecao[j][1][1] == lista_jogadores_selecao[j+1][1][1] and lista_jogadores_selecao[j][1][2] == lista_jogadores_selecao[j+1][1][2] and lista_jogadores_selecao[j][1][5] == lista_jogadores_selecao[j+1][1][5] and lista_jogadores_selecao[j][1][4] == lista_jogadores_selecao[j+1][1][4] and lista_jogadores_selecao[j][1][3] == lista_jogadores_selecao[j+1][1][3] and lista_jogadores_selecao[j][1][0] == lista_jogadores_selecao[j+1][1][0] and lista_jogadores_selecao[j][0] > lista_jogadores_selecao[j+1][0]
            ):
                
                lista_jogadores_selecao[j], lista_jogadores_selecao[j+1] = lista_jogadores_selecao[j+1], lista_jogadores_selecao[j]

    return lista_jogadores_selecao

operacao = input()
time = {}

while operacao != "*FIM":

    operacao = operacao.split()

    #Formato: *ADD jogador seleção gols assistencias passes_certos amarelos vermelhos    
    if operacao[0] == "*ADD":
        

        dados_string = " ".join(operacao[2:])
        dados_string = dados_string.split()


        dados = []
        for cada in dados_string:

            if cada.isnumeric():
                cada = int(cada)
            
            dados.append(cada)

        dados = tuple(dados)

        if operacao[1] not in time:

            time[operacao[1]] = dados

        elif operacao[1] in time:
            
            if operacao[1] in time and operacao[2] in time[operacao[1]]:

                atualizacao = [operacao[2]]

                for i in range(1, len(dados)):
                    atualizacao.append(dados[i] + time[operacao[1]][i])

                time[operacao[1]] = atualizacao

            else:

                time[operacao[1]] = dados
    
    #Formato: *DEL jogador seleção
    elif operacao[0] == "*DEL":

        op_delete = operacao[1:]
        op_delete = tuple(op_delete)
        combinacao_invalida = True

        while combinacao_invalida:

            if op_delete[0] in time:

                if op_delete[1] in time[op_delete[0]]:
                    combinacao_invalida = False

            if combinacao_invalida:
                op_delete = input()

        removido = time.pop(op_delete[0])
    
    #Formato: *BUSCAR jogador selecao
    elif operacao[0] == "*BUSCAR":

        if operacao[1] not in time:

            if operacao[1] == "Neymar":
                print("E o pessoal tá lá: 'será que Carlo Ancelotti vai convocar o Neymar?'")

            else:
                print(f"Jogador não encontrado na seleção {operacao[2]}")

        else:

            jogador = operacao[1]
            selecao = operacao[2]
            i = 1
            g, a, p, ca, cv = time[jogador][1], time[jogador][2], time[jogador][3], time[jogador][4], time[jogador][5]

            print(f"{jogador} ({selecao}): {g}G, {a}A, {p}P, {ca}CA, {cv}CV")

    #Formato: *DESTAQUE_SELECAO selecao
    elif operacao[0] == "*DESTAQUE_SELECAO":

        jogadores_selecao = {}

        for jogador in time:
            
            if operacao[1] == time[jogador][0]:
                jogadores_selecao[jogador] = time[jogador]

        if len(jogadores_selecao) == 0:
            
            print(f"Nenhum dado encontrado para a seleção {operacao[1]}")

        else:
             #(Seleção, Gols, Assistências, Passes Certos, Cartões Amarelos, Cartões Vermelhos)

            jogadores_ordenados = sistema_ordenacao(jogadores_selecao)

            dados = jogadores_ordenados[0]
            jogador = dados[0]
            g, a = dados[1][1], dados[1][2]

            print(f"Destaque da {selecao}: {jogador} {g} gols, {a} assistências")

    elif operacao == "*BOLA_DE_OURO":

        if len(time) == 0:
            
            print("Nenhum jogador registrado no torneio")
        
        else:
            
            jogadores_ordenados = sistema_ordenacao(time)

            dados = jogadores_ordenados[0]
            jogador = dados[0]
            selecao = dados[1][0]
            g = dados[1][1]

            print(f"Bola de Ouro atual: {jogador} {selecao} com {g} gols")

    elif operacao == "*FIM":

        if len(time) == 0:

            print("Nenhum jogador registrado para o ranking final.")

        else:
            #(Seleção, Gols, Assistências, Passes Certos, Cartões Amarelos, Cartões Vermelhos)

            jogadores_ordenados = sistema_ordenacao(time)

            for cada in jogadores_ordenados:

                jogador = cada[0]
                selecao = cada[1][0]
                g, a, p, ca, cv = cada[1][1], cada[1][2], cada[1][3], cada[1][4], cada[1][5]

                print(f"{jogador} ({selecao}) - G: {g}, A: {a}, P: {p}, CA: {ca}, CV: {cv}")

    operacao = input()

