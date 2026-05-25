print("Hoje é o dia da Lobotomia CinCorporation!")
print()
quant_dias = int(input())
   
def malkuth():
    nomes = input()
    falho = False
    if not nomes.strip(): #se a lista nomes está vazia ou contem apenas espaço
        falho = True
    else:
        nomes = nomes.split(" ")

        n = len(nomes)
        for i in range(n):
            for j in range(n - 1):
                if len(nomes[j]) < len(nomes[j+1]):
                    nomes[j], nomes[j+1] = nomes[j+1], nomes[j]

        energia = (len(nomes[0]) + len(nomes[n-1]))*20
   
    return falho, energia

def yesod():
    compressao = []
    caracteres = input()
    caracteres = list(caracteres)
    caracteres.append(".")
    caracteres = "".join(caracteres)
    anterior = ""
    falho = False
    nc = []
   
    for c in range(len(caracteres)):
        if caracteres[c] == "&":
            falho = True
            if anterior == "":
                compressao_str = ""
            else:
                nc = [quant_cada, anterior]
                compressao.append(nc)

        if not falho:
            
            if caracteres[c] == anterior:
                quant_cada += 1
           
            else:
                if anterior != "":
                   
                    if quant_cada == 1:
                        nc = [caracteres[c - 1]]
                        compressao.append(nc)
                    
                    else:
                        nc = [quant_cada, anterior]
                        compressao.append(nc)

                quant_cada = 1
                anterior = caracteres[c]

    compressao_str = ""

    for lista in compressao:
        for elemento in lista:
            elemento = str(elemento)
            compressao_str += elemento

    return compressao_str

def binah():
    matriz_A = []
    for i in range(3):
        linhaA = int(input())
        linhaA = linhaA.split(" ")
        matriz_A.append(linhaA)

    matriz_B = []
    for j in range(3):
        linhaB = int(input())
        linhaB = linhaB.split(" ")
        matriz_B.append(linhaB)
    return matriz_A, matriz_B

matriz_A, matriz_B = binah()
