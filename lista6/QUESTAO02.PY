print("Somente o melhor deve ser lembrado")

jogador_Clube = input()
competidor = {}

ranking = ("França", "Espanha", "Argentina", "Inglaterra", "Portugal", "Brasil", "Holanda", "Marrocos", "Bélgica", "Alemanha", "Croácia", "Colômbia", "Senegal", "México", "Estados Unidos", "Uruguai", "Japão", "Suíça", "Irã", "Turquia", "Equador", "Áustria", "Coreia Do Sul", "Australia", "Argélia", "Egito", "Canadá", "Noruega", "Panamá", "Costa Do Marfim", "Suécia", "Paraguai", "Tchéquia", "Escócia", "Tunísia", "Républica Democrática Do Congo", "Uzbequistão", "Catar", "Iraque", "Africa Do Sul", "Arábia Saudita", "Jordânia", "Bósnia-Herzgovina", "Cabo Verde", "Gana", "Curaçao", "Haiti", "Nova Zelândia")

top1 = ("jogador", "clube", 997,  -1)
top2 = ("jogador", "clube", 998, -2)
top3 = ("jogador", "clube", 999, -3)

while jogador_Clube != "FIM":
    jogador, clube = jogador_Clube.split(" - ")

    if clube not in competidor:
       
        competidor[clube] = {}

    if jogador in competidor[clube]:
        competidor[clube][jogador] += 1

    else:
        competidor[clube][jogador] = 1

    jogador_Clube = input()

indice_pais = 0
for pais in ranking:

    if pais in competidor:

        for jogador in competidor[pais]:
            
            jogador_atual = (jogador, pais, indice_pais, competidor[pais][jogador])

            if (
                jogador_atual[3] > top1[3]
                or jogador_atual[3] == top1[3] and jogador_atual[2] < top1[2]
                or jogador_atual[3] == top1[3] and jogador_atual[2] == top1[2] and jogador_atual[0] < top1[0]
            ):
                top3 = top2
                top2 = top1
                top1 = jogador_atual

            elif (
                jogador_atual[3] > top2[3]
                or jogador_atual[3] == top2[3] and jogador_atual[2] < top2[2]
                or jogador_atual[3] == top2[3] and jogador_atual[2] == top2[2] and jogador_atual[0] < top2[0]
            ):
                top3 = top2
                top2 = jogador_atual

            elif (
                jogador_atual[3] > top3[3]
                or jogador_atual[3] == top3[3] and jogador_atual[2] < top3[2]
                or jogador_atual[3] == top3[3] and jogador_atual[2] == top3[2] and jogador_atual[0] < top3[0]
            ):
                top3 = jogador_atual

    indice_pais += 1

print(f"O artilheiro foi {top1[0]} com {top1[3]} gols")
print(f"Eu poderia falar do {top2[0]} mas ele é somente o primeiro a ser esquecido")
print(f"O {top3[0]} então, nem pensar")
            