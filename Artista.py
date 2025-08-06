class Artista:
    def __init__(self, nombre, nacionalidad, nacimiento, muerte):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.nacimiento = nacimiento
        self.muerte = muerte

    def mostrar(self):
        print('\n< INFORMACIÓN DEL ARTISTA >')
        print(f'- NOMBRE: {self.nombre}')
        print(f'- NACIONALIDAD: {self.nacionalidad}')
        print(f'- FECHA DE NACIMIENTO: {self.nacimiento} - FECHA DE MUERTE: {self.muerte}')