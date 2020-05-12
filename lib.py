class Imprimir:
    def __init__(self, prefix):
        self.prefix = prefix
        self.num = 0

    def imprimir_texto(self, texto="Hola"):
        print(self.prefix + texto)
        return None

    def devolver_texto(self, texto="Hola"):
        return self.prefix + texto


class Mostrar:
    def __init__(self):
        pass
