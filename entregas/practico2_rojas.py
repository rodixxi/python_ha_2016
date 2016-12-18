#-*- coding: utf-8 -*-


class Persona(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return "<" + self.__class__.__name__ + " " + self.nombre + ">"

    def __add__(self, other):
        return Grupo([self, other])

    def __eq__(self, other):
        if self.__class__.__name__ == "Persona" and other.__class__.__name__ == "Persona":
            if self.nombre == other.nombre and self.edad == other.edad:
                return True
            else:
                return False

class Grupo(object):
    lista = []

    def __init__(self, lista):
        self.gp = lista
        self.index = 0


    def __repr__(self):
        return "<" + self.__class__.__name__ + " '" + str(len(self.gp)) + " personas'" + ">"

    def __add__(self, other):
        v = list(self.gp)
        if other.__class__.__name__ == "Persona":
            if other in self.gp:
                pass
            else:
                v.append(other)
        elif other.__class__.__name__ == "Grupo":
            for i in other.gp:
                if i in self.gp:
                    pass
                else:
                    v.append(i)
        v = tuple(v)
        return Grupo(v)

    def __ne__(self, other):
        if self.__class__.__name__ == "Grupo" and other.__class__.__name__ == "Grupo":
            if sorted(self.gp) != sorted(other.gp):
                return True
            else:
                return False

    def __sub__(self, other):
        if self.__class__.__name__ == "Grupo" and other.__class__.__name__ == "Persona":
            v = list(self.gp)
            for i in range(len(v)):
                if v[i] == other:
                    del v[i]
            v = tuple(v)
            return Grupo(v)

        elif self.__class__.__name__ == "Grupo" and other.__class__.__name__ == "Grupo":
            v = list(self.gp)
            for i in range(len(other.gp)):
                if other.gp[i] in v:
                    del v[i]
            v = tuple(v)
            return Grupo(v)

    def __len__(self):
        return len(self.gp)

    def edad_promedio(self):
        cont = prom = 0
        v = self.gp
        try:
            for i in v:
                prom += i.edad
                cont += 1
            prom = float(prom/cont)
            return prom
        except ZeroDivisionError:
            return "EmptyGroupError!!: Grupo vacío."

    def __iter__(self):
        return self

    def next(self):
        try:
            result = self.gp[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result




def iteracionGRUPOS(grupo):
    for persona in grupo:
        print persona

def gruposVERDADERO(grupo):
    if grupo:
        print "tiene"
    else:
        print "no tiene"














"----"

p0 = Persona("juan", 18)
p1 = Persona("tito", 34)
p2 = Persona("carlos", 36)
p4 = Persona("jose",40)
p5 = Persona("noelia", 25)


# repr Personas

#print repr(Persona("juan", 18))
#print repr(p1)
#print repr(p2)

# add, sub y repr de grupo


g0 = p0 + p1
g1 = p2 + p5
g2 = g1 + p4
g3 = g0 + g2
g4 = g0 - p1
g5 = g2 - g1


#print repr(g0)
#print repr(g1)
#print repr(g2)
#print repr(g3)
#print repr(g4)
#print repr(g5)



# eq de Persona y Grupo

#print bool(Persona("juan", 18) == Persona("juan", 18))
#print bool(Persona("juan", 18) == Persona("juan", 19))

#print bool(Grupo({p0, p1}) !=  Grupo([p1, p0]))
#print bool(Grupo((p0, p1)) != Grupo([p2, p0]))


# iterar Grupos


#iteracionGRUPOS(g0)
#iteracionGRUPOS(g1)
#iteracionGRUPOS(g2)
#iteracionGRUPOS(g3)
#iteracionGRUPOS(g4)
#iteracionGRUPOS(g5)



# len de Grupo
#print len(g0)
#print len(g1)
#print len(g2)
#print len(Grupo([]))

# if de Grupos
#gruposVERDADERO(g0)
#gruposVERDADERO(Grupo([]))
#gruposVERDADERO(Grupo(["tito", 18]))


# in de Persona en Grupo

#print p0 in g0
#print p0 in g1
#print p5 in g5



# edad promedio

#print g0.edad_promedio()
#print Grupo([]).edad_promedio()
