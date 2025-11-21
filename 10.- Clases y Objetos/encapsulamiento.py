# Encapsulamiento en Python


# Creamos una clase llamada Coche
class Coche:

    # Constructor para iniciar el metodo
    def __init__(self, parm_marca, parm_modelo, parm_color):
        self.marca = parm_marca  # Atributo publico
        self._modelo = parm_modelo  # Atributo protegido
        self.__color = parm_color  # Atributo privado

    # Creamos el Metodo Conducir
    def conducir(self):
        print(
            f"""Conduciendo el coche:
            Marca: {self.marca}
            Modelo: {self._modelo}
            Color: {self.__color}
            """
        )


# Creamos el programa principal con Objeto
if __name__ == "__main__":
    # Creamos el 1° Objeto Coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()
