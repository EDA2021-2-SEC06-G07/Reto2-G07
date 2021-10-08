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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.DataStructures import mapentry as me
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
    catalog[cf.ARTISTS] = mp.newMap(maptype == 'CHAINING')
    catalog[cf.ARTWORKS] = mp.newMap(maptype == 'CHAINING')
    catalog['dates']= mp.newMap(600, maptype='PROBING',loadfactor=0.5)
    return catalog


def add_artwork(map, artwork):
    mp.put(map, int(artwork['ObjectID']), artwork)

def add_artist(map, artist):
    mp.put(map, artist['ConstituentID'], artist)
# Funciones para agregar informacion al catalogo
def add_dates(catalog,catalogo):
    #catalog con los ARTWORKS
    #catalogo es el mapa de las dates
    years = catalogo
    for i in range(0,lt.size(catalog)-1):
        element= lt.getElement(catalog,i)
        fecha=element['DateAcquired']
        if (fecha != ''):
            pubyear = fecha
            pubyear= pubyear.split('-')
            pubyear = datetime.date(float(pubyear[0]) ,float(pubyear[1]),float(pubyear[2]))
            print(pubyear)
        else:
            pubyear = datetime.date(2020,8,9)
        existyear = mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            year = me.getValue(entry)
        else:
            year = newDate(pubyear)
            mp.put(years, pubyear, year)
        lt.addLast(year['dates'], element)
    return years

    
def newDate(pubyear):
    
    entry = {'date': "", "ARTWORKS": None}
    entry['date'] = pubyear
    entry['ARTWORKS'] = lt.newList('SINGLE_LINKED')
    return entry

def req1(catalog, year1, year2):
    artistas = lt.newList()
    for key in mp.keySet(catalog[cf.ARTISTS]):
        print(key)
        #artist = catalog[cf.ARTISTS][key]
        #if int(artist['BeginDate']) > year1 and int(artist['BeginDate']) < year2:
        #    lt.addLast(artist)
    ms.sort(artistas, cmp_artist_date)
    


# Funciones para creacion de datos
def get_date(catalog,año1,mes1,dia1):
    date1=datetime.date(año1,mes1,dia1)
    #date2=datetime.date(año2,mes2,dia2)
    date=mp.get(catalog['dates'], date1)
    if date:
        return me.getValue(date)
    return None
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmp_artist_date(artist1, artist2):
    year1 = artist1['BeginDate']
    year2 = artist2['BeginDate']

    if year1 < year2:
        return -1
    elif year2 < year1:
        return 1
    else:
        return 0

# Funciones de ordenamiento
