# Colecciones en Python

## Sets
mi_set = {1, 2, 3, 4, 5}
print("Set original:", mi_set)

# Agregar elementos
mi_set.add(6)
print("Después de add(6):", mi_set)
mi_set.add(3)  # No se agrega porque 3 ya está en el set
print("Después de add(3) (no cambia):", mi_set)

# Eliminar elementos
mi_set.remove(2)
print("Después de remove(2):", mi_set)
mi_set.discard(10)  # No genera error si el elemento no existe
print("Después de discard(10) (no cambia):", mi_set)
eliminado = mi_set.pop()  # Elimina un elemento arbitrario
print("Después de pop():", mi_set, "Elemento eliminado:", eliminado)

# Iteración sobre sets
for elemento in mi_set:
    print("Elemento:", elemento)
print("Iteración sobre el set terminada.")

# Operaciones de conjuntos
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b
interseccion = set_a & set_b
diferencia = set_a - set_b
diferencia_simetrica = set_a ^ set_b
print("Operaciones de conjuntos:")
print("Set A:", set_a)
print("Set B:", set_b)
print("Unión (A | B):", union)
print("Intersección (A & B):", interseccion)
print("Diferencia (A - B):", diferencia)
print("Diferencia simétrica (A ^ B):", diferencia_simetrica)

# Comprobación de pertenencia
pertenencia = 3 in mi_set
print("3 in mi_set:", pertenencia)
no_pertenencia = 10 not in mi_set
print("10 not in mi_set:", no_pertenencia)
print("Colecciones de sets en Python completadas.")

# Funciones útiles para sets
set_c = {1, 2, 2, 3, 4, 4, 5}
print("Set para funciones útiles (duplicados eliminados):", set_c)
print("Longitud del set:", len(set_c))
print("Set convertido a lista:", list(set_c))
print("Set convertido a tupla:", tuple(set_c))
print("Colecciones de sets en Python completadas.")

# Operaciones con Sets
set_d = {1, 2, 3}
set_e = {3, 4, 5}
set_d.update(set_e)  # Unión
print("Después de update (unión):", set_d)
set_d.intersection_update({2, 3, 4})  # Intersección
print("Después de intersection_update (intersección):", set_d)
set_d.difference_update({3})  # Diferencia
print("Después de difference_update (diferencia):", set_d)
set_d.symmetric_difference_update({1, 4})  # Diferencia simétrica
print("Después de symmetric_difference_update (diferencia simétrica):", set_d)
print("Colecciones de sets en Python completadas.")

# Subconjuntos y superconjuntos
set_f = {1, 2}
set_g = {1, 2, 3, 4}
es_subconjunto = set_f.issubset(set_g)
es_superconjunto = set_g.issuperset(set_f)
print("Set F:", set_f)
print("Set G:", set_g)
print("F es subconjunto de G:", es_subconjunto)
print("G es superconjunto de F:", es_superconjunto)
print("Colecciones de sets en Python completadas.")

