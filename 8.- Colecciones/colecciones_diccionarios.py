# Colecciones en Python

## Diccionarios
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("Diccionario original:", mi_diccionario)

# Acceder a elementos
print("Nombre:", mi_diccionario["nombre"])
print("Edad:", mi_diccionario.get("edad"))

# Agregar o modificar elementos
mi_diccionario["profesion"] = "Ingeniero"
print("Después de agregar profesion:", mi_diccionario)
mi_diccionario["edad"] = 31
print("Después de modificar edad:", mi_diccionario)

# Eliminar elementos
del mi_diccionario["ciudad"]
print("Después de eliminar ciudad:", mi_diccionario)
edad_eliminada = mi_diccionario.pop("edad")
print("Después de pop(edad):", mi_diccionario, "Edad eliminada:", edad_eliminada)

# Iteración sobre diccionarios
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
print("Iteración sobre el diccionario terminada.")

# Obtener listas de claves y valores
claves = list(mi_diccionario.keys())
valores = list(mi_diccionario.values())
print("Claves del diccionario:", claves)
print("Valores del diccionario:", valores)

# Comprobación de pertenencia
pertenencia = "nombre" in mi_diccionario
print("'nombre' in mi_diccionario:", pertenencia)
no_pertenencia = "ciudad" not in mi_diccionario
print("'ciudad' not in mi_diccionario:", no_pertenencia)
print("Colecciones de diccionarios en Python completadas.")

# Funciones útiles para diccionarios
mi_diccionario2 = {"a": 1, "b": 2, "c": 3}
print("Diccionario para funciones útiles:", mi_diccionario2)
print("Longitud del diccionario:", len(mi_diccionario2))
print("Diccionario convertido a lista de claves:", list(mi_diccionario2))
print("Diccionario convertido a lista de valores:", list(mi_diccionario2.values()))
print("Diccionario convertido a lista de ítems:", list(mi_diccionario2.items()))
print("Colecciones de diccionarios en Python completadas.")

# Operaciones con Diccionarios
mi_diccionario3 = {"x": 10, "y": 20}
mi_diccionario4 = {"y": 30, "z": 40}
mi_diccionario3.update(mi_diccionario4)  # Combina diccionarios, sobrescribe claves
print("Después de update (combinación):", mi_diccionario3)
print("Colecciones de diccionarios en Python completadas.")

