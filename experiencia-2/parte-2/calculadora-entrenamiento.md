## Resolución ejercicio calculadora entrenamiento

En este documento pueden encontrar un paso a paso de cómo resolver el primer ejercicio de la "calculadora de entrenamiento", la solución la encontrarán en esta misma carpeta. En este archivo iré explicando paso a paso el cómo construir la solución.

Para resolver la base del ejercicio, primero necesitamos hacer los cálculos relacionados a las calorías base, el peso y la edad. B
ásicamente según los parámetros ingresados, tendríamos un "presupuesto" de calorías que debe ser utilizado en relación a las calorías consumidas en el día por el usuario.

En función de la edad y los objetivos vamos ajustando este "presupuesto" de tal manera que al final de los ajustes podamos calcular la diferencia entre las calorías consumidas en el día.
Si la cantidad resultante es positiva, significa que nos sobran calorías. Por lo tanto estamos por debajo de lo necesario. En caso contrario, estamos por encima de lo necesario. Finalmente si son el mismo número, entonces estamos equilibrados

```python
# calculadora_entrenamiento.py

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso: "))
objetivo = int(input("Ingrese su objetivo: \n1) Perder peso\n2) Mantener peso\n3) Ganar masa muscular\n: "))
calorias_consumidas = int(input("Ingrese cantidad de calorías consumidas"))

calorias_base = 0

if 18 <= edad <= 30:
    calorias_base = 2000
elif 31 <= edad <= 50:
    calorias_base = 1800
elif 51 <= edad:
    calorias_base = 1600

# Ajuste de calorías por objetivo
if objetivo == 1: # Perder peso
    calorias_base -= 200
elif objetivo == 2: # Mantener peso
    calorias_base += 0
elif objetivo == 3: # Ganar masa muscular
    calorias_base += 500

# Ajuste de calorías según peso
# Supuesto: Cada 10 kilos exactos se hacen los cálculos:
# Ej: Si el usuario pesa 79 kilos, entonces no se quitan 100 calorías por 10 kilos sobre los 70
# Si el usuario pesa 51 kilos, sólo se le agregan 100 calorías, 
# ya que a pesar de estar 19 kilos debajo de 70, no son 20 exactos, solo se cuenta 10 kg

dif_peso = (peso - 70) // 10 # división entera según supuesto

if dif_peso > 0: # Peso por sobre los 70 kilos
    calorias_base -= 100 * dif_peso
elif dif_peso < 0: # Peso por debajo de los 70 kilos
    calorias_base += 100 * dif_peso

# Listos los ajustes, ahora calculamos la diferencia de calorías
dif_calorias = calorias_base - calorias_consumidas

if dif_calorias > 0: # Estamos por debajo del rango recomendado
    print("Se recomienda hacer actividades de fuerza")
elif dif_calorias < 0: # Estamos por sobre el rango recomendado
    print("Se recomienda hacer actividades aeróbicas")
else:
    print("Debes combinar actividades de fuerza y aeróbicas para mantener tus objetivos")
```

Es importante notar que se hace un supuesto en este ejercicio, el cual considera que a través de la división entera de 10 en la diferencia de pesos, ajustamos +100 o -100 calorías.
Esto quiere decir que si el usuario está 9 kilos por sobre el peso ideal, no cuenta. Al igual que si el usuario está 19 kilos por debajo, entonces solo cuenta los primeros 10 kilos, los otros 9 no cuentan.

### Ahora el plan de entrenamiento

Es importante que para este caso también tenemos supuestos, acá vamos a suponer los ejercicios que vamos a asignar (aeróbicos o de peso) y de cómo los distribuiremos por díam, de forma estática. Agregando al final esta parte del código

```python
for i in range(5): # Plan de 5 días
    ejercicio = ""
    series = 0
    repeticiones = 0
    minutos = 0
    if dif_calorias > 0:
        if i == 0:
            ejercicio = "curl de biceps"
            series = 3
            repeticiones = 8
        elif i == 1:
            ejercicio = "press banca"
            series = 4
            repeticiones = 6
        elif i == 2:
            ejercicio = "sentadillas con barra"
            series = 4
            repeticiones = 8
        elif i == 3:
            ejercicio = "face pulls"
            series = 4
            repeticiones = 14
        elif i == 4:
            ejercicio = "elevación de talones"
            series = 4
            repeticiones = 10
    elif dif_calorias < 0:
        if i == 0:
            ejercicio = "caminata"
            series = 1
            minutos = 30
        elif i == 1:
            ejercicio = "trote"
            series = 1
            minutos = 20
        elif i == 2:
            ejercicio = "sentadilla sin peso"
            series = 4
            repeticiones = 14 
        elif i == 3:
            ejercicio = "jumping jacks"
            series = 4
            repeticiones = 12
        elif i == 4:
            ejercicio = "burpees"
            series = 4
            repeticiones = 8
    else:
        if i == 0:
            ejercicio = "mancuernas"
            series = 4
            repeticiones = 6
        elif i == 1:
            ejercicio = "trote"
            series = 1
            minutos = 20 
        elif i == 2:
            ejercicio = "sentadillas con barra"
            series = 3
            repeticiones = 12
        elif i == 3:
            ejercicio = "jumping jacks"
            series = 3
            minutos = 1.5
        elif i == 4:
            ejercicio = "elevación de talones"
            series = 3
            repeticiones = 10
    
    mensaje_rutina = f"Para el día {i + 1} debes hacer { series } series del {ejercicio}"
    if repeticiones > 0:
        mensaje_rutina = f"{mensaje_rutina} x {repeticiones} repeticiones"
    elif minutos > 0:
        mensaje_rutina = f"{mensaje_rutina} por {minutos} minutos"
    
    print(mensaje_rutina)
```
### Calculando los días para alcanzar peso ideal

Para esta sección, necesitamos suponer el factor de perdida/ganancia de peso, de tal manera que podamos calcular correctamente la cantidad de días. 
En este caso arbitraimente se define que se pierden/ganan 5 kilos por semana. Resultando en el siguiente bloque de código:

```python
calcular_peso_ideal = int(input("Desea calcular en cuantos días podría su peso ideal? 1) Sí 2) No: "))

if calcular_peso_ideal == 1:
    factor_peso = 5 # Supongamos que si el usuario sigue la rutina, pierde/gana 5 kilos por semana

    calculando_dias = True

    acumulador_peso = peso # Inicializamos el acumulador con el peso ingresado por el usuario
    contador_semanas = 0

    while calculando_dias == True:
        contador_semanas += 1
        if acumulador_peso >= 70:
            if acumulador_peso - factor_peso < 70: # Si bajamos por debajo de los 70 kilos, ajustamos para evitar errores
                acumulador_peso = 70
            else:
                acumulador_peso -= factor_peso
        elif acumulador_peso <= 70:
            if acumulador_peso + factor_peso > 70: # Si subimos por sobre los 70 kilos, ajustamos para evitar errores
                acumulador_peso = 70
            else:
                acumulador_peso  += factor_peso
        if acumulador_peso == 70: # Si alcanzamos el peso ideal, detenemos el while
            calculando_dias = False
        
    print(f"Para alcanzar tu peso ideal, debes seguir la rutina por alrededor de {contador_semanas * 7} días")
```

### Código completo (Sólo resolución del problema)

Si sumamos todo el código planteado, tendremos la solución base del problema. Asumiendo que el usuario ingresa toda la información correctamente.

```python
# calculadora entrenamiento.py

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso: "))
objetivo = int(input("Ingrese su objetivo: \n1) Perder peso\n2) Mantener peso\n3) Ganar masa muscular\n: "))
calorias_consumidas = int(input("Ingrese cantidad de calorías consumidas: "))

calorias_base = 0

if 18 <= edad <= 30:
    calorias_base = 2000
elif 31 <= edad <= 50:
    calorias_base = 1800
elif 51 <= edad:
    calorias_base = 1600

# Ajuste de calorías por objetivo
if objetivo == 1: # Perder peso
    calorias_base -= 200
elif objetivo == 2: # Mantener peso
    calorias_base += 0
elif objetivo == 3: # Ganar masa muscular
    calorias_base += 500

# Ajuste de calorías según peso
# Supuesto: Cada 10 kilos exactos se hacen los cálculos:
# Ej: Si el usuario pesa 79 kilos, entonces no se quitan 100 calorías por 10 kilos sobre los 70
# Si el usuario pesa 51 kilos, sólo se le agregan 100 calorías, 
# ya que a pesar de estar 19 kilos debajo de 70, no son 20 exactos, solo se cuenta 10 kg

dif_peso = (peso - 70) // 10 # división entera según supuesto

if dif_peso > 0: # Peso por sobre los 70 kilos
    calorias_base -= 100 * dif_peso
elif dif_peso > 0: # Peso por debajo de los 70 kilos
    calorias_base += 100 * dif_peso

# Listos los ajustes, ahora calculamos la diferencia de calorías
dif_calorias = calorias_base - calorias_consumidas

if dif_calorias > 0: # Estamos por debajo del rango recomendado
    print("Se recomienda hacer actividades de fuerza")
elif dif_calorias < 0: # Estamos por sobre el rango recomendado
    print("Se recomienda hacer actividades aeróbicas")
else:
    print("Debes combinar actividades de fuerza y aeróbicas para mantener tus objetivos")

for i in range(5): # Plan de 5 días
    ejercicio = ""
    series = 0
    repeticiones = 0
    minutos = 0
    if dif_calorias > 0:
        if i == 0:
            ejercicio = "curl de biceps"
            series = 3
            repeticiones = 8
        elif i == 1:
            ejercicio = "press banca"
            series = 4
            repeticiones = 6
        elif i == 2:
            ejercicio = "sentadillas con barra"
            series = 4
            repeticiones = 8
        elif i == 3:
            ejercicio = "face pulls"
            series = 4
            repeticiones = 14
        elif i == 4:
            ejercicio = "elevación de talones"
            series = 4
            repeticiones = 10
    elif dif_calorias < 0:
        if i == 0:
            ejercicio = "caminata"
            series = 1
            minutos = 30
        elif i == 1:
            ejercicio = "trote"
            series = 1
            minutos = 20
        elif i == 2:
            ejercicio = "sentadilla sin peso"
            series = 4
            repeticiones = 14 
        elif i == 3:
            ejercicio = "jumping jacks"
            series = 4
            repeticiones = 12
        elif i == 4:
            ejercicio = "burpees"
            series = 4
            repeticiones = 8
    else:
        if i == 0:
            ejercicio = "mancuernas"
            series = 4
            repeticiones = 6
        elif i == 1:
            ejercicio = "trote"
            series = 1
            minutos = 20 
        elif i == 2:
            ejercicio = "sentadillas con barra"
            series = 3
            repeticiones = 12
        elif i == 3:
            ejercicio = "jumping jacks"
            series = 3
            minutos = 1.5
        elif i == 4:
            ejercicio = "elevación de talones"
            series = 3
            repeticiones = 10
    
    mensaje_rutina = f"Para el día {i + 1} debes hacer { series } series del {ejercicio}"
    if repeticiones > 0:
        mensaje_rutina = f"{mensaje_rutina} x {repeticiones} repeticiones"
    elif minutos > 0:
        mensaje_rutina = f"{mensaje_rutina} por {minutos} minutos"
    
    print(mensaje_rutina)

calcular_peso_ideal = int(input("Desea calcular en cuantos días podría su peso ideal? 1) Sí 2) No: "))

if calcular_peso_ideal == 1:
    factor_peso = 5 # Supongamos que si el usuario sigue la rutina, pierde/gana 5 kilos por semana

    calculando_dias = True

    acumulador_peso = peso
    contador_semanas = 0

    while calculando_dias == True:
        contador_semanas += 1
        if acumulador_peso >= 70:
            if acumulador_peso - factor_peso < 70: # Si bajamos por debajo de los 70 kilos, ajustamos para evitar errores
                acumulador_peso = 70
            else:
                acumulador_peso -= factor_peso
        elif acumulador_peso <= 70:
            if acumulador_peso + factor_peso > 70: # Si subimos por sobre los 70 kilos, ajustamos para evitar errores
                acumulador_peso = 70
            else:
                acumulador_peso  += factor_peso
        if acumulador_peso == 70: # Si alcanzamos el peso ideal, detenemos el while
            calculando_dias = False
        
    print(f"Para alcanzar tu peso ideal, debes seguir la rutina por alrededor de {contador_semanas * 7} días")
```
