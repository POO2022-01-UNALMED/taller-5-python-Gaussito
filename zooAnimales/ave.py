from zooAnimales.animal import Animal


class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    # CONSTRUCTOR

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    # GETTERS AND SETTERS

    def getListado(self):
        return Ave._listado

    def getColorPlumas(self):
        return self._colorPlumas

    def setListado(self, listado):
        Ave._listado = listado

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(Ave._listado)

    # METHODS

    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montana", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montana", genero, "blanco y amarillo")

    def toString(self):
        return self.__str__()
