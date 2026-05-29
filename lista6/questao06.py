#fase 1 - escalação


convocacao_brasil = {
    'Alisson': [],
    'Ederson': [],
    'Bento': [],
    'Alex Sandro': [],
    'Danilo': [],
    'Douglas Santos': [],
    'Wesley': [],
    'Marquinhos': [],
    'Gabriel Magalhães': [],
    'Bremer': [],
    'Léo Pereira': [],
    'Andrey Santos': [],
    'Bruno Guimarães': [],
    'Casemiro': [],
    'Danilo Santos': [],
    'Fabinho': [],
    'Joelinton': [],
    'Endrick': [],
    'Igor Thiago': [],
    'Gabriel Martinelli': [],
    'João Pedro': [],
    'Neymar': [],
    'Luiz Henrique': [],
    'Matheus Cunha': [],
    'Raphinha': [],
    'Vinícius Júnior': []
}

convocacao_marrocos = {
    'Bounou': [],
    'Munir Mohamedi': [],
    'El Mehdi Benabid': [],
    'Hakimi': [],
    'Mazraoui': [],
    'Aguerd': [],
    'Chadi Riad': [],
    'Yahya Attiat-Allah': [],
    'Abdelkabir Abqar': [],
    'Achraf Dari': [],
    'Ayoub El Amloud': [],
    'Amrabat': [],
    'Ounahi': [],
    'Brahim Díaz': [],
    'Bilal El Khannouss': [],
    'Ismael Saibari': [],
    'Amir Richardson': [],
    'Oussama El Azzouzi': [],
    'Amine Harit': [],
    'Ziyech': [],
    'Amine Adli': [],
    'En-Nesyri': [],
    'Ezzalzouli': [],
    'Soufiane Rahimi': [],
    'Ilias Akhomach': [],
    'Ayoub El Kaabi': []
}


esquema = input().split("-")
esquema = [int(i) for i in esquema]

valido = True
soma = 0

for num in esquema:
    
    if num < 1:
        valido = False
    
    soma += num

if soma != 10:
    valido = False

jogando = {}

for i in range(10):

        


if valido:

