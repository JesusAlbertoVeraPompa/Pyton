# Constructores en Python

# Uns constructor es un metodo espercial y se utiliza para crear un objeto o instanciar una clase,
# ademas nos puede servir para crear e inicializar los atributos de un nuevo objeto

## Difinimos una clase llamada Persona y creamos 2 metodos


# Creamos la Clase
class Persona:

    # Constructor para iniciar el metodo
    def __init__(self, parm_nombre, parm_apellido):
        # Creamos los atributos de la clase
        self.nombre = parm_nombre
        self.apellido = parm_apellido

    # Creamos el Metodo mostrar_persona
    def mostrar_persona(self):
        # Mostramos los atributos de la clase
        print(
            f"""Persona:
              Nombre: {self.nombre}
              Apellido: {self.apellido}"""
        )


# Creamos el Objeto
if __name__ == "__main__":
    # Creamos un primer objeto
    persona1 = Persona("Layla", "Acosta")
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona("Ian", "Sanchez")
    persona2.mostrar_persona()
