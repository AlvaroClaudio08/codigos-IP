print("Conexão CBF e CIn-UFPE estabelecida! Processando os dados da convocação rumo ao Hexa...")

vagas = int(input())

if vagas == 0:

    print("Vixe, zero vagas? Parece que a panela já ta formada e o mister já tem os 26 nomes na cabeça.")

else:

    jogadores = {}
    partida = input()

    while partida != "A coletiva vai começar":

        partida = partida.split(" ", 1)
        dados = partida[1]
        dados = dados.split(" - ")
        partida = input()
        print(dados)



