class Obra:
    def __init__(self, idx, titulo, tipo, anio_creacion, imagen_url, artista, departamento):
        self.idx = idx
        self.titulo = titulo
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen_url = imagen_url
        self.artista = artista
        self.departamento = departamento

    def mostrar(self):
        print('\n< INFORMACIÓN GENERAL DE LA OBRA >')
        print(f'- TÍTULO: {self.titulo} - ID: {self.idx}')
        print(f'- NOMBRE DEL ARTISTA: {self.artista.nombre}')

    def mostrar_detalles(self):
        print('\n< INFORMACIÓN DETALLADA DE LA OBRA >')
        print(f'- TÍTULO: {self.titulo} - ID: {self.idx}')
        print(f'- TIPO: {self.titulo}')
        print(f'- AÑO DE CREACIÓN: {self.anio_creacion}')
        self.artista.mostrar()
    def probar_cambio(self):
        pass

