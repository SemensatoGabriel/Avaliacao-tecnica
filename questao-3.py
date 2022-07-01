import requests
import json
from json import dumps

#CONSULTANDO A API DO STAR WARS - PERSONAGENS
lista = []
num = 1
''' 
    Criando uma lista vazia para armazenamento dos dados verdadeiros e
    uma variavel de contagem auxiliar.
'''

while num <= 9:
    ''' 
        A consulta na API referente a "people" contém 9 páginas, 
        utilizei o while para a leitura de todas as paginas.
    '''
    peoples = requests.get("https://swapi.dev/api/people/?page=%d" % (num))
    peoples = peoples.json()

    peoples = peoples['results']

    num2 = 0
    while num2 < len(peoples):
        ''' 
            Verificando na página a condição se o personagem
            participou de mais de 4 filmes.
        '''

        if len(peoples[num2]['films']) >= 4:
            ''' Se verdadeiro armazena o nome na lista e incrementa 1 na contagem'''
            nome = str(peoples[num2]['name'])
            lista.append(nome)
            num2 = num2 + 1

        else:
            ''' Se falso apenas incrementa 1 na contagem'''
            num2 = num2 + 1

    ''' Após executar 1 página, incrementa 1 para verificar a prox página'''
    num = num + 1


#CONSULTANDO A API DO STAR WARS - PERSONAGENS
lista2 = []
num3 = 1
''' 
    Criando uma lista vazia para armazenamento dos dados verdadeiros e
    uma variavel de contagem auxiliar.
'''

while num3 <= 6:
    ''' 
        A consulta referente a "planets" contém 6 páginas, 
    '''
    planets = requests.get("https://swapi.dev/api/planets/?page=%d" % (num3))
    planets = planets.json()

    planets = planets['results']

    num4 = 0
    while num4 < len(planets):
        ''' 
            Verificando na página a condição se o planeta
            possui pelo menos 5 moradores.
        '''

        if len(planets[num4]['residents']) >= 5:
            ''' Se verdadeiro armazena o nome na lista e incrementa 1 na contagem'''
            nome = str(planets[num4]['name'])
            lista2.append(nome)
            num4 = num4 + 1

        else:
            ''' Se falso apenas incrementa 1 na contagem'''
            num4 = num4 + 1

    ''' Após executar 1 página, incrementa 1 para verificar a prox página'''
    num3 = num3 + 1


### Gravando as respostas em arquivo JSON
''' 
Convertendo os objetos em strings.
'''

resposta1 = {"Personagens que aparecem em 4 ou mais filmes:" : lista }
resposta1_string = json.dumps(resposta1)

resposta2 = {"Planetas que possuem 5 ou mais moradores:" : lista2}
resposta2_string = json.dumps(resposta2)

''' 
Criando e gravando as respostas no arquivo JSON.
'''
file = open('resposta.json', 'wb')
file.write(resposta1_string.encode())
file.write(resposta2_string.encode())
file.close()