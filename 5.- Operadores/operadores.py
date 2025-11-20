# Operadores en Python

## Aritméticos
a = 10
b = 3
suma = a + b  # Suma
resta = a - b  # Resta
multiplicacion = a * b  # Multiplicación
division = a / b  # División
modulo = a % b  # Módulo
potencia = a**b  # Potencia
print("Aritméticos:")
print(
    f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}, Módulo: {modulo}, Potencia: {potencia}"
)

## Asignación
x = 5
x += 2  # Equivalente a x = x + 2
x *= 3  # Equivalente a x = x * 3
print("\nAsignación:")
print(f"Valor de x después de asignaciones: {x}")

## Comparación
c1 = a == b  # Igualdad
c2 = a != b  # Desigualdad
c3 = a > b  # Mayor que
c4 = a < b  # Menor que
c5 = a >= b  # Mayor o igual que
c6 = a <= b  # Menor o igual que
print("\nComparación:")
print(
    f"Igualdad: {c1}, Desigualdad: {c2}, Mayor que: {c3}, Menor que: {c4}, Mayor o igual que: {c5}, Menor o igual que: {c6}"
)
## Lógicos
l1 = (a > b) and (b > 0)  # AND lógico
l2 = (a > b) or (b < 0)  # OR lógico
l3 = not (a > b)  # NOT lógico
print("\nLógicos:")
print(f"AND lógico: {l1}, OR lógico: {l2}, NOT lógico: {l3}")
## Bit a bit
bit1 = a & b  # AND bit a bit
bit2 = a | b  # OR bit a bit
bit3 = a ^ b  # XOR bit a bit
bit4 = ~a  # NOT bit a bit
bit5 = a << 1  # Desplazamiento a la izquierda
bit6 = a >> 1  # Desplazamiento a la derecha
print("\nBit a bit:")
print(
    f"AND bit a bit: {bit1}, OR bit a bit: {bit2}, XOR bit a bit: {bit3}, NOT bit a bit: {bit4}, Desplazamiento a la izquierda: {bit5}, Desplazamiento a la derecha: {bit6}"
)
## De pertenencia
lista = [1, 2, 3, 4, 5]
p1 = 3 in lista  # Pertenencia
p2 = 6 not in lista  # No pertenencia
print("\nDe pertenencia:")
print(f"3 in lista: {p1}, 6 not in lista: {p2}")
## De identidad
id1 = a is b  # Identidad
id2 = a is not b  # No identidad
print("\nDe identidad:")
print(f"a is b: {id1}, a is not b: {id2}")




