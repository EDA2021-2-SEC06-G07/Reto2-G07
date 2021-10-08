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
 """

import config as cf
import model
import csv


FILE_ARTISTS = 'MoMa/Artists-utf8-small.csv'
FILE_ARTWORKS = 'MoMa/Artworks-utf8-small.csv' 

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog = model.newCatalog()
    return catalog

def load_artworks(map):
    #artworkfile
    awf = cf.data_dir + FILE_ARTWORKS
    in_file = csv.DictReader(open(awf, encoding='utf-8'))
    for artwork in in_file:
        model.add_artwork(map, artwork)

    
def load_artists(map):
    #artistfile
    artf = cf.data_dir + FILE_ARTISTS
    in_file = csv.DictReader(open(artf, encoding='utf-8'))
    for artist in in_file:
        model.add_artist(map, artist)

# Funciones para la carga de datos
def GetDate(catalog,catalogo):
    return model.add_dates(catalog,catalogo)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def get_date(catalog,año1,mes1,dia1):
    return model.get_date(catalog,año1,mes1,dia1)

    
def req1(catalog, year1, year2):
    return model.req1(catalog, year1, year2)