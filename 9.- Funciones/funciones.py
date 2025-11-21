# Funciones en Python


# Definición de una función simple
def saludar(nombre):
    """Función que saluda a una persona por su nombre."""
    return f"Hola, {nombre}!"


# Uso de la función
print(saludar("Ana"))


# Función con múltiples parámetros
def sumar(a, b):
    """Función que suma dos números."""
    return a + b


# Uso de la función
print(sumar(5, 3))


# Función con valor por defecto
def potencia(base, exponente=2):
    """Función que calcula la potencia de un número."""
    return base**exponente


# Uso de la función
print(potencia(4))  # Usa el valor por defecto del exponente

print(potencia(4, 3))  # Especifica un exponente diferente


# Función con argumentos arbitrarios
def lista_nombres(*nombres):
    """Función que recibe una cantidad arbitraria de nombres y los imprime."""
    for nombre in nombres:
        print(nombre)


# Uso de la función
lista_nombres("Ana", "Luis", "Carlos")


# Función con argumentos clave arbitrarios
def imprimir_info(**info):
    """Función que recibe información clave-valor y la imprime."""
    for clave, valor in info.items():
        print(f"{clave}: {valor}")


# Uso de la función
imprimir_info(nombre="Ana", edad=30, ciudad="Madrid")


# Función con retorno múltiple
def operaciones(a, b):
    """Función que retorna la suma y el producto de dos números."""
    suma = a + b
    producto = a * b
    return suma, producto


# Uso de la función
suma, producto = operaciones(4, 5)
print(f"Suma: {suma}, Producto: {producto}")


# Función recursiva
def factorial(n):
    """Función que calcula el factorial de un número de forma recursiva."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Uso de la función
print(factorial(5))  # Output: 120
# Función lambda (anónima)
cuadrado = lambda x: x**2
# Uso de la función lambda
print(cuadrado(6))  # Output: 36
# Uso de funciones lambda con map
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Output: [1, 4, 9, 16, 25]
# Uso de funciones lambda con filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4]
