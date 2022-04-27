from zooAnimales.animal import Animal


class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    # CONSTRUCTOR

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    # GETTERS AND SETTERS

    def getListado(self):
        return Anfibio._listado

    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setListado(self, listado):
        Anfibio._listado = listado

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio._listado)

    # METHODS

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra
