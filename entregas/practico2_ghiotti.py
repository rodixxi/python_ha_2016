

class Grupo:
    grupo = []
    def __init__(self, lista):
        self.grupo = lista
        self.index = len(lista)

    def __repr__(self):
        return "Grupo: " + str(len(self.grupo)) + " Personas"

    def __ne__(self, grupo):
        igual = 0
        if len(self.grupo) != len(grupo.grupo):
            return True
        else:
            for i in range(len(self.grupo)):
                for e in range(len(grupo.grupo)):
                    if self.grupo[i] == grupo.grupo[i]:
                        igual = igual + 1
            return not igual != len(self.grupo)

    def __eq__(self, grupo):
        return not self != grupo

    def __add__(self, other):
        if isinstance(other, Grupo):
            grupo = other.grupo
        else:
            grupo = [other]
        grupo1 = self.PasajeDePersonas()
        for i in range(len(grupo)):
            agregar = True
            for e in range(len(grupo1)):
                if grupo1[e] == grupo[i] and agregar:
                    agregar = False
            if agregar:
                grupo1.append(grupo[i])
        return Grupo(grupo1)

    def __len__(self):
        return len(self.grupo)

    def __sub__(self, other):
        grupo1 = self.PasajeDePersonas()
        if isinstance(other, Grupo):
            grupo = other.grupo
        else:
            grupo = [other]
        resta = 0
        acomulador = 0
        for i in range(len(grupo1)):
            conservar = True
            for e in range(len(grupo)):
                if grupo1[resta] == grupo[e] and conservar:
                    conservar = False
            if not conservar:
                del grupo1[resta]
                acomulador =+1
                resta = i + 1 - acomulador
            else:
                resta = i + 1 - acomulador
        return Grupo(grupo1)

    def __ifloordiv__(self, other):
        return len(self.grupo) >= 0

    def __contains__(self, persona):
        for i in range(len(self.grupo)):
            if persona == self.grupo[i]:
                return True
        return False

    def EdadPromedio(self):
        edadPromedio = 0
        try:
            for i in range(len(self.grupo)):
                edadPromedio = edadPromedio + self.grupo[i].edad
            return ((float)(edadPromedio) / (float)(len(self.grupo)))
        except ZeroDivisionError:
            print("El grupo esta vacio")

    def PasajeDePersonas(self):
        a = []
        for i in range(len(self.grupo)):
            a.append(self.grupo[i])
        return a

    def __iter__(self):
        self.index = len(self.grupo)
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.grupo[self.index]


class Persona:
    def __init__(self, nombre, edad):
                    self.nombre = nombre
                    self.edad = edad

    def __add__(self, persona):
                    return Grupo([self, persona])

    def __repr__(self):
                    return "Persona: " + self.nombre

    def __eq__(self, persona):
                    return self.edad == persona.edad and self.nombre == persona.nombre

    def __ne__(self, persona):
                    return not self == persona
