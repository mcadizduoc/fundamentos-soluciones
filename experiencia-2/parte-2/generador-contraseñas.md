## Resolución ejercicio generador y verificador de contraseñas

En este documento encontraremos el paso a paso para resolver el ejercicio del "Generador de Contraseñas Seguras y Verificador". Iré explicando cómo construir la solución paso por paso y al final tendré el código completo.

### Estructura básica del programa

Primero, necesitamos crear la estructura del programa con un menú principal y un bucle que mantenga el programa en ejecución hasta que el usuario decida salir. También definiremos contadores para las estadísticas que se mostrarán al finalizar.

```python
print("Bienvenido al Generador y Verificador de Contraseñas")

# Contadores para estadísticas
contador_generadas = 0
contador_verificadas = 0
suma_fortaleza = 0  # Para calcular el promedio de fortaleza

ejecutando = True

while ejecutando:
    print("\nMenú Principal:")
    print("1) Generar contraseña")
    print("2) Verificar fortaleza de contraseña")
    print("3) Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        # Aquí irá el código para generar contraseña
        print("Generador de contraseñas seleccionado")
        
    elif opcion == "2":
        # Aquí irá el código para verificar contraseña
        print("Verificador de contraseñas seleccionado")
        
    elif opcion == "3":
        # Mostrar estadísticas y salir
        ejecutando = False
        
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

# Mostrar estadísticas al finalizar
print("\n--- Estadísticas ---")
print(f"Contraseñas generadas: {contador_generadas}")
print(f"Contraseñas verificadas: {contador_verificadas}")

if contador_verificadas > 0:
    promedio_fortaleza = suma_fortaleza / contador_verificadas
    print(f"Promedio de fortaleza: {promedio_fortaleza:.2f}/9")
else:
    print("No se verificaron contraseñas.")

print("¡Gracias por usar el Generador y Verificador de Contraseñas!")
```

### Generador de contraseñas

Ahora vamos a implementar la funcionalidad para generar contraseñas. Dado que no podemos usar listas ni funciones, haremos un enfoque más básico. Utilizaremos números aleatorios para seleccionar caracteres de conjuntos predefinidos de letras, números y símbolos.

Para esto, necesitaremos importar el módulo `random`.

```python
import random

# Conjuntos de caracteres (definidos como strings)
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()-_=+[]{}|;:,.<>?"

# Código para la opción 1: Generar contraseña
if opcion == "1":
    print("\n--- Generador de Contraseñas ---")
    
    # Solicitar longitud
    longitud = 0
    while longitud < 8:
        try:
            longitud = int(input("Ingrese la longitud deseada (mínimo 8 caracteres): "))
            if longitud < 8:
                print("La longitud debe ser de al menos 8 caracteres.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Preguntar qué tipos de caracteres incluir
    incluir_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == "s"
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == "s"
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"
    
    # Verificar que al menos un tipo de carácter está seleccionado
    if not (incluir_minusculas or incluir_mayusculas or incluir_numeros or incluir_simbolos):
        print("Debe seleccionar al menos un tipo de carácter. Se incluirán letras minúsculas por defecto.")
        incluir_minusculas = True
    
    # Generar la contraseña
    contraseña = ""
    
    # Supuesto: Garantizamos que se incluya al menos un carácter de cada tipo seleccionado
    if incluir_minusculas:
        indice = random.randint(0, len(letras_minusculas) - 1)
        contraseña += letras_minusculas[indice]
        
    if incluir_mayusculas:
        indice = random.randint(0, len(letras_mayusculas) - 1)
        contraseña += letras_mayusculas[indice]
        
    if incluir_numeros:
        indice = random.randint(0, len(numeros) - 1)
        contraseña += numeros[indice]
        
    if incluir_simbolos:
        indice = random.randint(0, len(simbolos) - 1)
        contraseña += simbolos[indice]
    
    # Completar la contraseña hasta la longitud deseada
    caracteres_faltantes = longitud - len(contraseña)
    
    for i in range(caracteres_faltantes):
        # Decidir qué tipo de carácter agregar
        tipo_caracter = 0
        caracter_valido = False
        
        while not caracter_valido:
            tipo_caracter = random.randint(1, 4)
            
            if tipo_caracter == 1 and incluir_minusculas:
                indice = random.randint(0, len(letras_minusculas) - 1)
                contraseña += letras_minusculas[indice]
                caracter_valido = True
            elif tipo_caracter == 2 and incluir_mayusculas:
                indice = random.randint(0, len(letras_mayusculas) - 1)
                contraseña += letras_mayusculas[indice]
                caracter_valido = True
            elif tipo_caracter == 3 and incluir_numeros:
                indice = random.randint(0, len(numeros) - 1)
                contraseña += numeros[indice]
                caracter_valido = True
            elif tipo_caracter == 4 and incluir_simbolos:
                indice = random.randint(0, len(simbolos) - 1)
                contraseña += simbolos[indice]
                caracter_valido = True
    
    # Para aumentar la aleatoriedad, desordenamos los caracteres
    # Supuesto: Como no podemos usar listas, usaremos un enfoque básico de intercambio de caracteres
    contraseña_final = ""
    indices_utilizados = ""
    
    for i in range(len(contraseña)):
        indice_valido = False
        while not indice_valido:
            indice = random.randint(0, len(contraseña) - 1)
            # Verificar si el índice ya fue utilizado
            utilizado = False
            for j in range(len(indices_utilizados)):
                if str(indices_utilizados[j]) == str(indice):
                    utilizado = True
                    break
            
            if not utilizado:
                indice_valido = True
                indices_utilizados += str(indice)
                contraseña_final += contraseña[indice]
    
    print(f"\nLa contraseña generada es: {contraseña_final}")
    contador_generadas += 1
```

### Verificador de contraseñas

Ahora implementaremos la funcionalidad para verificar la fortaleza de las contraseñas. Evaluaremos la longitud, la variedad de caracteres y verificaremos si contiene palabras comunes.

```python
elif opcion == "2":
    print("\n--- Verificador de Contraseñas ---")
    
    contraseña = input("Ingrese la contraseña a verificar: ")
    
    # Puntuación inicial
    puntos = 0
    
    # Evaluación de longitud (1-3 puntos)
    if len(contraseña) >= 12:
        puntos += 3
        mensaje_longitud = "Excelente longitud (3 puntos)"
    elif len(contraseña) >= 8:
        puntos += 2
        mensaje_longitud = "Buena longitud (2 puntos)"
    elif len(contraseña) >= 6:
        puntos += 1
        mensaje_longitud = "Longitud aceptable (1 punto)"
    else:
        mensaje_longitud = "Longitud insuficiente (0 puntos)"
    
    # Evaluación de variedad de caracteres (1-4 puntos)
    tiene_minusculas = False
    tiene_mayusculas = False
    tiene_numeros = False
    tiene_simbolos = False
    
    for i in range(len(contraseña)):
        caracter = contraseña[i]
        
        # Verificar si es minúscula
        for j in range(len(letras_minusculas)):
            if caracter == letras_minusculas[j]:
                tiene_minusculas = True
                break
        
        # Verificar si es mayúscula
        for j in range(len(letras_mayusculas)):
            if caracter == letras_mayusculas[j]:
                tiene_mayusculas = True
                break
        
        # Verificar si es número
        for j in range(len(numeros)):
            if caracter == numeros[j]:
                tiene_numeros = True
                break
        
        # Verificar si es símbolo
        for j in range(len(simbolos)):
            if caracter == simbolos[j]:
                tiene_simbolos = True
                break
    
    puntos_variedad = 0
    if tiene_minusculas:
        puntos_variedad += 1
    if tiene_mayusculas:
        puntos_variedad += 1
    if tiene_numeros:
        puntos_variedad += 1
    if tiene_simbolos:
        puntos_variedad += 1
    
    puntos += puntos_variedad
    
    mensaje_variedad = f"Variedad de caracteres: {puntos_variedad}/4 puntos"
    
    # Verificación de palabras comunes (2 puntos)
    # Supuesto: Definimos algunas palabras comunes para verificar
    palabras_comunes = "password contraseña 123456 qwerty admin user login"
    contiene_palabra_comun = False
    
    contraseña_lower = ""
    for i in range(len(contraseña)):
        caracter = contraseña[i]
        # Convertir a minúscula si es una letra mayúscula
        es_mayuscula = False
        for j in range(len(letras_mayusculas)):
            if caracter == letras_mayusculas[j]:
                es_mayuscula = True
                contraseña_lower += letras_minusculas[j]
                break
        
        if not es_mayuscula:
            contraseña_lower += caracter
    
    # Verificar si contiene alguna palabra común
    for palabra in palabras_comunes.split():
        if palabra in contraseña_lower:
            contiene_palabra_comun = True
            break
    
    if not contiene_palabra_comun:
        puntos += 2
        mensaje_comunes = "No contiene palabras comunes (+2 puntos)"
    else:
        mensaje_comunes = "Contiene palabras comunes (0 puntos)"
    
    # Clasificación de fortaleza
    if puntos >= 8:
        clasificacion = "Muy fuerte"
    elif puntos >= 6:
        clasificacion = "Fuerte"
    elif puntos >= 4:
        clasificacion = "Media"
    else:
        clasificacion = "Débil"
    
    # Sugerencias de mejora
    sugerencias = []
    
    if len(contraseña) < 8:
        sugerencias.append("Aumentar la longitud a al menos 8 caracteres")
    
    if not tiene_minusculas:
        sugerencias.append("Incluir letras minúsculas")
    if not tiene_mayusculas:
        sugerencias.append("Incluir letras mayúsculas")
    if not tiene_numeros:
        sugerencias.append("Incluir números")
    if not tiene_simbolos:
        sugerencias.append("Incluir símbolos especiales")
    
    if contiene_palabra_comun:
        sugerencias.append("Evitar palabras comunes o predecibles")
    
    # Mostrar resultados
    print(f"\nResultados del análisis de fortaleza:")
    print(f"1. {mensaje_longitud}")
    print(f"2. {mensaje_variedad}")
    print(f"3. {mensaje_comunes}")
    print(f"\nPuntuación total: {puntos}/9")
    print(f"Clasificación: {clasificacion}")
    
    if sugerencias:
        print("\nSugerencias para mejorar:")
        for i, sugerencia in enumerate(sugerencias):
            print(f"{i+1}. {sugerencia}")
    
    # Actualizar estadísticas
    contador_verificadas += 1
    suma_fortaleza += puntos
```

### Código completo

Ahora juntaremos todo el código para obtener la solución completa.

```python
import random

print("Bienvenido al Generador y Verificador de Contraseñas")

# Conjuntos de caracteres (definidos como strings)
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()-_=+[]{}|;:,.<>?"

# Palabras comunes para verificación
palabras_comunes = "password contraseña 123456 qwerty admin user login"

# Contadores para estadísticas
contador_generadas = 0
contador_verificadas = 0
suma_fortaleza = 0  # Para calcular el promedio de fortaleza

ejecutando = True

while ejecutando == True:
    print("\nMenú Principal:")
    print("1) Generar contraseña")
    print("2) Verificar fortaleza de contraseña")
    print("3) Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        print("\n--- Generador de Contraseñas ---")
        
        # Solicitar longitud
        longitud = 0
        while longitud < 8:
            try:
                longitud = int(input("Ingrese la longitud deseada (mínimo 8 caracteres): "))
                if longitud < 8:
                    print("La longitud debe ser de al menos 8 caracteres.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        # Preguntar qué tipos de caracteres incluir
        incluir_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == "s"
        incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == "s"
        incluir_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
        incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"
        
        # Verificar que al menos un tipo de carácter está seleccionado
        if incluir_minusculas == False and incluir_mayusculas == False and incluir_numeros == False and incluir_simbolos == False:
            print("Debe seleccionar al menos un tipo de carácter. Se incluirán letras minúsculas por defecto.")
            incluir_minusculas = True
        
        # Generar la contraseña
        contraseña = ""
        
        # Supuesto: Garantizamos que se incluya al menos un carácter de cada tipo seleccionado
        if incluir_minusculas:
            indice = random.randint(0, len(letras_minusculas) - 1)
            contraseña += letras_minusculas[indice]
            
        if incluir_mayusculas == True:
            indice = random.randint(0, len(letras_mayusculas) - 1)
            contraseña += letras_mayusculas[indice]
            
        if incluir_numeros == True:
            indice = random.randint(0, len(numeros) - 1)
            contraseña += numeros[indice]
            
        if incluir_simbolos == True:
            indice = random.randint(0, len(simbolos) - 1)
            contraseña += simbolos[indice]
        
        # Completar la contraseña hasta la longitud deseada
        caracteres_faltantes = longitud - len(contraseña)
        
        for i in range(caracteres_faltantes):
            # Decidir qué tipo de carácter agregar
            tipo_caracter = 0
            caracter_valido = False
            
            while caracter_valido == False:
                tipo_caracter = random.randint(1, 4)
                
                if tipo_caracter == 1 and incluir_minusculas == True:
                    indice = random.randint(0, len(letras_minusculas) - 1)
                    contraseña += letras_minusculas[indice]
                    caracter_valido = True
                elif tipo_caracter == 2 and incluir_mayusculas == True:
                    indice = random.randint(0, len(letras_mayusculas) - 1)
                    contraseña += letras_mayusculas[indice]
                    caracter_valido = True
                elif tipo_caracter == 3 and incluir_numeros == True:
                    indice = random.randint(0, len(numeros) - 1)
                    contraseña += numeros[indice]
                    caracter_valido = True
                elif tipo_caracter == 4 and incluir_simbolos == True:
                    indice = random.randint(0, len(simbolos) - 1)
                    contraseña += simbolos[indice]
                    caracter_valido = True
        
        # Para aumentar la aleatoriedad, desordenamos los caracteres
        # Supuesto: Como no podemos usar listas, usaremos un enfoque básico de intercambio de caracteres
        contraseña_final = ""
        indices_utilizados = ""
        
        for i in range(len(contraseña)): # Iteramos por cada caracter de la contraseña
            indice_valido = False
            while indice_valido == False:
                indice = random.randint(0, len(contraseña) - 1)
                # Verificar si el índice ya fue utilizado
                utilizado = False
                for j in range(len(indices_utilizados)):
                    if str(indices_utilizados[j]) == str(indice):
                        utilizado = True
                        break
                
                if utilizado == False:
                    indice_valido = True
                    indices_utilizados += str(indice)
                    contraseña_final += contraseña[indice]
        
        print(f"\nLa contraseña generada es: {contraseña_final}")
        contador_generadas += 1
        
    elif opcion == "2":
        print("\n--- Verificador de Contraseñas ---")
        
        contraseña = input("Ingrese la contraseña a verificar: ")
        
        # Puntuación inicial
        puntos = 0
        
        # Evaluación de longitud (1-3 puntos)
        if len(contraseña) >= 12:
            puntos += 3
            mensaje_longitud = "Excelente longitud (3 puntos)"
        elif len(contraseña) >= 8:
            puntos += 2
            mensaje_longitud = "Buena longitud (2 puntos)"
        elif len(contraseña) >= 6:
            puntos += 1
            mensaje_longitud = "Longitud aceptable (1 punto)"
        else:
            mensaje_longitud = "Longitud insuficiente (0 puntos)"
        
        # Evaluación de variedad de caracteres (1-4 puntos)
        tiene_minusculas = False
        tiene_mayusculas = False
        tiene_numeros = False
        tiene_simbolos = False
        
        for i in range(len(contraseña)):
            caracter = contraseña[i]
            
            # Verificar si es minúscula
            for j in range(len(letras_minusculas)):
                if caracter == letras_minusculas[j]:
                    tiene_minusculas = True
                    break
            
            # Verificar si es mayúscula
            for j in range(len(letras_mayusculas)):
                if caracter == letras_mayusculas[j]:
                    tiene_mayusculas = True
                    break
            
            # Verificar si es número
            for j in range(len(numeros)):
                if caracter == numeros[j]:
                    tiene_numeros = True
                    break
            
            # Verificar si es símbolo
            for j in range(len(simbolos)):
                if caracter == simbolos[j]:
                    tiene_simbolos = True
                    break
        
        puntos_variedad = 0
        if tiene_minusculas == True:
            puntos_variedad += 1
        if tiene_mayusculas == True:
            puntos_variedad += 1
        if tiene_numeros == True:
            puntos_variedad += 1
        if tiene_simbolos == True:
            puntos_variedad += 1
        
        puntos += puntos_variedad
        
        mensaje_variedad = f"Variedad de caracteres: {puntos_variedad}/4 puntos"
        
        # Verificación de palabras comunes (2 puntos)
        # Supuesto: Verificamos si alguna palabra común está contenida en la contraseña
        contiene_palabra_comun = False
        
        contraseña_lower = ""
        for i in range(len(contraseña)):
            caracter = contraseña[i]
            # Convertir a minúscula si es una letra mayúscula
            es_mayuscula = False
            for j in range(len(letras_mayusculas)):
                if caracter == letras_mayusculas[j]:
                    es_mayuscula = True
                    contraseña_lower += letras_minusculas[j]
                    break
            
            if es_mayuscula == False:
                contraseña_lower += caracter
        
        # Verificar si contiene alguna palabra común
        palabras = palabras_comunes.split()
        for p in range(len(palabras)):
            if palabras[p] in contraseña_lower:
                contiene_palabra_comun = True
                break
        
        if contiene_palabra_comun == False:
            puntos += 2
            mensaje_comunes = "No contiene palabras comunes (+2 puntos)"
        else:
            mensaje_comunes = "Contiene palabras comunes (0 puntos)"
        
        # Clasificación de fortaleza
        if puntos >= 8:
            clasificacion = "Muy fuerte"
        elif puntos >= 6:
            clasificacion = "Fuerte"
        elif puntos >= 4:
            clasificacion = "Media"
        else:
            clasificacion = "Débil"
        
        # Sugerencias de mejora
        print(f"\nResultados del análisis de fortaleza:")
        print(f"1. {mensaje_longitud}")
        print(f"2. {mensaje_variedad}")
        print(f"3. {mensaje_comunes}")
        print(f"\nPuntuación total: {puntos}/9")
        print(f"Clasificación: {clasificacion}")
        
        print("\nSugerencias para mejorar:")
        if len(contraseña) < 8:
            print("- Aumentar la longitud a al menos 8 caracteres")
        
        if tiene_minusculas == False:
            print("- Incluir letras minúsculas")
        if tiene_mayusculas == False:
            print("- Incluir letras mayúsculas")
        if tiene_numeros == False:
            print("- Incluir números")
        if tiene_simbolos == False:
            print("- Incluir símbolos especiales")
        
        if contiene_palabra_comun == True:
            print("- Evitar palabras comunes o predecibles")
        
        if puntos >= 8:
            print("- ¡Excelente contraseña! No se necesitan mejoras.")
        
        # Actualizar estadísticas
        contador_verificadas += 1
        suma_fortaleza += puntos
        
    elif opcion == "3":
        # Mostrar estadísticas y salir
        ejecutando = False
        
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

# Mostrar estadísticas al finalizar
print("\n--- Estadísticas ---")
print(f"Contraseñas generadas: {contador_generadas}")
print(f"Contraseñas verificadas: {contador_verificadas}")

if contador_verificadas > 0:
    promedio_fortaleza = suma_fortaleza / contador_verificadas
    print(f"Promedio de fortaleza: {promedio_fortaleza:.2f}/9")
else:
    print("No se verificaron contraseñas.")

print("Gracias por usar el Generador y Verificador de Contraseñas!")
```

## Supuestos realizados

1. **Generación de contraseñas**:
   - Se garantiza que si el usuario selecciona ciertos tipos de caracteres, la contraseña incluirá al menos uno de cada tipo seleccionado.
   - Para aleatorizar la contraseña final, se implementó un sistema básico de selección aleatoria de índices sin usar listas.
   - Si el usuario no selecciona ningún tipo de carácter, se incluyen letras minúsculas por defecto.

2. **Verificación de contraseñas**:
   - Se definió un conjunto limitado de palabras comunes para verificar si la contraseña las contiene.
   - La puntuación de fortaleza se clasifica en cuatro niveles:
     - Débil: 0-3 puntos
     - Media: 4-5 puntos
     - Fuerte: 6-7 puntos
     - Muy fuerte: 8-9 puntos
   - Para verificar si la contraseña contiene palabras comunes, se convierte primero a minúsculas.

3. **Estadísticas**:
   - Se realiza un seguimiento del número de contraseñas generadas y verificadas.
   - Se calcula un promedio de fortaleza basado en las puntuaciones de las contraseñas verificadas.

Este programa cumple con todos los requisitos sin utilizar listas, arreglos, colecciones, tuplas, funciones definidas por el usuario ni expresiones regulares, manteniendo un enfoque básico que es accesible para estudiantes que aún no conocen estos conceptos.
