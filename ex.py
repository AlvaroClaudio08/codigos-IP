quant_sois = int(input())
plantas_combatentes = []
#nome - 0, vida = 1, velocidade = 2 posição = 3
sobreZumbi = ["", 10, 2, 18]
sobrePlantas = []
fim = False

def compra_plantas(quant_sois, fim, plantas_combatentes):
    print("O quintal está sendo invadido! Prepare a melhor linha de defesa possível!")
    planta = input()

    while planta != "FIM" and not fim:
        #nome = 0, vida = 1, dano = 2
        nova_planta = []
        if planta == "Disparervilha":
            if quant_sois >= 50:
                nova_planta.append("Disparervilha")
                nova_planta.append(1)
                nova_planta.append(1)
                plantas_combatentes.append(nova_planta)
                quant_sois -= 50
            else:
                print("Você não tem sóis suficientes para isso!")

        elif planta == "Gelervilha":
            if quant_sois >= 100:
                nova_planta.append("Gelervilha")
                nova_planta.append(1)
                nova_planta.append(1)
                plantas_combatentes.append(nova_planta)
                quant_sois -= 100
            else:
                print("Você não tem sóis suficientes para isso!")

        elif planta == "Noz-Obstáculo":
            if quant_sois >= 75:
                nova_planta.append("Noz-Obstáculo")
                nova_planta.append(2)
                nova_planta.append(0)
                plantas_combatentes.append(nova_planta)
                quant_sois -= 75
            else:
                print("Você não tem sóis suficientes para isso!")

        if len(plantas_combatentes) == 18:
            fim = True
        planta = input()

#zumbi
#nome - 0, vida = 1, velocidade = 2 posição = 3
#planta
#nome = 0, vida = 1, dano = 2
def zumbi(sobreZumbi):
    tipo_zumbi = input()
    if tipo_zumbi == "Zumbi Normal":
        sobreZumbi[0] = "Zumbi Normal"
        sobreZumbi[1] = 10
        sobreZumbi[2] = 2
        sobreZumbi[3] = 18
    if tipo_zumbi == "Zumbi Cabeça-de-Cone":
        sobreZumbi[0] = "Zumbi Cabeça-de-Cone"
        sobreZumbi[1] = 14
        sobreZumbi[2] = 2
        sobreZumbi[3] = 18
    if tipo_zumbi == "Zumbi do Jornal":
    #fazer verificação na batalha pra saber se é ele pra poder aumentar a velocidade depois que tiver com a vida com menos da metade
        sobreZumbi[0] = "Zumbi do Jornal"
        sobreZumbi[1] = 10
        sobreZumbi[2] = 2
        sobreZumbi[3] = 18
    if tipo_zumbi == "Zumbi Saltador":
    #fazer verificação pra saber se é ele, se for ele vai poder pular o noz_obstáculo
        sobreZumbi[0] = "Zumbi Saltador"
        sobreZumbi[1] = 10
        sobreZumbi[2] = 2
        sobreZumbi[3] = 18

def batalha(sobreZumbi):
#nome - 0, vida = 1, velocidade = 2 posição = 3
    #enquanto o zumbi não morre e não chega na casa
    compra_plantas(quant_sois, fim, plantas_combatentes)
    zumbi(sobreZumbi)
    metadinha = False
    morteZumbi = False
    print("Lá vem o zumbi... espero que suas plantas estejam preparadas!")

    while not morteZumbi and sobreZumbi[3] > 0:

        for i in range(len(plantas_combatentes)):
            sobreZumbi[1] -= plantas_combatentes[i][2]
            
            if plantas_combatentes[i][0] == "Gelervilha":
                sobreZumbi[2] -= 1
                
                if sobreZumbi[2] < 1:
                    sobreZumbi[2] = 1
                
                if metadinha:
                    if sobreZumbi[2] < 2:
                        sobreZumbi[2] == 2

        if sobreZumbi[1] <= 0:
            morteZumbi = True

        if not morteZumbi:

            if sobreZumbi[0] == "Zumbi do Jornal":
                
                if sobreZumbi[1] <= 5 and not metadinha:
                    sobreZumbi[2] += 1
                    metadinha = True
            

            #PARTE QUE O ZUMBI VAI TENTAR ANDAR ATÉ O FINAL
            n = 0
            achou = False
            #verifica quantos passos ele vai dar e anda um por um, se tiver alguma planta nesse índice, ele para e ataca
            while  n != sobreZumbi[2] and not achou:
                #se a posição da planta for na mesma posição do zumbi
                if len(plantas_combatentes) - 1 == sobreZumbi[3]:
                    indice = sobreZumbi[3] - 1
                    plantas_combatentes[indice][1] -= 1
                    #se conseguiu comer a planta ele pega a posição dela
                    if plantas_combatentes[indice][1] == 0:
                        print("NOMNOMNOM!")
                        sobreZumbi[3] -= 1
                        achou = True

                else:
                    #zumbi vai andar as proximas posições
                    prox_posicao = sobreZumbi[3] - 1
                    #se a posição na frente do zumbi tiver alguma planta
                    if len(plantas_combatentes) - 1 == prox_posicao:

                        achou = True
                        if prox_posicao - 1 >= 0:
                            indice = prox_posicao - 1

                        if 0 <= prox_posicao < len(plantas_combatentes):
                            if plantas_combatentes[prox_posicao ][0] == "Noz-Obstáculo":
                                #ignora a posição
                                sobreZumbi[3] = prox_posicao
                                remover = plantas_combatentes.pop(prox_posicao)


                        plantas_combatentes[indice][1] -= 1
                        #se conseguiu destruir a planta
                        if plantas_combatentes[indice][1] == 0:
                            remover = plantas_combatentes.pop(indice)
                            print("NOMNOMNOM!")

                    n += 1
                    sobreZumbi[3] = prox_posicao

    if sobreZumbi[3] == 0:
        print("O zumbi chegou à porta! Você perdeu!")

    if morteZumbi:
        print("Bom trabalho! Dave Doidão nunca esteve tão feliz...")

          
batalha(sobreZumbi)

