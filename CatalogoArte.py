from Artista import Artista
from Departamento import Departamento
from Obra import Obra

from Utils import mostrar_imagen
import requests

class CatalogoArte:
    def __init__(self):
        self.obras = []
        self.artistas = []
        self.departamentos = []


    def cargar_datos(self):
        url_api = 'https://collectionapi.metmuseum.org/public/collection/v1'

        # LLamado a la API de departamentos
        departamentos = requests.get(f'{url_api}/departments').json()['departments']
        print('Departamentos Obtenidos...')

        # LLamado a la API de IDS de obras
        obras_ids = requests.get(f'{url_api}/objects').json()['objectIDs']
        print('IDS Obras Obtenidos...')

        # LLamado a la API de Obras
        obras = []
        contador = 0
        for obra_id in obras_ids:
            obras.append(requests.get(f'{url_api}/objects/{obra_id}').json())
            contador +=1
            if contador == 10:
                break

        ### CARGA DE DATOS ###

        for departamento in departamentos:
            nuevo_departamento = Departamento(departamento['departmentId'], departamento['displayName'])
            self.departamentos.append(nuevo_departamento)

        for obra in obras:
            # Creacion de Artistas
            if obra['artistDisplayName'] == "":
                nombre = "Desconocido"
            else:
                nombre = obra['artistDisplayName']

            if obra['artistNationality'] == "":
                nacionalidad = "Desconocido"
            else:
                nacionalidad = obra['artistNationality']

    
            if obra['artistBeginDate'] == "":
                nacimiento = "Desconocido"
            else:
                nacimiento = obra['artistBeginDate']

            if obra['artistEndDate'] == "":
                muerte = "Desconocido"
            else:
                muerte = obra['artistEndDate']

            nuevo_artista = Artista(nombre,nacionalidad,nacimiento,muerte)

            self.artistas.append(nuevo_artista)

            nueva_obra = Obra(obra['objectID'], obra['title'], obra['classification'], obra['objectDate'], obra['primaryImage'], nuevo_artista, obra['department'])

            self.obras.append(nueva_obra)


    def buscar_por_departamento(self):
        print('\n< BÚSQUEDA DE OBRAS POR DEPARTAMENTO >')

        dptos_disponibles = [] #Lista de nombres de departamentos
        for departamento in self.departamentos:
            if departamento.nombre not in dptos_disponibles:
                dptos_disponibles.append(departamento.nombre)

        num = 1
        for departamento in dptos_disponibles:
            print(f'{num}) {departamento.upper()}')
            num +=1
        
        print(f'{num}) OTROS DEPARTAMENTOS/OBRAS NO CLASIFICADAS')

        x = input('>> Escriba el número de la opción que prefiera: ')
        while not x.isnumeric() or int(x) not in range(1, num+1):
            print('>> Inválido')
            x = input('>> Escriba el número de la opción que prefiera: ')

        contador = 0
        print('\n< LISTADO DE OBRAS ENCONTRADAS >')
        if int(x) == num:
            for obra in self.obras:
                if obra.departamento not in dptos_disponibles:
                    obra.mostrar()
                    contador +=1
        else:
            seleccion = dptos_disponibles[int(x)-1]
            for obra in self.obras:
                if obra.departamento == seleccion:
                    obra.mostrar()
                    contador +=1
        
        if contador == 0:
            print('\nNo se han encontrado obras que coincidan con su selección...')
        else:
            print(f'\nSe encontraron {contador} coincidencias!')
            self.mostrar_detalles_obra()

    def buscar_por_nacionalidad(self):
        print('\n< BÚSQUEDA DE OBRAS POR NACIONALIDAD DEL ARTISTA >')

        nac_disponibles = []
        for artista in self.artistas:
            if artista.nacionalidad not in nac_disponibles:
                nac_disponibles.append(artista.nacionalidad)

        num = 1
        for nacionalidad in nac_disponibles:
            print(f'{num}) {nacionalidad.upper()}')
            num +=1
        
        print(f'{num}) OTRAS NACIONALIDADES/OBRAS NO CLASIFICADAS')

        x = input('>> Escriba el número de la opción que prefiera: ')
        while not x.isnumeric() or int(x) not in range(1, num+1):
            print('>> Inválido')
            x = input('>> Escriba el número de la opción que prefiera: ')

        contador = 0
        print('\n< LISTADO DE OBRAS ENCONTRADAS >')
        if int(x) == num:
            for obra in self.obras:
                if obra.artista.nacionalidad not in nac_disponibles:
                    obra.mostrar()
                    contador +=1
        else:
            seleccion = nac_disponibles[int(x)-1]
            for obra in self.obras:
                if obra.artista.nacionalidad == seleccion:
                    obra.mostrar()
                    contador +=1
            
        
        if contador == 0:
            print('\nNo se han encontrado obras que coincidan con su selección...')
        else:
            print(f'\nSe encontraron {contador} coincidencias!')
            self.mostrar_detalles_obra()

    def buscar_por_nombre_autor(self):
        print('\n< BÚSQUEDA DE OBRAS POR NOMBRE DEL ARTISTA >')

        nombres_disponibles = [] #Lista de nombres de departamentos
        for artista in self.artistas:
            if artista.nombre not in nombres_disponibles:
                nombres_disponibles.append(artista.nombre)

        num = 1
        for nombre in nombres_disponibles:
            print(f'{num}) {nombre.upper()}')
            num +=1
        
        print(f'{num}) OTROS NOMBRES/OBRAS NO CLASIFICADAS')

        x = input('>> Escriba el número de la opción que prefiera: ')
        while not x.isnumeric() or int(x) not in range(1, num+1):
            print('>> Inválido')
            x = input('>> Escriba el número de la opción que prefiera: ')

        contador = 0
        print('\n< LISTADO DE OBRAS ENCONTRADAS >')
        if int(x) == num:
            for obra in self.obras:
                if obra.artista.nombre not in nombres_disponibles:
                    obra.mostrar()
                    contador +=1
        else:
            seleccion = nombres_disponibles[int(x)-1]
            for obra in self.obras:
                if obra.artista.nombre == seleccion:
                    obra.mostrar()
                    contador +=1
            
        
        if contador == 0:
            print('\nNo se han encontrado obras que coincidan con su selección...')
        else:
            print(f'\nSe encontraron {contador} coincidencias!')
            self.mostrar_detalles_obra()

    def mostrar_detalles_obra(self):
        print('Desea visualizar mas detalles sobre alguna de las obras?')
        x = input('Si (s)/No (n): ')
        while x.lower() not in ['s','n']:
            print('>> Inválido')
            x = input('Si (s)/No (n): ')

        if x.lower() == 's':
            print('\n< DETALLES DE LAS OBRAS >')
            while True:
                idx = input('Ingrese el ID de la Obra que desea visualizar: ')

                while not idx.isnumeric():
                    print('>> Inválido')
                    idx = input('Ingrese el ID de la Obra que desea visualizar: ')

                obra_seleccionada = None

                for obra in self.obras:
                    if obra.idx == int(idx):
                        obra_seleccionada = obra
                        break

                if obra_seleccionada == None:
                    print('El ID ingresado no coincide. Desea reintentar?')
                    x = input('Si (s)/No (n): ')
                    while x.lower() not in ['s','n']:
                        print('>> Inválido')
                        x = input('Si (s)/No (n): ')
                    
                    if x.lower() == 'n':
                        break
                else:
                    obra_seleccionada.mostrar_detalles()
                    break


    def inicio(self):
        print('Iniciando Carga de Datos...')
        self.cargar_datos()
        print('Finalizada Carga de Datos...')

        while True:
            print('\n< CATÁLOGO DE ARTE - MUSEO METROPOLITANO DE ARTE >')
            print('\n>> MENÚ INICIAL <<')
            print('1. Buscar Obras por Departamento')
            print('2. Buscar Obras por Nacionalidad')
            print('3. Buscar Obras por Nombre del Autor')
            print('4. Salir del Sistema')

            x = input('>> Escriba el número de la opción que prefiera: ')

            if x == '1':
                self.buscar_por_departamento()
            elif x == '2':
                self.buscar_por_nacionalidad()
            elif x == '3':
                self.buscar_por_nombre_autor()
            elif x == '4':
                print('>> Gracias por visitarnos. Vuelva pronto')
                break
            else:
                print('>> Inválido')