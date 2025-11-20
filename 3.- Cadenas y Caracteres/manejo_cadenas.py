# Manejo de Cadenas en Python

nombre = "Juan"
edad = 30
saludo = "Hola, ¿Como estas?"
frase_completa = saludo + " " + nombre
print(frase_completa)


# Uso de comillas simples y dobles
comillas_simples = "Esto es una cadena con comillas simples"
comillas_dobles = "Esto es una cadena con comillas dobles"
print(comillas_simples)
print(comillas_dobles)

# Cadenas multilínea
cadena_multilinea = """Esta es una cadena
que abarca varias líneas.
Puedes escribir tanto como quieras."""
print(cadena_multilinea)


# Acceso a caracteres individuales
cadena_acceso = "Python"
primer_caracter = cadena_acceso[0]
print("Primer carácter de 'Python':", primer_caracter)


# Subcadenas (slicing)
subcadena = cadena_acceso[1:4]
print("Subcadena de 'Python' (índices 1 a 3):", subcadena)

# Longitud de una cadena
longitud_cadena = len(cadena_acceso)
print("Longitud de 'Python':", longitud_cadena)

# Conversión a mayúsculas y minúsculas
cadena_mayusculas = cadena_acceso.upper()
cadena_minusculas = cadena_acceso.lower()
print("Mayúsculas:", cadena_mayusculas)
print("Minúsculas:", cadena_minusculas)

# Reemplazo de subcadenas
cadena_reemplazo = cadena_acceso.replace("thon", "tón")
print("Reemplazo en 'Python':", cadena_reemplazo)

# División de cadenas
cadena_dividida = "manzana,banana,naranja".split(",")
print("Cadenas divididas:", cadena_dividida)

# Unión de cadenas
cadena_unida = " - ".join(cadena_dividida)
print("Cadenas unidas:", cadena_unida)

# Búsqueda de subcadenas
indice_subcadena = cadena_acceso.find("tho")
print("Índice de 'tho' en 'Python':", indice_subcadena)

# Verificación de prefijos y sufijos
es_prefijo = cadena_acceso.startswith("Py")
es_sufijo = cadena_acceso.endswith("on")
print("¿'Python' empieza con 'Py'?", es_prefijo)
print("¿'Python' termina con 'on'?", es_sufijo)

# Eliminación de espacios en blanco
cadena_espacios = "   Hola Mundo   "
cadena_sin_espacios = cadena_espacios.strip()
print("Cadena sin espacios:", cadena_sin_espacios)

# Formateo con el método format()
cadena_format = "Nombre: {}, Edad: {}".format(nombre, edad)
print(cadena_format)

# Cadenas f-strings con expresiones
cadena_fstring_expresion = f"En 5 años, {nombre} tendrá {edad + 5} años."
print(cadena_fstring_expresion)

# Cadenas multilínea con paréntesis
cadena_multilinea_parentesis = (
    "Esta es una cadena que abarca " "varias líneas usando paréntesis."
)
print(cadena_multilinea_parentesis)

# Cadenas vacías
cadena_vacia = ""
print("Cadena vacía:", cadena_vacia)

# Concatenación con join para listas
lista_palabras = ["Python", "es", "genial"]
cadena_concatenada = " ".join(lista_palabras)
print("Cadena concatenada:", cadena_concatenada)

# Cadenas formateadas con alineación
cadena_alineada = f"|{'Izquierda':<10}|{'Centro':^10}|{'Derecha':>10}|"
print("Cadenas alineadas:\n", cadena_alineada)

# Uso de f-strings para formateo numérico
numero = 3.14159265
cadena_numero_formateado = f"Número formateado: {numero:.2f}"
print(cadena_numero_formateado)

# Escape de caracteres especiales en f-strings
cadena_fstring_escape = f"Comillas dobles: \" y comillas simples: '"
print(cadena_fstring_escape)

# Cadenas con expresiones matemáticas en f-strings
cadena_fstring_matematicas = f"El área de un círculo con radio 5 es: {3.1416 * 5**2}"
print(cadena_fstring_matematicas)


# Cadenas con Concatenación y Repetición
cadena_saludo = "Hola! " * 3
print(cadena_saludo)
cadena_nombre = "Juan"
cadena_completa = cadena_saludo + cadena_nombre
print(cadena_completa)

# Cadenas con Métodos Incorporados
cadena_ejemplo = "  Python es Genial  "
print("Original:", cadena_ejemplo)
print("Mayúsculas:", cadena_ejemplo.upper())
print("Minúsculas:", cadena_ejemplo.lower())
print("Eliminar espacios:", cadena_ejemplo.strip())
print(
    "Reemplazar 'Genial' por 'Increíble':",
    cadena_ejemplo.replace("Genial", "Increíble"),
)
print("Dividir por espacios:", cadena_ejemplo.split())

# Cadenas con Formateo
nombre = "Ana"
edad = 28
cadena_formateada = f"{nombre} tiene {edad} años."
print(cadena_formateada)
cadena_formateada2 = "Nombre: {}, Edad: {}".format(nombre, edad)
print(cadena_formateada2)

# Cadenas con Acceso a Caracteres e Índices
