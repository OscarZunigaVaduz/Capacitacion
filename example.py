"""
class Sum:
    def __init__(self, tipo):
        print(tipo)
        self.tipo = tipo
    def print_sum(self, uno, dos):
        resultado = uno + dos
        resultado_txt = str(resultado)
        print(self.tipo + ' ' + resultado_txt)
    def get_sum(self, uno, dos):
        resultado = uno + dos
        return resultado
sumatorias = Sum(10)
sumatorias.print_sum(1,5)
# sumatorias.get_sum(1,5)
sumatorias2 = Sum(20)
sumatorias2.print_sum(1,5)
# sumatorias2.get_sum(1,5)

ESTE LO HICE YO
class Resta: 
    def __init__(self,tipo):
        print(tipo)
        self.tipo = tipo
    def print_resta(self, dos, uno):
        resultado = dos - uno
        resultado_txt = int(resultado)
        print(self.tipo - resultado_txt)
    def get_resta(self, dos, uno):
        resultado = dos - uno
        return resultado

diferencia = Resta(50)
diferencia.print_resta(2,1)
diferencia.get_resta(2,1)
#sumatorias2 = Sum(20)
#sumatorias2.print_sum(1,5)
# sumatorias2.get_sum(1,5)


ESTE ES EL QUE HICE YO Y OSCAR ME DIO MAS EJEMPLOS
class Resta:
    def __init__(self,tipo):
        print(tipo)
        self.tipo = tipo
    def print_resta(self, primero, segundo):
        resultado = segundo - primero
        print(self.tipo - resultado)
    def get_resta(self, dos, uno):
        resultado = dos - uno
        return resultado
    def print_default(self, valor="Hola", debug=True):
        if debug:
            print(valor)
diferencia = Resta(50)
diferencia.print_default(debug=False)



class Resta:
    def __init__(self,tipo):
        print(tipo)
        self.tipo = tipo
    def print_resta(self, primero, segundo):
        resultado = segundo - primero
        print(self.tipo - resultado)
    def get_resta(self, dos, uno):
        resultado = dos - uno
        return resultado
    def print_default(self, valor="Hola"):
        print(valor)
        return valor
        

diferencia = Resta(50)
diferencia.print_default(valor="Chau")


"""


class Resta:
    def __init__(self,tipo):
        print(tipo)
        self.tipo = tipo

    def print_resta(self, dos, uno):
        resultado = dos - uno
        resultado_txt = int(resultado)
        print(self.tipo - resultado_txt)

    def get_resta(self, dos, uno):
        resultado = dos - uno
        return resultado


#diferencia = Resta(50)
#diferencia.print_resta(2,1)

# Esto es una diferencia
