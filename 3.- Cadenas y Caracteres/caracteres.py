#Caracteres especiales en Python

# Nueva línea
cadena_nueva_linea = "Primera línea\nSegunda línea"
print(cadena_nueva_linea)

# Tabulación
cadena_tabulacion = "Columna 1\tColumna 2\tColumna 3"
print(cadena_tabulacion)

# Comillas dentro de cadenas
cadena_comillas = "Ella dijo: \"Hola, ¿cómo estás?\""
print(cadena_comillas)

# Barra invertida
cadena_barra_invertida = "Ruta del archivo: C:\\Usuarios\\Juan\\Documentos"
print(cadena_barra_invertida)

# Caracteres Unicode
cadena_unicode = "Símbolo de corazón: \u2764"
print(cadena_unicode)

# Raw strings (cadenas crudas)
cadena_raw = r"Ruta del archivo sin escape: C:\Usuarios\Juan\Documentos"
print(cadena_raw)

# Formateo avanzado con f-strings
nombre = "Ana"
edad = 30
cadena_fstring = f"{nombre} tiene {edad} años."
print(cadena_fstring)

# Repetición de cadenas
cadena_repetida = "Hola! " * 3
print(cadena_repetida)

# Acceso a caracteres individuales
cadena_acceso = "Python"
primer_caracter = cadena_acceso[0]
print("Primer carácter de 'Python':", primer_caracter)
