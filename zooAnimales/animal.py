import mamifero
import ave
import reptil
import anfibio
import pez


class Animal:

    _totalAnimales = 0

    # CONSTRUCTOR

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    # GETTERS AND SETTERS

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def getZona(self):
        return self._zona

    @classmethod
    def getTotalAnimales(cls):
        return Animal._totalAnimales

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def setGenero(self, genero):
        self._genero = genero

    def setZona(self, zona):
        self._zona = zona

    # METHODS

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        return f"""
            Mamiferos : {mamifero.Mamifero.cantidadMamiferos()}
            Aves : {ave.Ave.cantidadAves()}
            Reptiles : {reptil.Reptil.cantidadReptiles()}
            Peces : {pez.Pez.cantidadPeces()}
            Anfibios : {anfibio.Anfibio.cantidadAnfibios()}
            """

    def __str__(self):
        if self._zona is None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi " \
                   f"genero es {self._genero} "
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi " \
                   f"genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()}," \
                   f" en el {self._zona.getZoo().getNombre()} "
