todos_jogos = []
gols_brasil = []

for i in range(6):
    jogo = input()

    casa, visitante = jogo.split(" x ")

    selecao_casa, gols_casa = casa.rsplit(" ", 1)
    gols_visitante, selecao_visitante = visitante.split(" ", 1)

    jogo = (
        selecao_casa,
        int(gols_casa),
        int(gols_visitante),
        selecao_visitante
    )

    todos_jogos.append(jogo)

    if jogo[0] == "Brasil" or jogo[3] == "Brasil":
        cont = 0
        valido = False

        if jogo[0] == "Brasil":
            posicao = 1
            if jogo[1] >= 1:
                valido = True
        elif jogo[3] == "Brasil":
            posicao = 2
            if jogo[2] >= 1:
                valido = True

        if valido:

            gols = input().rsplit(" ", 1)
            gols[1] = int(gols[1])
            gols = tuple(gols)

            gols_brasil.append(gols)
            cont += gols[1]

            while jogo[posicao] > cont:

                gols = input().rsplit(" ", 1)
                gols[1] = int(gols[1])
                gols = tuple(gols)

                gols_brasil.append(gols)
                cont += gols[1]

estatisticas_paises = {}

for jogo in todos_jogos:

    if jogo[0] not in estatisticas_paises:
        estatisticas_paises[jogo[0]] = {
            'pontos': 0,
            'vitorias': 0, 
            'derrotas': 0, 
            'empates': 0, 
            'saldo': 0
        }

    if jogo[3] not in estatisticas_paises:
        estatisticas_paises[jogo[3]] = {
            'pontos': 0,
            'vitorias': 0, 
            'derrotas': 0, 
            'empates': 0, 
            'saldo': 0
        }

    if jogo[1] > jogo[2]:
        estatisticas_paises[jogo[0]]['pontos'] += 3
        estatisticas_paises[jogo[0]]['vitorias'] += 1
        
        estatisticas_paises[jogo[3]]['derrotas'] += 1

    elif jogo[1] == jogo[2]:
        estatisticas_paises[jogo[0]]['pontos'] += 1
        estatisticas_paises[jogo[0]]['empates'] += 1

        estatisticas_paises[jogo[3]]['pontos'] += 1
        estatisticas_paises[jogo[3]]['empates'] += 1

    else:
        estatisticas_paises[jogo[3]]['pontos'] += 3
        estatisticas_paises[jogo[3]]['vitorias'] += 1

        estatisticas_paises[jogo[0]]['derrotas'] += 1

    estatisticas_paises[jogo[0]]['saldo'] += jogo[1] - jogo[2]
    estatisticas_paises[jogo[3]]['saldo'] += jogo[2] - jogo[1]

lista_estatisticas = list(estatisticas_paises.items())

for i in range(len(lista_estatisticas)):
    for j in range(len(lista_estatisticas)-1):

        if (
            lista_estatisticas[j][1]['pontos'] < lista_estatisticas[j+1][1]['pontos']
            or lista_estatisticas[j][1]['pontos'] == lista_estatisticas[j+1][1]['pontos'] and lista_estatisticas[j][1]["saldo"] < lista_estatisticas[j+1][1]["saldo"]
            or lista_estatisticas[j][1]['pontos'] == lista_estatisticas[j+1][1]['pontos'] and lista_estatisticas[j][1]["saldo"] == lista_estatisticas[j+1][1]["saldo"] and lista_estatisticas[j][0] > lista_estatisticas[j+1][0]
        ):
            
            lista_estatisticas[j], lista_estatisticas[j+1] = lista_estatisticas[j+1], lista_estatisticas[j]

ordenado = {}

for selecao, dados in lista_estatisticas:
    ordenado[selecao] = dados

i = 1
print("------- Grupo C -------")
for pais in ordenado:

    if i < 5:

        pontos = ordenado[pais]["pontos"]
        V = ordenado[pais]["vitorias"]
        D = ordenado[pais]["derrotas"]
        E = ordenado[pais]["empates"]
        SG = ordenado[pais]["saldo"]

        print(f"{i}º | {pais} | {pontos} | {V} | {D} | {E} | {SG}")

    if pais == "Brasil":
        posicao_brasil = i

    i += 1

print()
gols_marcados = {}
for gol in gols_brasil:

    if gol[0] not in gols_marcados:
        gols_marcados[gol[0]] = gol[1]
    
    else:
        gols_marcados[gol[0]] += gol[1]

quant_gols_brasil = 0
for gol in gols_marcados:
    
    quant_gols_brasil += gols_marcados[gol]

gols_sofridos = quant_gols_brasil - ordenado["Brasil"]["saldo"]

lista_gols = list(zip(gols_marcados.keys(), gols_marcados.values()))

for i in range(len(lista_gols)):
    for j in range(len(lista_gols)-1):

        if lista_gols[j][1] < lista_gols[j+1][1]:
            lista_gols[j], lista_gols[j+1] = lista_gols[j+1], lista_gols[j]

print("-- Desempenho Brasileiro --")
print(f"Posição: {posicao_brasil}")
print(f"Gols Marcados: {quant_gols_brasil}")
print(f"Gols Sofridos: {gols_sofridos}")

if len(gols_brasil) >= 1:
    for gol in gols_marcados:
        print(f"{gol}: {gols_marcados[gol]}")

    print(f"Artilheiro: {lista_gols[0][0]}")