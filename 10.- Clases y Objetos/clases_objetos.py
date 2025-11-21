# Clases y Objetos en Python

"""
Elementos de una Clase

Una Clase se compone de
    - Atributos
    - Metodos

los Abributos son las CARACTERISTICAS de nuestros objetos.

Los Metodos son las ACCIONES que pueden realizar nuestros objetos.
En si, estas acciones son funciones, pero cuando se asocian con una clase se les llama metodos.

Una vez, que hemos definido nuestra clase, podemos crear objetos, a estos se le llama instanciar una clase.

"""

"""
Ejemplo:

Si queremos construir un edificio,
primero necesitamos su plano,
es decir, una CLASE o plantilla,
y a partir de ese plano,
podemos crear muchos edificios similares, es decir, los OBJETOS.

"""

## Difinimos una clase llamada Persona y creamos 2 metodos

# Creamos la Clase
class Persona:

    # Creamos el Metodo inicializar_persona
    def inicializar_persona(self, parm_nombre, parm_apellido):
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


# Creamos el programa principal con Objeto
if __name__ == "__main__":
    # Creamos un primer objeto
    persona1 = Persona()  # Se crea un objeto vacio en memoria
    persona1.inicializar_persona("Layla", "Acosta")
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona()  # Se crea un objeto vacio en memoria
    persona2.inicializar_persona("Ian", "Sanchez")
    persona2.mostrar_persona()


