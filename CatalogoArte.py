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
        pass

    def buscar_por_nacionalidad(self):
        pass

    def buscar_por_nombre_autor(self):
        pass

    def mostrar_detalles_obra(self):
        pass

    def inicio(self):
        print('Iniciando Carga de Datos...')
        self.cargar_datos()
        print('Finalizada Carga de Datos...')

        print('< CATÁLOGO DE ARTE - MUSEO METROPOLITANO DE ARTE >')
        while True:
            print('>> MENÚ INICIAL <<')
            print('1. Buscar Obras por Departamento')
            print('2. Buscar Obras por Nacionalidad')
            print('3. Buscar Obras por Nombre del Autor')
            print('4. Mostrar Detalles de Obras')
            print('5. Salir del Sistema')

            x = input('>> Escriba el número de la opción que prefiera: ')

            if x == '1':
                self.buscar_por_departamento()
            elif x == '2':
                self.buscar_por_nacionalidad()
            elif x == '3':
                self.buscar_por_nombre_autor()
            elif x == '4':
                self.mostrar_detalles_obra()
            elif x == '5':
                print('>> Gracias por visitarnos. Vuelva pronto')
                break