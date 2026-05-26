def sistema_ordenacao(jogador, time, selecao="qualquer"):
    if selecao != "qualquer":
        
        jogadores_selecao = {}

        for jogador in time:
            
            if selecao == time[jogador][0]:
                jogadores_selecao[jogador] = time[jogador]

        lista_jogadores_selecao = list(jogadores_selecao.items())

        for i in range(len(lista_jogadores_selecao)):
            for j in range(len(lista_jogadores_selecao)-1):

                if lista_jogadores_selecao[0][j]

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

    elif operacao[0] == "":

        
                    






    operacao = input()

