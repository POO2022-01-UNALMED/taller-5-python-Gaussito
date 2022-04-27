class Zona:

    # CONSTRUCTOR
    def __init__(self, nombre, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    # GETTERS AND SETTERS

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimales(self):
        return self._animales

    def cantidadAnimales(self):
        return len(self._animales)

    # METHODS

    def agregarAnimales(self, animal):
        self._animales.append(animal)
