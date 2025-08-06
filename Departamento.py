class Departamento:
    def __init__(self, idx, nombre):
        self.idx = idx
        self.nombre = nombre

    def mostrar(self):
        print('< INFORMACIÓN DEL DEPARTAMENTO >')
        print(f'- NOMBRE: {self.nombre} - ID: {self.idx}')