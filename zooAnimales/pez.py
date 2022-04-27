import animal


class Pez(animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    # CONSTRUCTOR

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    # GETTERS AND SETTERS

    def getListado(self):
        return Pez._listado

    def getColorEscamas(self):
        return self._colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setListado(self, listado):
        Pez._listado = listado

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    @classmethod
    def cantidadPeces(cls):
        return len(Pez._listado)

    # METHODS

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
