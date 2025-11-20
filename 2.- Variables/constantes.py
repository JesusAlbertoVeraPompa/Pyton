# Constantes en Python

# En Python, las constantes se definen utilizando variables con nombres en mayúsculas.
PI = 3.1416
MAX_CONNECTIONS = 100
API_KEY = "12345-ABCDE"

# Imprimir las constantes
print("Valor de PI:", PI)
print("Máximo de conexiones:", MAX_CONNECTIONS)
print("Clave de API:", API_KEY)


"""Buenas Prácticas para Nombres de Variables en Python
1. Reglas Básicas para Nombres de Variables
- Solo usar letras (a-z, A-Z), números (0-9) y guiones bajos (_).
- No empezar con números.
- No usar espacios ni guiones medios.
- Distinguir entre mayúsculas y minúsculas (case-sensitive).
- No usar palabras reservadas del lenguaje.
"""

"""2. Convenciones de Nomenclatura según PEP 8
- Variables y funciones: usar snake_case (minúsculas y guiones bajos).
- Constantes: usar UPPER_CASE (mayúsculas sostenidas).  
- Variables "privadas": usar un guion bajo al inicio (_variable).
"""

"""3. Buenas Prácticas Semánticas   
- Usar nombres descriptivos que expliquen el propósito de la variable.
- Evitar abreviaciones crípticas.
- Mantener consistencia en el estilo de nombres a lo largo del código.
"""
# Ejemplos de Buenas Prácticas
# Variables descriptivas
dias_semana = 7
total_ventas = 1500.75
usuario_activo = True

# Constantes
GRAVEDAD_TIERRA = 9.81  # m/s²
VELOCIDAD_LUZ = 299792458  # m/s
# Variable "privada"
_configuracion_interna = {"modo": "desarrollo"}
# Imprimir ejemplos
print("Días en una semana:", dias_semana)
print("Total de ventas:", total_ventas)
print("¿Usuario activo?", usuario_activo)
print("Gravedad en la Tierra:", GRAVEDAD_TIERRA)
print("Velocidad de la luz:", VELOCIDAD_LUZ)
print("Configuración interna:", _configuracion_interna)
