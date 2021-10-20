"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

from typing import Container
import config as cf
import sys
import controller
import timer
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import linkedlistiterator as iter
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    menu = """Bienvenido
    0- Carga de datos
    1- Artistas nacidos entre dos fechas
    2- listar cronológicamente las adquisiciones
    3- clasificar las obras de un artista por técnica
    4- Nacionalidades
    5- Transportar obras de un departamento
    6-
    7- Tiempo de carga de mapas laboratorio
    8- Tiempo de ejecucion de los requerimientos"""
    print(menu)

catalog = None


def load():
    print("Cargando información de los archivos ....")
    catalog = controller.initCatalog()
    print("Loading artists")
    controller.load_artists(catalog[cf.ARTISTS])
    print("loaded " + str(mp.size(catalog[cf.ARTISTS])) + " artists")
    print("Loading artworks")
    controller.load_artworks(catalog[cf.ARTWORKS])
    print("loaded " + str(mp.size(catalog[cf.ARTWORKS])) + " artworks")
    return catalog


def req1():
    first_year = int(input("Cual es el año inicial:"))
    second_year = int(input("Cual es el año final:"))
    print("loadig artists between " + str(first_year) + " and " + str(second_year))

    artists = controller.req1(catalog[cf.ARTISTS], first_year, second_year)
    size = mp.size(artists)
    
    print(f"Numero de artistas entre {first_year} y {second_year} : {size}")

    print("Primeros 3:")
    for i in range(1, 3):
        print(f"  Nombre: {lt.getElement(artists, i)['DisplayName']}")
        print(f"  Año de nacimiento: {lt.getElement(artists, i)['BeginDate']}")
        print(f"  Año de fallecimiento: {lt.getElement(artists, i)['EndDate']}")
        print(f"  Nacionalidad: {lt.getElement(artists, i)['Nationality']}")
        print(f"  Genero: {lt.getElement(artists, i)['Gender']}")
        print()
    
    print("Ultimos 3:")
    for i in range(size - 3, size):
        print(f"  Nombre: {lt.getElement(artists, i)['DisplayName']}")
        print(f"  Año de nacimiento: {lt.getElement(artists, i)['BeginDate']}")
        print(f"  Año de fallecimiento: {lt.getElement(artists, i)['EndDate']}")
        print(f"  Nacionalidad: {lt.getElement(artists, i)['Nationality']}")
        print(f"  Genero: {lt.getElement(artists, i)['Gender']}")
        print()



def req2():
    print("Si va a escribir una fecha, omita los 0 antes de los numeros ")
    año1 = int(input("Agregue el año de la fecha 1: "))
    mes1 = int(input("Agregue el mes de la fecha 1: "))
    dia1 = int(input("Agregue el dia de la fecha 1: "))
    año2 = int(input("Agregue el año de la fecha 2: "))
    mes2 = int(input("Agregue el mes de la fecha 2: "))
    dia2 = int(input("Agregue el dia de la fecha 2: "))
    artworks= controller.req2(catalog[cf.ARTWORKS],año1,mes1,dia1,año2,mes2,dia2)
    print(artworks)
    print("Las obras en esas fechas son: "+ str(lt.size(artworks)))
    print('')
    print('los primeros 3 son:')
    print('')
    for i in range(0,3):
        print('Titulo: '+ lt.getElement(artworks,i)['Title'])
        print('ID(s): '+ lt.getElement(artworks,i)['ConstituentID']) 
        print('Fecha: '+ lt.getElement(artworks,i)['DateAcquired']) 
        print('Medio: '+ lt.getElement(artworks,i)['Medium'])
        if  lt.getElement(artworks,i)['Dimensions'] != None and lt.getElement(artworks,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(artworks,i)['Dimensions']) 
        elif lt.getElement(artworks,i)['Dimensions'] == None or lt.getElement(artworks,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ')    
        print('')
    print('los ultimos 3 son:')
    print('')
    for i in range(lt.size(artworks)-3,lt.size(artworks)):
        print('Titulo: '+ lt.getElement(artworks,i)['Title'])
        print('ID(s): '+ lt.getElement(artworks,i)['ConstituentID']) 
        print('Fecha: '+ lt.getElement(artworks,i)['DateAcquired']) 
        print('Medio: '+ lt.getElement(artworks,i)['Medium'])
        if  lt.getElement(artworks,i)['Dimensions'] != None and lt.getElement(artworks,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(artworks,i)['Dimensions']) 
        elif lt.getElement(artworks,i)['Dimensions'] == None or lt.getElement(artworks,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ')    
        print('')


def req3():
    artista= str(input('Agregue el nombre del artista: '))
    id=(controller.req3(catalog,artista))
    medios=controller.req3_1(catalog,id)
    print('')
    print('El ID del artista es: '+ str(id))
    print('')
    print('Las 3 primeras son')
    print('')
    for i in range(0,3):
        print('ObjectID'+ lt.getElement(medios,i)['ObjectID'])
        print('Titulo: '+ lt.getElement(medios,i)['Title'])
        print('ID(s): '+ lt.getElement(medios,i)['DateAcquired']) 
        print('Fecha: '+ lt.getElement(medios,i)['Medium']) 
        print('Medio: '+ lt.getElement(medios,i)['Dimensions'])
        if  lt.getElement(medios,i)['Dimensions'] != None and lt.getElement(medios,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(medios,i)['Dimensions']) 
        elif lt.getElement(medios,i)['Dimensions'] == None or lt.getElement(medios,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ')    
        print('')
    print('los ultimos 3 son:')
    print('')
    for i in range(lt.size(medios)-3,lt.size(medios)):
        print('ObjectID'+ lt.getElement(medios,i)['ObjectID'])
        print('Titulo: '+ lt.getElement(medios,i)['Title'])
        print('Fecha: '+ lt.getElement(medios,i)['DateAcquired']) 
        print('Medio: '+ lt.getElement(medios,i)['Medium']) 
        if  lt.getElement(medios,i)['Dimensions'] != None and lt.getElement(medios,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(medios,i)['Dimensions']) 
        elif lt.getElement(medios,i)['Dimensions'] == None or lt.getElement(medios,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ')    
        print('')


def req4():
    nationalities = controller.req4(catalog)
    array = controller.sort_nationalities(nationalities)
    for i in range(0, 9):
        elem = array[i]
        key = elem['key']
        size = elem['value']['size']
        print(f'Amount of artworks in {key}: {size}')
    print()

    mayor = array[0]['value']
    # print(mayor)
    it = iter.newIterator(mayor)
    for i in range(0, 3):
        if not iter.hasNext(it):
            break
        artwork = iter.next(it)
        ids = artwork['ConstituentID'].replace('[','').replace(']','').split(', ')
        artists = controller.get_artists(catalog, ids)
        print(f"Title: {artwork['Title']}")
        print(f"    Artists:")
        j = iter.newIterator(artists)
        while iter.hasNext(j):
            artist = iter.next(j)
            print(f'       {artist}')
        
        print(f"    Date: {artwork['Date']}")
        print(f"    Medium: {artwork['Medium']}")
        print(f"    Dimensions: {artwork['Dimensions']}")

    for i in range(mayor['size'] - 3, mayor['size']):
        artwork = lt.getElement(mayor, i)
        ids = artwork['ConstituentID'].replace('[','').replace(']','').split(', ')
        artists = controller.get_artists(catalog, ids)
        print(f"Title: {artwork['Title']}")
        print(f"    Artists:")
        j = iter.newIterator(artists)
        while iter.hasNext(j):
            artist = iter.next(j)
            print(f'       {artist}')
        
        print(f"    Date: {artwork['Date']}")
        print(f"    Medium: {artwork['Medium']}")
        print(f"    Dimensions: {artwork['Dimensions']}")


def req5():
    departamento= str(input('Escriba el depasrtamento: '))
    lista= controller.req5(catalog[cf.ARTWORKS],departamento)
    costoso=controller.mas_costosa(lista)
    antiguo=controller.mas_antigua(lista)
    print('')
    print('el total de obras es: ' + str(lt.size(lista)) )
    print('')
    print('Los mas antiguos ')
    print('')
    for i in range(0,5):
        print('')
        print('Titulo'+ lt.getElement( antiguo,i)['Title'])
        print('Artistas'+ lt.getElement( antiguo,i)['Artistas'])
        print('Clasificacion: '+ lt.getElement( antiguo,i)['Classification']) 
        print('Fecha: '+ lt.getElement( antiguo,i)['Date']) 
        print('Medio: '+ lt.getElement( antiguo,i)['Medium'])
        if  lt.getElement(antiguo,i)['Dimensions'] != None and lt.getElement(antiguo,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(antiguo,i)['Dimensions']) 
        elif lt.getElement(antiguo,i)['Dimensions'] == None or lt.getElement(antiguo,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ') 
        print('Costo: '+ str(lt.getElement( antiguo,i)['Costo']))
    print('')
    print('Los mas costosos')
    for i in range(lt.size(costoso)-5,lt.size(costoso)):
        print('')
        print('Titulo'+ lt.getElement( costoso,i)['Title'])
        print('Artistas'+ lt.getElement( costoso,i)['Artistas'])
        print('Clasificacion: '+ lt.getElement( costoso,i)['Classification']) 
        print('Fecha: '+ lt.getElement( costoso,i)['Date']) 
        print('Medio: '+ lt.getElement( costoso,i)['Medium'])
        if  lt.getElement(costoso,i)['Dimensions'] != None and lt.getElement(costoso,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(costoso,i)['Dimensions']) 
        elif lt.getElement(costoso,i)['Dimensions'] == None or lt.getElement(costoso,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ') 
        print('Costo: '+ str(lt.getElement( costoso,i)['Costo']))


def test_req1():
    first_year = 1920
    second_year = 1985
    print("loadig artists between " + str(first_year) + " and " + str(second_year))

    artists = controller.req1(catalog[cf.ARTISTS], first_year, second_year)
    size = mp.size(artists)
    
    print(f"Numero de artistas entre {first_year} y {second_year} : {size}")

    print("Primeros 3:")
    for i in range(1, 3):
        print(f"  Nombre: {lt.getElement(artists, i)['DisplayName']}")
        print(f"  Año de nacimiento: {lt.getElement(artists, i)['BeginDate']}")
        print(f"  Año de fallecimiento: {lt.getElement(artists, i)['EndDate']}")
        print(f"  Nacionalidad: {lt.getElement(artists, i)['Nationality']}")
        print(f"  Genero: {lt.getElement(artists, i)['Gender']}")
        print()
    
    print("Ultimos 3:")
    for i in range(size - 3, size):
        print(f"  Nombre: {lt.getElement(artists, i)['DisplayName']}")
        print(f"  Año de nacimiento: {lt.getElement(artists, i)['BeginDate']}")
        print(f"  Año de fallecimiento: {lt.getElement(artists, i)['EndDate']}")
        print(f"  Nacionalidad: {lt.getElement(artists, i)['Nationality']}")
        print(f"  Genero: {lt.getElement(artists, i)['Gender']}")
        print()



def test_req2():
    print("Si va a escribir una fecha, omita los 0 antes de los numeros ")
    año1 = 1944
    mes1 = 6
    dia1 = 6
    año2 = 1989
    mes2 = 11
    dia2 = 9
    artworks= controller.req2(catalog[cf.ARTWORKS],año1,mes1,dia1,año2,mes2,dia2)
    print(artworks)
    print("Las obras en esas fechas son: "+ str(lt.size(artworks)))
    print('')
    print('los primeros 3 son:')
    print('')
    for i in range(0,3):
        print('Titulo: '+ lt.getElement(artworks,i)['Title'])
        print('ID(s): '+ lt.getElement(artworks,i)['ConstituentID']) 
        print('Fecha: '+ lt.getElement(artworks,i)['DateAcquired']) 
        print('Medio: '+ lt.getElement(artworks,i)['Medium'])
        if  lt.getElement(artworks,i)['Dimensions'] != None and lt.getElement(artworks,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(artworks,i)['Dimensions']) 
        elif lt.getElement(artworks,i)['Dimensions'] == None or lt.getElement(artworks,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ')    
        print('')
    print('los ultimos 3 son:')
    print('')
    for i in range(lt.size(artworks)-3,lt.size(artworks)):
        print('Titulo: '+ lt.getElement(artworks,i)['Title'])
        print('ID(s): '+ lt.getElement(artworks,i)['ConstituentID']) 
        print('Fecha: '+ lt.getElement(artworks,i)['DateAcquired']) 
        print('Medio: '+ lt.getElement(artworks,i)['Medium'])
        if  lt.getElement(artworks,i)['Dimensions'] != None and lt.getElement(artworks,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(artworks,i)['Dimensions']) 
        elif lt.getElement(artworks,i)['Dimensions'] == None or lt.getElement(artworks,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ')    
        print('')


def test_req3():
    artista= 'Louise Bourgeois'
    id=(controller.req3(catalog,artista))
    medios=controller.req3_1(catalog,id)
    print('')
    print('El ID del artista es: '+ str(id))
    print('')
    print('Las 3 primeras son')
    print('')
    for i in range(0,3):
        print('ObjectID'+ lt.getElement(medios,i)['ObjectID'])
        print('Titulo: '+ lt.getElement(medios,i)['Title'])
        print('ID(s): '+ lt.getElement(medios,i)['DateAcquired']) 
        print('Fecha: '+ lt.getElement(medios,i)['Medium']) 
        print('Medio: '+ lt.getElement(medios,i)['Dimensions'])
        if  lt.getElement(medios,i)['Dimensions'] != None and lt.getElement(medios,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(medios,i)['Dimensions']) 
        elif lt.getElement(medios,i)['Dimensions'] == None or lt.getElement(medios,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ')    
        print('')
    print('los ultimos 3 son:')
    print('')
    for i in range(lt.size(medios)-3,lt.size(medios)):
        print('ObjectID'+ lt.getElement(medios,i)['ObjectID'])
        print('Titulo: '+ lt.getElement(medios,i)['Title'])
        print('Fecha: '+ lt.getElement(medios,i)['DateAcquired']) 
        print('Medio: '+ lt.getElement(medios,i)['Medium']) 
        if  lt.getElement(medios,i)['Dimensions'] != None and lt.getElement(medios,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(medios,i)['Dimensions']) 
        elif lt.getElement(medios,i)['Dimensions'] == None or lt.getElement(medios,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ')    
        print('')


def test_req4():
    nationalities = controller.req4(catalog)
    array = controller.sort_nationalities(nationalities)
    for i in range(0, 9):
        elem = array[i]
        key = elem['key']
        size = elem['value']['size']
        print(f'Amount of artworks in {key}: {size}')
    print()

    mayor = array[0]['value']
    # print(mayor)
    it = iter.newIterator(mayor)
    for i in range(0, 3):
        if not iter.hasNext(it):
            break
        artwork = iter.next(it)
        ids = artwork['ConstituentID'].replace('[','').replace(']','').split(', ')
        artists = controller.get_artists(catalog, ids)
        print(f"Title: {artwork['Title']}")
        print(f"    Artists:")
        j = iter.newIterator(artists)
        while iter.hasNext(j):
            artist = iter.next(j)
            print(f'       {artist}')
        
        print(f"    Date: {artwork['Date']}")
        print(f"    Medium: {artwork['Medium']}")
        print(f"    Dimensions: {artwork['Dimensions']}")

    for i in range(mayor['size'] - 3, mayor['size']):
        artwork = lt.getElement(mayor, i)
        ids = artwork['ConstituentID'].replace('[','').replace(']','').split(', ')
        artists = controller.get_artists(catalog, ids)
        print(f"Title: {artwork['Title']}")
        print(f"    Artists:")
        j = iter.newIterator(artists)
        while iter.hasNext(j):
            artist = iter.next(j)
            print(f'       {artist}')
        
        print(f"    Date: {artwork['Date']}")
        print(f"    Medium: {artwork['Medium']}")
        print(f"    Dimensions: {artwork['Dimensions']}")


def test_req5():
    departamento= 'Drawings & Prints'
    lista= controller.req5(catalog[cf.ARTWORKS],departamento)
    costoso=controller.mas_costosa(lista)
    antiguo=controller.mas_antigua(lista)
    print('')
    print('el total de obras es: ' + str(lt.size(lista)) )
    print('')
    print('Los mas antiguos ')
    print('')
    for i in range(0,5):
        print('')
        print('Titulo'+ lt.getElement( antiguo,i)['Title'])
        print('Artistas'+ lt.getElement( antiguo,i)['Artistas'])
        print('Clasificacion: '+ lt.getElement( antiguo,i)['Classification']) 
        print('Fecha: '+ lt.getElement( antiguo,i)['Date']) 
        print('Medio: '+ lt.getElement( antiguo,i)['Medium'])
        if  lt.getElement(antiguo,i)['Dimensions'] != None and lt.getElement(antiguo,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(antiguo,i)['Dimensions']) 
        elif lt.getElement(antiguo,i)['Dimensions'] == None or lt.getElement(antiguo,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ') 
        print('Costo: '+ str(lt.getElement( antiguo,i)['Costo']))
    print('')
    print('Los mas costosos')
    for i in range(lt.size(costoso)-5,lt.size(costoso)):
        print('')
        print('Titulo'+ lt.getElement( costoso,i)['Title'])
        print('Artistas'+ lt.getElement( costoso,i)['Artistas'])
        print('Clasificacion: '+ lt.getElement( costoso,i)['Classification']) 
        print('Fecha: '+ lt.getElement( costoso,i)['Date']) 
        print('Medio: '+ lt.getElement( costoso,i)['Medium'])
        if  lt.getElement(costoso,i)['Dimensions'] != None and lt.getElement(costoso,i)['Dimensions'] != '':
            print('Dimensiones: '+ lt.getElement(costoso,i)['Dimensions']) 
        elif lt.getElement(costoso,i)['Dimensions'] == None or lt.getElement(costoso,i)['Dimensions'] == '':
            print('Dimensiones: Unknown ') 
        print('Costo: '+ str(lt.getElement( costoso,i)['Costo']))

"""
Menu principal
"""
if __name__ == "__main__":
    running = True
    while running:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 0:
            catalog = load()

        elif int(inputs[0]) == 1:
            req1()

        elif int(inputs[0]) == 2:
            req2()
        
        elif int(inputs[0]) == 3:
            req3()
            
        elif int(inputs[0]) == 4:
            req4()

        elif int(inputs[0]) == 5:
            req5()
            
        elif int(inputs[0])== 7:
            tipo= str(input('Escripe el MapType de la carga entre comillas: '))
            carga= float(input('Escribe el factor de carga: '))
            print('el tiempo de demora al cargar el mapa de nacionalidades es: '+ str(controller.lab_6(catalog,tipo,carga)))

        elif int(inputs[0]) == 8:
            stop_watch = timer.Timer()

            time1 = str(stop_watch.time_function(test_req1))
            time2 = str(stop_watch.time_function(test_req2))
            time3 = str(stop_watch.time_function(test_req3))
            time4 = str(stop_watch.time_function(test_req4))
            time5 = str(stop_watch.time_function(test_req5))
            
            print('\n\n')
            print("time req1: " + time1+ 's')
            print("time req2: " + time2+ 's')
            print("time req3: " + time3+ 's')
            print("time req4: " + time4+ 's')
            print("time req5: " + time5+ 's')
        else:
            running = False


