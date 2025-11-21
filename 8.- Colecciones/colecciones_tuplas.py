# Colecciones en Python

## Tuplas
mi_tupla = (1, 2, 3, 4, 5)
print("Tupla original:", mi_tupla)

# Acceder a elementos
print("Elemento en índice 0:", mi_tupla[0])
print("Elemento en índice -1 (último):", mi_tupla[-1])
print("Subtupla de índice 1 a 3:", mi_tupla[1:4])

# Longitud de la tupla
print("Longitud de la tupla:", len(mi_tupla))

# Desempaquetado de tuplas
a, b, c, d, e = mi_tupla
print("Desempaquetado:", a, b, c, d, e)

# Iteración sobre tuplas
for elemento in mi_tupla:
    print("Elemento:", elemento)
print("Iteración sobre la tupla terminada.")

## Inmutabilidad de las tuplas
try:
    mi_tupla[0] = 10
except TypeError as e:
    print("Error al intentar modificar una tupla:", e)
print("Colecciones de tuplas en Python completadas.")

## Funciones útiles para tuplas
mi_tupla2 = (3, 1, 4, 1, 5, 9, 2)
print("Tupla para funciones útiles:", mi_tupla2)
print("Índice de primer aparición de 1:", mi_tupla2.index(1))
print("Cantidad de apariciones de 1:", mi_tupla2.count(1))
print("Tupla ordenada:", tuple(sorted(mi_tupla2)))
print("Tupla convertida a lista:", list(mi_tupla2))
print("Colecciones de tuplas en Python completadas.")

## Anidamiento de tuplas
tupla_anidada = (1, 2, (3, 4), (5, 6))
print("Tupla anidada:", tupla_anidada)
print("Elemento anidado (3,4):", tupla_anidada[2])
print("Elemento 4 de la tupla anidada:", tupla_anidada[2][1])
print("Colecciones de tuplas en Python completadas.")

## Listas dentro de tuplas
tupla_con_lista = (1, 2, [3, 4, 5])
print("Tupla con lista:", tupla_con_lista)
tupla_con_lista[2].append(6)
print("Después de agregar 6 a la lista dentro de la tupla:", tupla_con_lista)
tupla_con_lista[2][0] = 30
print(
    "Después de modificar el primer elemento de la lista dentro de la tupla:",
    tupla_con_lista,
)
print("Colecciones de tuplas en Python completadas.")

## Tuplas dentro de una lista
lista_con_tuplas = [(1, 2), (3, 4), (5, 6)]
print("Lista con tuplas:", lista_con_tuplas)
for tupla in lista_con_tuplas:
    print("Tupla en la lista:", tupla)
print("Colecciones de tuplas en Python completadas.")

## Conversión entre listas y tuplas
lista = [1, 2, 3, 4, 5]
tupla_desde_lista = tuple(lista)
print("Tupla convertida desde lista:", tupla_desde_lista)
nueva_lista_desde_tupla = list(tupla_desde_lista)
print("Lista convertida desde tupla:", nueva_lista_desde_tupla)
print("Conversión entre listas y tuplas completada.")

## Tuplas dentro de tuplas
tupla_interna = (1, 2, (3, 4), (5, 6))
print("Tupla con tuplas internas:", tupla_interna)
print("Elemento de la tupla interna (3,4):", tupla_interna[2])
print("Elemento 4 de la tupla interna:", tupla_interna[2][1])
print("Tuplas dentro de tuplas completado.")

## Uso de la función zip() con tuplas
tupla1 = (1, 2, 3)
tupla2 = ("a", "b", "c")
combinadas = zip(tupla1, tupla2)
for elemento in combinadas:
    print("Elemento combinado:", elemento)
print("Uso de la función zip() con tuplas completado.")

## Eliminar tuplas
mi_tupla_temp = (1, 2, 3)
print("Tupla temporal antes de eliminar:", mi_tupla_temp)
del mi_tupla_temp
try:
    print(mi_tupla_temp)
except NameError as e:
    print("Error al intentar acceder a la tupla eliminada:", e)
print("Eliminación de tuplas completada.")

## Tuplas con diferentes tipos de datos
tupla_mixta = (1, "dos", 3.0, [4, 5], (6, 7))
print("Tupla mixta:", tupla_mixta)
print("Elementos de la tupla mixta:")
for elemento in tupla_mixta:
    print("Elemento:", elemento)
print("Tuplas con diferentes tipos de datos completado.")
