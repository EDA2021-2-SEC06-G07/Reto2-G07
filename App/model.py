﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from App.controller import initCatalog
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import linkedlistiterator as iter
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime
from statistics import mode
assert cf

ARTISTAS = "Artistas"
ARTWORKS = "Artworks"

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {
        cf.ARTWORKS: None,
        cf.ARTISTS: None,
        'dates':None
    }
    catalog[cf.ARTISTS] = mp.newMap(maptype = 'CHAINING')
    catalog[cf.ARTWORKS] = mp.newMap(maptype = 'CHAINING')
    return catalog


def add_artwork(map, artwork):
    mp.put(map, int(artwork['ObjectID']), artwork)

def add_artist(map, artist):
    mp.put(map, artist['ConstituentID'], artist)
# Funciones para agregar informacion al catalogo

def req4(catalog):
    # create a map. key: country, value: list
    nationalities = mp.newMap(maptype = 'CHAINING')
    nationalities_keys = lt.newList()
    key_artworks = mp.keySet(catalog[cf.ARTWORKS])
    i = iter.newIterator(key_artworks)
    while iter.hasNext(i):
        key = iter.next(i)
        element = mp.get(catalog[cf.ARTWORKS], key)['value']
        c_id = element['ConstituentID'].replace('[', '').replace(']', '').split(',')[0]
        nationality = mp.get(catalog[cf.ARTISTS], c_id)['value']['Nationality']

        #look for the nationality in the keys
        found = False
        j = iter.newIterator(nationalities_keys)
        while iter.hasNext(j) and found != True:
            current = iter.next(j)
            if nationality == current:
                found = True
                lt.addLast(mp.get(nationalities, nationality)['value'], element)
        
        # key was not found in the map
        if not found:
            # add the new list
            mp.put(nationalities, nationality, lt.newList())
            lt.addLast(mp.get(nationalities, nationality)['value'] ,element)
            lt.addLast(nationalities_keys, nationality)

    return nationalities


# Funciones para creacion de datos
def lab_6(catalog,tipo,carga):
    start_time=time.process_time()
    # create a map. key: country, value: list
    nationalities = mp.newMap(maptype = tipo, loadfactor= float(carga))
    nationalities_keys = lt.newList()
    key_artworks = mp.keySet(catalog[cf.ARTWORKS])
    i = iter.newIterator(key_artworks)
    while iter.hasNext(i):
        key = iter.next(i)
        element = mp.get(catalog[cf.ARTWORKS], key)['value']
        c_id = element['ConstituentID'].replace('[', '').replace(']', '').split(',')[0]
        nationality = mp.get(catalog[cf.ARTISTS], c_id)['value']['Nationality']

        #look for the nationality in the keys
        found = False
        j = iter.newIterator(nationalities_keys)
        while iter.hasNext(j) and found != True:
            current = iter.next(j)
            if nationality == current:
                found = True
                lt.addLast(mp.get(nationalities, nationality)['value'], element)
        

        # key was not found in the map
        if not found:
            # add the new list
            mp.put(nationalities, nationality, lt.newList())
            lt.addLast(mp.get(nationalities, nationality)['value'] ,element)
            lt.addLast(nationalities_keys, nationality)
    stop_time= time.process_time()
    time_in_ms=(stop_time-start_time)*1000
    return time_in_ms


# Funciones de consulta
def req1(catalog, year1, year2):
    artistas = lt.newList(datastructure='ARRAY_LIST')
    keys = mp.keySet(catalog)
    i = iter.newIterator(keys)
    while iter.hasNext(i):
        key = iter.next(i)
        artist = mp.get(catalog, key)['value']
        if artist != None and int(artist['BeginDate']) > year1 and int(artist['BeginDate']) < year2:
            lt.addLast(artistas, artist)        
    ms.sort(artistas, cmp_artist_date)

    return artistas


def req2(catalog,año1,mes1,dia1,año2,mes2,dia2):
    date1=datetime.date(año1,mes1,dia1)
    date2=datetime.date(año2,mes2,dia2)
    artworks=lt.newList(datastructure='ARRAY_LIST')
    keys = mp.keySet(catalog)
    i = iter.newIterator(keys)
    contador = 0
    while iter.hasNext(i):
        key = iter.next(i)
        trabajos = mp.get(catalog, key)['value']
        lista1= trabajos['DateAcquired']
        if lista1!= None and lista1!= '':
            lista= lista1.split('-')
            fecha= datetime.date(int(lista[0]),int(lista[1]),int(lista[2]))
            if fecha > date1 and fecha < date2:
                lt.addLast(artworks, trabajos)
        purchase= trabajos['CreditLine']
        if 'Purchase' in purchase:
            contador += 1
    ms.sort(artworks,cmp_artwork_date)
    print('-------------------------')
    print('Las obras en purchase son : '+ str(contador))
    print('')
    return artworks


def req3(catalog, artista):
    keys = mp.keySet(catalog[cf.ARTISTS])
    #crea una tadlist
    i = iter.newIterator(keys)
    id=None
    while iter.hasNext(i):
        key = iter.next(i)
        autores = mp.get(catalog[cf.ARTISTS], key)['value']
        #me.getvalue(trabajos)
        names= autores['DisplayName']
        if artista in names:
            id = autores['ConstituentID']
            break
    return id


def req3_1(catalog, id):
    medios= mp.newMap(maptype='CHAINING')
    llave_medios=lt.newList()
    key_artworks = mp.keySet(catalog[cf.ARTWORKS])
    i = iter.newIterator(key_artworks)
    contador= 0
    lista=lt.newList(datastructure='ARRAY_LIST')
    while iter.hasNext(i):
        key = iter.next(i)
        element = mp.get(catalog[cf.ARTWORKS], key)['value']
        id2=int(element['ConstituentID'].replace('[', '').replace(']', '').split(',')[0])
        # Si se imprime sin el .split hay una coma en el medio, por eso se divide
        obid = int(element['ObjectID'])
        if int(id) == int(id2):
            contador+=1
            medio=mp.get(catalog[cf.ARTWORKS],obid)['value']
            medio= medio['Medium']
            lt.addLast(lista,medio)
            found=False
            j = iter.newIterator(llave_medios)
            while iter.hasNext(j) and found != True:
                current = iter.next(j)
                if medio==current:
                    found=True
                    lt.addLast(mp.get(medios,medio)['value'], element)
            if not found:
                mp.put(medios,medio,lt.newList())
                lt.addLast(mp.get(medios,medio)['value'], element)
                lt.addLast(llave_medios,medio)
    usada= mode(lista['elements'])
    lista2=lt.newList(datastructure='ARRAY_LIST')
    keys = mp.keySet(medios)
    i = iter.newIterator(keys)
    while iter.hasNext(i):
        key = iter.next(i)
        entry=mp.get(medios,key)['key']
        if usada == entry:
            trabajos=mp.get(medios,key)['value']
            for k in lt.iterator(trabajos):
                lt.addLast(lista2,k)
    ms.sort(lista2,cmp_medio_date)
    print('-------------------------------')
    print('El total de obras del autor es: ' + str(contador))
    print('')
    print('la mas usada es: ' + usada)
    return lista2
            
def req5(catalog,departamento):
    lista=lt.newList(datastructure='ARRAY_LIST')
    contador_peso= 0
    contador_costo= 0
    keys = mp.keySet(catalog)
    i = iter.newIterator(keys)
    while iter.hasNext(i):
        key = iter.next(i)
        trabajos = mp.get(catalog, key)['value']
        depa=trabajos['Department']
        if depa == departamento:
            Largo = 0
            Ancho = 0
            Alto = 0
            Peso = 0
            countLongitud=0
            countPeso=0 
            costos= 0
            if trabajos['Width (cm)']!= None and trabajos['Width (cm)']!="":
                Ancho = (float(trabajos['Width (cm)']))/100
            else:
                Ancho = 1
            if trabajos['Height (cm)']!= None and trabajos['Height (cm)']!="":
                Alto = (float(trabajos['Height (cm)']))/100
            else:
                    Alto = 1
            if trabajos['Length (cm)']!= None and trabajos['Length (cm)']!= "":
                        Largo = (float(trabajos['Length (cm)']))/100
            else:
                Largo=1
            countLongitud= 72*(Alto * Ancho * Largo)
            if trabajos['Weight (kg)'] != None and trabajos['Weight (kg)'] != "":
                Peso= float(trabajos['Weight (kg)'])
            else: 
                Peso= 0
            countPeso= 72*(Peso)

            if countPeso > countLongitud:
                costos=countPeso
            else: 
                costos=countLongitud
            contador_costo += costos
            contador_peso += Peso
            dicc={}               
            dicc['Title']= trabajos['Title']
            dicc['Artistas']= trabajos['ConstituentID']
            dicc['Classification']= trabajos['Classification']
            dicc['Date']=trabajos['Date']
            dicc['Medium']= trabajos['Medium']
            dicc['Dimensions']= trabajos['Dimensions']
            dicc['Costo']= costos
            lt.addLast(lista,dicc)
    print('---------------')
    print('El costo estimado es de: ' + str(contador_costo))
    print('')
    print('El peso total es de: ' + str(contador_peso))
    return lista

def mas_costosos(lista):
    costoso = lista
    ms.sort(costoso,cmp_cost)
    return costoso

def mas_antiguas(lista):
    antiguas= lista
    ms.sort(antiguas,cmp_artwork_date_created)
    return antiguas
    
# Funciones de ordenamiento
def cmp_cost(artw1, artw2):
    cost1 = artw1['Costo']
    cost2 = artw2['Costo']

    if cost1 > cost2:
        return 1
    elif cost1 < cost2:
        return -1
    else:
        return 0


def cmp_artist_date(artist1, artist2):
    result = 0
    
    if artist1['BeginDate'] > artist2['BeginDate']:
        result = 1
    elif artist1['BeginDate'] < artist2['BeginDate']:
        result = -1
    return result

def cmp_artwork_date(art1, art2):
    result = 0
    art1= art1['DateAcquired'].split('-')
    art2= art2['DateAcquired'].split('-')
    art1= datetime.date(int(art1[0]),int(art1[1]),int(art1[2]))
    art2= datetime.date(int(art2[0]),int(art2[1]),int(art2[2]))
    if art1 > art2:
        result = 1
    elif art1 < art2:
        result = -1
    return result


def cmp_artwork_date_created(art1, art2):
    result = 0
    art1= art1['Date']
    art2= art2['Date']

    if art1 > art2:
        result = 1
    elif art1 < art2:
        result = -1
    return result



def cmp_medio_date(med1,med2):
    result= 0
    med1= med1['DateAcquired'].split('-')
    med2= med2['DateAcquired'].split('-')
    med1= datetime.date(int(med1[0]),int(med1[1]),int(med1[2]))
    med2= datetime.date(int(med2[0]),int(med2[1]),int(med2[2]))

    if med1 > med2:
        result = 1
    elif med1 < med2:
        result = -1
    return result


def get_artists(catalog, ids):
    artists = lt.newList()
    for id in ids:
        artist = mp.get(catalog[cf.ARTISTS], id)['value']
        lt.addLast(artists,artist['DisplayName'])
    return artists


# insertion sort del diccionario, a un arreglo de tamaño definido
# se usa insertion ya que pese a ser O(n²), son pocas las nacionalidades
# y dificilmente superaran los 64 elementos siendo en tiempo insertion
# mas eficiente que merge o quick
def sort_nationalities(nationalities):
    # no se usa la estructura de datos dada, ya que no es posible establecer un size 
    # fijo para esta, esto haria insertar en el peor caso, O(n²) pero como se sabe la
    # cantidad de elementos que va a haber en el arreglo, la complegidad es O(1) para 
    # todos los casos
    array = [None] * mp.size(nationalities)
    it = iter.newIterator(mp.keySet(nationalities))
    i = 0
    while iter.hasNext(it):
        elem = mp.get(nationalities, iter.next(it))
        array[i] = elem
        size = elem['value']['size']

        j = i
        stop = False
        while j > 0 and not stop:
            if size > array[j-1]['value']['size']:
                
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            else:
                stop = True
            j -= 1
        i += 1
    return array

