# Ciclos en Python

## Ciclo While
contador = 0
while contador < 5:
    print(f"Contador (while): {contador}")
    contador += 1
print("Ciclo While terminado.")

## Ciclo For
for i in range(5):
    print(f"Índice (for): {i}")
print("Ciclo For terminado.")

## Uso de break y continue
for numero in range(10):
    if numero == 5:
        print("Se encontró el número 5, saliendo del ciclo.")
        break  # Sale del ciclo cuando encuentra el número 5
    if numero % 2 == 0:
        print(f"Número par encontrado: {numero}, saltando al siguiente.")
        continue  # Salta los números pares
    print(f"Número impar procesado: {numero}")
print("Ciclo con break y continue terminado.")

## Ciclo anidado
for fila in range(3):
    for columna in range(3):
        print(f"Fila: {fila}, Columna: {columna}")
print("Ciclo anidado terminado.")

## Uso de else en ciclos
for n in range(3):
    print(f"Número: {n}")
else:
    print("Ciclo for completado sin interrupciones.")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1
else:
    print("Ciclo while completado sin interrupciones.")
print("Ciclos con else terminados.")

## Iteración sobre colecciones
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
print("Iteración sobre colecciones terminada.")

## Uso de la función range()
for numero in range(2, 10, 2):  # Desde 2 hasta 10 con paso de 2
    print(f"Número en rango: {numero}")
print("Uso de la función range() terminado.")

## Uso de la función enumerate()
for indice, valor in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {valor}")
print("Uso de la función enumerate() terminado.")

## Uso de la función zip()
colores = ["rojo", "verde", "azul"]
for fruta, color in zip(frutas, colores):
    print(f"Fruta: {fruta}, Color: {color}")
print("Uso de la función zip() terminado.")

## Uso de la función reversed()
for fruta in reversed(frutas):
    print(f"Fruta en orden inverso: {fruta}")
print("Uso de la función reversed() terminado.")

## Uso de la función sorted()
for fruta in sorted(frutas):
    print(f"Fruta ordenada: {fruta}")
print("Uso de la función sorted() terminado.")
print("Ciclos en Python completados.")



