# -*- coding: utf-8 -*-
import requests
import json
import random



url = "https://openlibrary.org/dev/docs/api/subjects/love.json?details=true"





headers = {
        'cache-control': "no-cache"
}

response = requests.get('https://openlibrary.org/subjects/love.json?limit=500').json()


works_diccionary=response['works']

#random.shuffle(works_diccionary)

#print (response.text)
for i in range(0,10):
	x= random.randrange(499)
	print (works_diccionary[x]['title'])




# Pasamos la información de json a un diccionario.
#response_data = json.loads(response.text)


"""
# Como no nos devuelve la informacion directamente, hay que hacer otra peticion
estaciones = requests.request("GET", response_data["datos"])
estaciones_dic = json.loads(estaciones.text)

#Imprimimos el nombre y la latitud de cada estación
for estacion in estaciones_dic:
    print (estacion['nombre'] + ": " + estacion['latitud'])



"""
