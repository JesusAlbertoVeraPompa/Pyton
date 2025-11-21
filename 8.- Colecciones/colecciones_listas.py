# Colecciones en Python

## Listas
mi_lista = [1, 2, 3, 4, 5]
print("Lista original:", mi_lista)

# Agregar elementos
mi_lista.append(6)
print("Después de append(6):", mi_lista)
mi_lista.insert(0, 0)
print("Después de insert(0, 0):", mi_lista)
mi_lista.insert(7, 1000)
print("Después de insert(0, 0):", mi_lista)
mi_lista.insert(15, 1000)
print("Después de insert(0, 0):", mi_lista)
mi_lista.insert(5, 1000)
print("Después de insert(0, 0):", mi_lista)

# Eliminar elementos
mi_lista.remove(1000)
print("Después de remove(1000):", mi_lista)
eliminado = mi_lista.pop()
print("Después de pop():", mi_lista, "Elemento eliminado:", eliminado)
eliminado_index = mi_lista.pop(2)
print("Después de pop(2):", mi_lista, "Elemento eliminado:", eliminado_index)

## Eliminar duplicados de una lista
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print("Lista con duplicados:", lista_con_duplicados)
print("Lista sin duplicados:", lista_sin_duplicados)
print("Colecciones de listas en Python completadas.")

# Acceder a elementos
print("Elemento en índice 0:", mi_lista[0])
print("Elemento en índice -1 (último):", mi_lista[-1])
print("Sublista de índice 1 a 3:", mi_lista[1:4])

# Modificar elementos
mi_lista[0] = 10
print("Después de modificar índice 0 a 10:", mi_lista)
mi_lista[2:4] = [20, 30]
print("Después de modificar índices 2 a 4 a [20, 30]:", mi_lista)

# Longitud de la lista
print("Longitud de la lista:", len(mi_lista))

# Ordenar la lista
mi_lista.sort()
print("Después de sort():", mi_lista)
mi_lista.sort(reverse=True)
print("Después de sort(reverse=True):", mi_lista)

# Invertir la lista
mi_lista.reverse()
print("Después de reverse():", mi_lista)

# Limpiar la lista
mi_lista.clear()
print("Después de clear():", mi_lista)


## Iteración sobre listas
otra_lista = [5, 3, 8, 6, 2]
for elemento in otra_lista:
    print("Elemento:", elemento)
print("Iteración sobre la lista terminada.")

## Uso de la función range() con listas
for i in range(len(otra_lista)):
    print(f"Índice: {i}, Elemento: {otra_lista[i]}")
print("Uso de la función range() con listas terminado.")

## Uso de la función enumerate() con listas
for indice, valor in enumerate(otra_lista):
    print(f"Índice: {indice}, Elemento: {valor}")
print("Uso de la función enumerate() con listas terminado.")







