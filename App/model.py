"""
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
    while iter.hasNext(i):
        key = iter.next(i)
        autores = mp.get(catalog[cf.ARTISTS], key)['value']
        #me.getvalue(trabajos)
        names= autores['DisplayName']
        if artista in names:
            id = autores['ConstituentID']
    return id

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
    while iter.hasNext(i):
        key = iter.next(i)
        autores = mp.get(catalog[cf.ARTISTS], key)['value']
        #me.getvalue(trabajos)
        names= autores['DisplayName']
        if artista in names:
            id = autores['ConstituentID']
    keys = mp.keySet(catalog[cf.ARTWORKS])
    #crea una tadlist
    i = iter.newIterator(keys)
    while iter.hasNext(i):
        key = iter.next(i)
        autores= mp.get(catalog[cf.ARTWORKS], key)['value']
    return id

def req3_1(catalog, id):
    medios= mp.newMap(maptype='CHAINING')
    llave_medios=lt.newList()
    key_artworks = mp.keySet(catalog[cf.ARTWORKS])
    i = iter.newIterator(key_artworks)
    while iter.hasNext(i):
        key = iter.next(i)
        element = mp.get(catalog[cf.ARTWORKS], key)['value']
        id2=int(element['ConstituentID'].replace('[', '').replace(']', '').split(',')[0])
        # Si se imprime sin el .split hay una coma en el medio, por eso se divid
        obid = int(element['ObjectID'])
        if int(id) == int(id2):
            medio=mp.get(catalog[cf.ARTWORKS],obid)['value']
            medio= medio['Medium']
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
    return medios

# Funciones de ordenamiento
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