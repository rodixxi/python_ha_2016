# -*- coding: utf-8 -*-


class EmptyGroupError(Exception):
    pass


class Persona(object):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return "<Persona {}>".format(self.nombre)

    def __len__(self):
        return 1

    def __eq__(self, other):
        if self.nombre == other.nombre and self.edad == other.edad:
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Persona):
            return Grupo([self, other])
        else:
            raise TypeError("Persona no Valida")


class Grupo(object):

    def __init__(self, gente):
        self.gente = set(gente)

    def __eq__(self, other):
        if isinstance(other, Grupo):
            if self.__dict__ == other.__dict__:
                return True
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Grupo):
            if self.__dict__ != other.__dict__:
                return True
        else:
            return False

    def __add__(self, obj):
        if isinstance(obj, Persona):
            return Grupo(list(self.gente) + [obj])
        elif isinstance(self, Grupo):
            return Grupo(list(self.gente) + list(obj.gente))
        else:
            raise TypeError("Grupo no valido")

    def __sub__(self, obj):
        if isinstance(obj, Persona):
            return Grupo([x for x in self.gente if x != obj])
        else:
            raise TypeError("Grupo no valido")

    def __iter__(self):
        for e in self.gente:
            yield e

    def __len__(self):
        cnt = 0
        for e in self.gente:
            cnt += 1
        if cnt > 0:
            return cnt
        else:
            raise EmptyGroupError("Grupo Vacio")

    def __repr__(self):
        return "<Grupo '{} personas'>".format(len(self.gente))

    def imprimir(self):
        for e in self:
            print e

    def edad_promedio(self):
        edad = 0
        for e in self.gente:
            edad += e.edad

        return float(edad/len(self))


p0 = Persona("juan", 18)
p1 = Persona("tito", 34)
p2 = Persona("carlos", 36)
p3 = Persona("navarro", 36)
p4 = Persona("peperoni", 36)

g0 = p0 + p1 + p2 + p3 + p4 + p1 + p1
g1 = p0 + p1 + p2
g2 = p0 + p1 + p3
g3 = g1 + g2

print g0.edad_promedio()

print bool(Persona("juan", 18) == Persona("juan", 18))
print bool(Persona("juan", 18) == Persona("juan", 19))

print bool(Grupo({p0, p1}) != Grupo([p1, p0]))
print bool(Grupo({p0, p1}) != Grupo([p2, p0]))

if g0:
    print "tiene"

if Grupo([]):
    print "tiene"
