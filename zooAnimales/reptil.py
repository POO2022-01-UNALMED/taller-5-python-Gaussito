import animal


class Reptil(animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    # CONSTRUCTOOR

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    # GETTERSS AND SETTERS

    def getListado(self):
        return Reptil._listado

    def getColorEscamas(self):
        return self._colorEscamas

    def getLargoCola(self):
        return self._largoCola

    def setListado(self, listado):
        Reptil._listado = listado

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil._listado)

    # METHODS

    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil.serpientes += 1
        reptil = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        return reptil
