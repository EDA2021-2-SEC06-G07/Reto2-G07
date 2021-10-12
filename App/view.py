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
    2- dswdwdww
    3- 
    4- """
    print(menu)

catalog = None

"""
Menu principal
"""
if __name__ == "__main__":
    running = True
    while running:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 0:
            print("Cargando información de los archivos ....")
            catalog = controller.initCatalog()
            print("Loading artists")
            controller.load_artists(catalog[cf.ARTISTS])
            print("loaded " + str(mp.size(catalog[cf.ARTISTS])) + " artists")
            print("Loading artworks")
            controller.load_artworks(catalog[cf.ARTWORKS])
            print("loaded " + str(mp.size(catalog[cf.ARTWORKS])) + " artworks")

        elif int(inputs[0]) == 1:
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

        elif int(inputs[0]) == 2:
            print("Si va a escribir una fecha, omita los 0 antes de los numeros ")
            año1 = int(input("Gregue el año de la fecha 1: "))
            mes1 = int(input("Gregue el año de la fecha 1: "))
            dia1 = int(input("Gregue el año de la fecha 1: "))
            #año2 = int(input("Gregue el año de la fecha 2: "))
            #mes2 = int(input("Gregue el año de la fecha 2: "))
            #dia2 = int(input("Gregue el año de la fecha 2: "))
            mapa= controller.get_date(controller.GetDate(catalog[cf.ARTWORKS],catalog['dates']),año1,mes1,dia1)
            
            print(mapa)

            pass
        elif int(inputs[0] == 3):
            pass

        elif int(inputs[0] == 4):
            nationalities = controller.req4(catalog)
            pass

        else:
            running = False
