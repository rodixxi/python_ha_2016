

class Persona:



    def __init__(self, nombre, edad):
        self.nombre = (
            'Nombre: {} '.format(
                nombre
            )
        )
        self.edad = edad

    # metodo extra no es lo pedido
    def mostrar_datos(self):

            print (self.nombre)
        print('Edad: {}'.format(self.edad))

    #
        def __repr__(self):
            return '<Persona %s>'  % self.nombre


        def __add__(self, other):

            lista = []
            lista.append(self)
            lista.append(other)

            return Grupo(lista)

        def __eq__ (self,p2):
           igual = False
           if self.edad== p2.edad and  self.nombre==p2.nombre:
               igual= True

           return igual

        def __ne__ (self,p2):
           Desigual = True
           if self.edad== p2.edad and  self.nombre==p2.nombre:
               Desigual= False

           return Desigual



class Grupo:


   def __init__(self,personas):
    self.personas = personas
    self.cantidad = len(self.personas)

    def __init__(): #constructor vacio para probar if Grupo[vacio]
        ""







   def __repr__(self):


           return '<Grupo %s '  % self.cantidad + 'personas>'




    # metodo longitud
   def __len__(self):

    return len(self.personas)

    # metodo extra
   def mostrar__grupo(self):
        for x in self.personas:
            print x

        return

   def __iter__ (self):

       for x in self.personas:

          print x




   def __eq__(self, g2):
       Iguales = False
       CantidadIgual = 0
       cantidad1 = self.__len__()
       cantidad2 = g2.__len__()

       if cantidad1 == cantidad2:

           for p1 in self.personas:
               for p2 in g2.personas:
                   if p1.__eq__(p2) == True:
                       CantidadIgual += 1
                       break

           if CantidadIgual ==  cantidad2:
               Iguales = True

           else:
               Iguales = False


       else:
           print "No pueden ser iguales ya que no coincide la cantidad de personas"


       return Iguales

   def __ne__(self, g2):
       Iguales = True
       CantidadIgual = 0
       cantidad1 = self.__len__()
       cantidad2 = g2.__len__()

       if cantidad1 == cantidad2:

           for p1 in self.personas:
               for p2 in g2.personas:
                   if p1.__eq__ (p2) == True:
                       CantidadIgual += 1
                       break

           if CantidadIgual == cantidad2:
               Iguales = False

           else:
               Iguales = True


       else:

           print "Son distintos ya que no coincide la cantidad de personas"




       return Iguales

   def __add__(self, p1):

       lista_nva = self.personas[:]
       lista_nva.append(p1)

       return Grupo(lista_nva)

   def __sub__(self, p1):

       if p1 in self.personas:
           lista = self.personas[:]
           lista.remove(p1)

       else:
           print "Este elemento no existe en la lista "
           return

       return Grupo(lista)

   def __isub__(self, grupo2): # es muy jodido python en listas tuve que hacer ese bardo
      # por que encima [:] esto me lo hace una lista de tuplas
       Lista_G1 = self.personas[:]
       Lista_G2 = grupo2.personas[:]
       Lista_G3 = list(Lista_G1)
       Lista_G2 = list(Lista_G2)

       Lista_G3.extend(Lista_G2)
       Lista_G4 = Lista_G3[:]







       for p1 in Lista_G4:

           for p2 in grupo2.personas:

               if p1.__eq__(p2):
                   Lista_G3.remove(p1)


       return Grupo(Lista_G3)




   def __iadd__(self, grupo2):  # lo que esta comentado en este metodo con print le pude ayudar a entender la logica del metodo , son controles no hacen falta para el ejercicio
           inicio = 0
           tamano1 = self.__len__() - 1
           tamano2 = grupo2.__len__()
           tamano_else1 = self.__len__()
           tamano2_else1 = grupo2.__len__() - 1
           devuelvo = []
           Lista_G1 = self.personas[:]
           Lista_G2 = grupo2.personas[:]



           if tamano2 <= tamano1:

               for p1 in range(0, len(Lista_G1)):
                   #print "p1"
                   #print Lista_G1[p1]
                   for p2 in range(inicio, len(Lista_G2)):
                       #print "p2:", Lista_G2[p2]

                       if (p1 == tamano1):

                           #print "entre if1"

                           if Lista_G1[p1].__eq__(Lista_G2[p2]) == False:
                               Lista_G1.append(Lista_G2[p2])
                               inicio += 1

                       if Lista_G1[p1].__eq__(Lista_G2[p2]) == True:
                           #print "entre if2"

                           inicio += 1
                           #print "inicio: ", inicio
                   if (inicio == tamano2):
                       print tamano2
                       devuelvo = Lista_G1
                       #print " final"
                       break

           else:
               #print "entre else"
               for p1 in range(0, len(Lista_G2)):
                  # print "p1"
                   print Lista_G2[p1]
                   for p2 in range(inicio, len(Lista_G1)):
                     #  print "p2:", Lista_G1[p2]

                       if (p1 == tamano2_else1):

                         #  print "entre if1"

                           if Lista_G1[p2].__eq__(Lista_G2[p1]) == False:
                               Lista_G2.append(
                                   Lista_G1[p2])  # el ultimo define , los que no se conozcan los agrega
                               inicio += 1

                       if Lista_G1[p2].__eq__(Lista_G2[p1]) == True:
                          # print "entre if2"

                           inicio += 1
                           #print "inicio: ", inicio

                   if (inicio == tamano_else1):
                       #print " final"
                       devuelvo = Lista_G2
                       break

           return Grupo(devuelvo)



           #Punto Grupo Verdadero

   def grupo_verdadero(self):

       if self.__len__() >= 1:
          return True
       else:
           return False

   def __next__(self,p1):
       if p1 in self.personas:
           return True
       else:
           return False

   def edad_promedio(self):


       acumulador = 0.
       if len(self.personas)== 0:

        raise EmpyGroupError("grupo vacio")

       else:

           for persona in self.personas:
               acumulador += persona.edad

           if (acumulador > 0):
               promedio = acumulador / self.__len__()

           return promedio


class EmpyGroupError(Exception):
    __module__ = Exception.__module__

















p = Persona('Juan', 20)
p2 = Persona('cristian', 38)
p3 = Persona('Damian', 22)
p4 = Persona('miguel', 55)
p5 = Persona('Lucas', 25)
p6 = Persona('Martin', 18)
p7 = Persona('Martin', 18)
p8 = Persona('Ernesto', 18)
comodin = Persona('Juan', 20)

g8 = p7.__add__(p8)
g9 = g8.__add__(p4)


# primer punto
#p.mostrar_datos()
#print p.__repr__()

#Punto 2
go = p.__add__(p2)
print go.__repr__()

g1 = p2.__add__(p)
print "representacion grupo1"
print g1.__repr__()



#Punto 3 comparacion de personas
print "comparacion de personas"
print p.__eq__(comodin)
print p.__ne__(p2)

print "creo g2"
g2 = p2.__add__(p3)



#Punto 4 comparacion de Grupos
#print "Comparacion de grupos:"
#print g1.__ne__(go)
#print g1.__ne__(g2)
#print "iguales"
#print g1.__eq__(go)
#print g1.__eq__(g2)


#Punto 6 g1 = go - p2
print "quitar persona a grupo"
g3 = go.__sub__(p)
#print g3.__repr__()


#Punto 5 g1 = go + p2
g4 = g1.__add__(p3)
#print g4.__repr__()
#print g4.mostrar__grupo()

#Punto 7 g2 = go + g1

g5 = p5.__add__(p6)

g6 = g4.__iadd__(g5) # g6 queda con 5 elementos


g7 = g6.__iadd__(g4)
#print "mostrar g7: "
#print g7.mostrar__grupo()  #---> como g7 queda igual a g6 se cumple con lo pedido

print "mostrar g10: "
g10 = g9.__iadd__(g7)

#Punto 8 g2 = go - g1
#print "Punto 8"
#g11 =g6.__isub__(g4)
#print "mostrar"
#g11.mostrar__grupo()
print "aaaa"





#Punto 10 Longitud
#print "Punto 10:"
#print g10.__len__()
#print g3.__len__()
#g11 = Grupo([])
#print g11.__len__() #Cumple ya que en esta vacia muestra 0

#Punto 11 Un grupo es verdadero:

print g10.grupo_verdadero()
print g6.grupo_verdadero()




#Punto 12 In
#print "punto 12"
#print g2.__next__(p3)
#print g2.__next__(p5)

#Punto 13 edad_promedio:
print "punto promedio"

#g13 = Grupo([])
#print go.edad_promedio()
#print g13.edad_promedio()


#Punto 9 Los grupos son iterables
#print "punto 9"

#for x in g10:
#    print x



