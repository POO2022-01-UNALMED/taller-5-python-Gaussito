class Zoologico:

    # CONSTRUCTOR
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    # GETTERS AND SETTERS

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zonas

    # METHODS

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        aux = 0
        for zona in self._zonas:
            aux += zona.cantidadAnimales()
        return aux
