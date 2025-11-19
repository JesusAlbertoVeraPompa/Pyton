# Buenas Practicas de Variables


"""
1. Reglas Obligatorias (Sintaxis)
Si no sigues estas reglas, Python lanzará un error (SyntaxError) y tu programa no funcionará.

Caracteres permitidos: Letras (a-z, A-Z), números (0-9) y guiones bajos (_).

No pueden empezar con números:

✅ variable1
❌ 1variable

No usar espacios ni guiones medios:

✅ mi_variable
❌ mi variable o mi-variable

Case-sensitive (Distingue mayúsculas): edad, Edad y EDAD son tres variables diferentes.

Palabras reservadas: No puedes usar palabras clave del lenguaje (como if, class, return, True, def).

"""

"""
2. El Estándar de Oro: PEP 8
La comunidad de Python sigue la guía de estilo PEP 8. Para variables, la convención es clara:

A. Variables y Funciones: snake_case
Usa todo en minúsculas y separa las palabras con guiones bajos.

✅ nombre_usuario
✅ total_ventas

❌ nombreUsuario (esto es camelCase, común en Java/JS, pero no en Python)
❌ NombreUsuario (esto se reserva para Clases)

B. Constantes: UPPER_CASE
Si una variable no debería cambiar nunca (es una constante), usa mayúsculas sostenidas.

✅ PI = 3.1416
✅ MAX_CONNECTIONS = 100

C. Variables "Privadas": _guion_bajo
Un guion bajo al inicio indica que la variable es para uso interno (convención fuerte, aunque no bloquea el acceso).

✅ _configuracion_interna
"""

"""
3. Buenas Prácticas Semánticas (Legibilidad)
Más allá de la sintaxis, el nombre debe explicar qué contiene la variable.

Sé descriptivo, no críptico
El nombre debe responder a la pregunta "¿Qué es esto?" sin necesidad de leer el código circundante.

Malo: d = 7 (¿Qué es d?)
Bueno: dias_semana = 7
Malo: val = get_val()
Bueno: saldo_actual = obtener_saldo()

Booleans (Verdadero/Falso)
Los nombres de variables booleanas deben sonar como preguntas de Sí/No. Usa prefijos como is, has, can (o es, tiene en español).

✅ is_active / es_activo
✅ has_errors / tiene_errores

❌ active (¿Es el estado activo o una función para activar?)

Colecciones (Listas, Tuplas)
Si la variable contiene múltiples elementos, usa el plural.

✅ usuarios = ['Ana', 'Luis']
❌ usuario = ['Ana', 'Luis'] (Confuso, parece uno solo)
"""

"""
Evitar	                    Por qué	                                                                                Ejemplo malo
Nombres de una sola letra	Excepto en matemáticas o iteradores (i, j, x, y), no aportan significado.	            a = 500
Caracteres confusos	        La letra l (ele minúscula), I (i mayúscula) y O (o mayúscula) se confunden con 1 y 0.	l = 1
Nombres genéricos	        No dicen nada sobre el dato.	                                                        data, info, temp, cosa
Notación Húngara	        No pongas el tipo de dato en el nombre (Python es dinámico).	                        str_nombre, lista_precios (Mejor: nombre, precios)
"""

"""
5. ¿Inglés o Español?
Esta es una duda común.

Proyectos Personales/Locales: Español está bien.

Proyectos Open Source/Profesionales: Inglés es el estándar mundial. La mayoría de las librerías están en inglés, y mezclar idiomas (calcular_tax o user_edad) se ve desordenado.

Consejo: Elige un idioma y mantente fiel a él en todo el proyecto.
"""

"""
# ❌ MALO
x = "Juan"              # ¿Qué es x?
Lista = ["a", "b"]      # No usar Mayúscula inicial
miVar = 10              # No usar camelCase
flag = True             # Nombre vago

# ✅ BUENO
nombre_cliente = "Juan" # snake_case y descriptivo
letras = ["a", "b"]     # Plural para listas
intentos_maximos = 10   # Explicativo
is_admin = True         # Booleano claro
"""

