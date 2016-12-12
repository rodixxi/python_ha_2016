
class Persona(object):

    def __init__(self, nombre):
        self.nombre = nombre



nombre = raw_input("Cual es su nombre: ")
p = Persona(nombre)

while True:
    attr = raw_input("Que otro atributo le gustaria agregar? ")
    value = raw_input("Con que valor de {}? ".format(attr))

    setattr(p, attr, value)

    continuar = raw_input("Desea continuar? [S/N] ")
    if continuar.lower().strip() == "n":
        break

print("\nPersona '{}' Creada:".format(p.nombre))
for k, v in vars(p).items():
    print("\t{} = {}".format(k, v))
