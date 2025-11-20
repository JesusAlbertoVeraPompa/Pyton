# Tipos de Datos en Python

# Números enteros
entero = 42
print("Número entero:", entero)
print("Tipo de dato:", type(entero))

# Números de punto flotante
flotante = 3.1416
print("Número flotante:", flotante)
print("Tipo de dato:", type(flotante))

# Números complejos
complejo = 2 + 3j
print("Número complejo:", complejo)
print("Tipo de dato:", type(complejo))

# Cadenas de texto
cadena = "Hola, Mundo!"
print("Cadena de texto:", cadena)
print("Tipo de dato:", type(cadena))

# Booleanos
booleano = True
print("Valor booleano:", booleano)
print("Tipo de dato:", type(booleano))

# Listas
lista = [1, 2, 3, 4, 5]
print("Lista:", lista)
print("Tipo de dato:", type(lista))

# Tuplas
tupla = (1, 2, 3)
print("Tupla:", tupla)
print("Tipo de dato:", type(tupla))

# Conjuntos
conjunto = {1, 2, 3}
print("Conjunto:", conjunto)
print("Tipo de dato:", type(conjunto))

# Diccionarios
diccionario = {"clave1": "valor1", "clave2": "valor2"}
print("Diccionario:", diccionario)
print("Tipo de dato:", type(diccionario))

# NoneType
nulo = None
print("Valor None:", nulo)
print("Tipo de dato:", type(nulo))

# Conversión de tipos de datos
numero_str = "100"
numero_int = int(numero_str)
print("Cadena convertida a entero:", numero_int)
print("Tipo de dato:", type(numero_int))
numero_float = float(numero_str)
print("Cadena convertida a flotante:", numero_float)
print("Tipo de dato:", type(numero_float))
booleano_desde_str = bool(numero_str)
print("Cadena convertida a booleano:", booleano_desde_str)
print("Tipo de dato:", type(booleano_desde_str))

# Operaciones con tipos de datos
suma = entero + numero_int
print("Suma de enteros:", suma)
multiplicacion = flotante * 2
print("Multiplicación de flotantes:", multiplicacion)
concatenacion = cadena + " ¿Cómo estás?"
print("Concatenación de cadenas:", concatenacion)
longitud_lista = len(lista)
print("Longitud de la lista:", longitud_lista)
valor_diccionario = diccionario["clave1"]
print("Valor del diccionario para 'clave1':", valor_diccionario)

# Verificación de tipos
es_entero = isinstance(entero, int)
print("¿'entero' es de tipo int?", es_entero)
es_cadena = isinstance(cadena, str)
print("¿'cadena' es de tipo str?", es_cadena)
es_lista = isinstance(lista, list)
print("¿'lista' es de tipo list?", es_lista)
es_diccionario = isinstance(diccionario, dict)
print("¿'diccionario' es de tipo dict?", es_diccionario)
es_nulo = nulo is None
print("¿'nulo' es None?", es_nulo)

# Tipos de datos mutables e inmutables
# Listas (mutables)
lista.append(6)
print("Lista después de agregar un elemento:", lista)

# Tuplas (inmutables)
# tupla[0] = 10  # Esto generaría un error
print("Tupla (inmutable):", tupla)

# Diccionarios (mutables)
diccionario["clave3"] = "valor3"
print("Diccionario después de agregar un par clave-valor:", diccionario)

# Conjuntos (mutables)
conjunto.add(4)
print("Conjunto después de agregar un elemento:", conjunto)

# Cadenas (inmutables)
# cadena[0] = "h"  # Esto generaría un error
print("Cadena (inmutable):", cadena)

# Funcion Bool con diferentes tipos de datos
print("Bool de 0:", bool(0))
print("Bool de 42:", bool(42))
print("Bool de cadena vacía:", bool(""))
print("Bool de cadena no vacía:", bool("Hola"))
print("Bool de lista vacía:", bool([]))
print("Bool de lista no vacía:", bool([1, 2, 3]))
print("Bool de None:", bool(None))
print("Bool de diccionario vacío:", bool({}))
print("Bool de diccionario no vacío:", bool({"clave": "valor"}))
print("Bool de conjunto vacío:", bool(set()))
print("Bool de conjunto no vacío:", bool({1, 2, 3}))


Saludo = "¡Hola! ¿En qué puedo ayudarte hoy?"
print("Bool de cadena Saludo no vacía:", bool(Saludo))
