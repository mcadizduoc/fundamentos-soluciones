# simulador_ecosistema.py
import random

# Inicialización de variables para mantener un seguimiento del estado del ecosistema
poblacion_conejos = 0
poblacion_zorros = 0
cantidad_vegetacion = 0
condicion_climatica = 0

# Variables para controlar la simulación
ciclo_actual = 0
ciclos_equilibrio = 0
MAX_CICLOS = 50
simulacion_activa = True

# Solicitar datos al usuario
es_informacion_valida = False

while es_informacion_valida == False:
    try:
        poblacion_conejos = int(input("Ingrese la población inicial de conejos: "))
        poblacion_zorros = int(input("Ingrese la población inicial de zorros: "))
        cantidad_vegetacion = int(input("Ingrese la cantidad inicial de vegetación (unidades): "))
        condicion_climatica = int(input("Ingrese la condición climática inicial (1: soleado, 2: lluvioso, 3: sequía, 4: tormenta): "))
        
        # Validar que los valores sean positivos y que la condición climática esté en el rango correcto
        if poblacion_conejos < 0 or poblacion_zorros < 0 or cantidad_vegetacion < 0:
            print("Las poblaciones y la vegetación deben ser valores positivos.")
            continue
        
        if condicion_climatica < 1 or condicion_climatica > 4:
            print("La condición climática debe ser un número entre 1 y 4.")
            continue
            
        es_informacion_valida = True
    except ValueError:
        print("Error con la información ingresada. Por favor, ingrese solo números enteros.")

# Definir umbrales y capacidades máximas
UMBRAL_VEGETACION = 20  # Si la vegetación cae por debajo de este valor, los conejos empiezan a morir
UMBRAL_CONEJOS = 5  # Si los conejos caen por debajo de este valor, los zorros empiezan a morir
MAX_VEGETACION = 500  # Capacidad máxima de vegetación
MAX_CONEJOS = 200  # Capacidad máxima de conejos
MAX_ZORROS = 50  # Capacidad máxima de zorros

# Factores de reproducción base
TASA_REPRODUCCION_CONEJOS = 0.2  # 20% de reproducción por ciclo
TASA_REPRODUCCION_ZORROS = 0.1  # 10% de reproducción por ciclo

# Factores de consumo
CONSUMO_VEGETACION_POR_CONEJO = 2  # Cada conejo consume 2 unidades de vegetación por ciclo
CONSUMO_CONEJOS_POR_ZORRO = 1  # Cada zorro come 1 conejo por ciclo

# Factores de crecimiento de vegetación según clima
CRECIMIENTO_VEGETACION_SOLEADO = 10
CRECIMIENTO_VEGETACION_LLUVIOSO = 20
CRECIMIENTO_VEGETACION_SEQUIA = 5
CRECIMIENTO_VEGETACION_TORMENTA = 15

clima_inicial = ""

crecimiento_base = 0

if condicion_climatica == 1:
    clima_inicial = 'Soleado'
    crecimiento_base = CRECIMIENTO_VEGETACION_SOLEADO
elif condicion_climatica == 2:
    clima_inicial = 'Lluvioso'
    crecimiento_base = CRECIMIENTO_VEGETACION_LLUVIOSO
elif condicion_climatica == 3:
    clima_inicial == 'Sequía'
    crecimiento_base = CRECIMIENTO_VEGETACION_SEQUIA
elif condicion_climatica == 4:
    clima_inicial = 'Tormenta'
    crecimiento_base = CRECIMIENTO_VEGETACION_TORMENTA

print("\n===== INICIO DE LA SIMULACIÓN DEL ECOSISTEMA =====")
print(f"Condiciones iniciales: {poblacion_conejos} conejos, {poblacion_zorros} zorros, {cantidad_vegetacion} vegetación, clima {clima_inicial}")

# Bucle principal de la simulación
while simulacion_activa == True and ciclo_actual < MAX_CICLOS:
    ciclo_actual += 1
    print(f"\n--- Ciclo {ciclo_actual} ---")
    
    # 1. Cambio climático aleatorio (20% de probabilidad)
    if random.random() < 0.2:  # random.random() devuelve un valor entre 0 y 1
        nuevo_clima = random.randint(1, 4)

        nombre_clima = ""

        if nuevo_clima == 1:
            nombre_clima = 'Soleado'
            crecimiento_base = CRECIMIENTO_VEGETACION_SOLEADO
        elif nuevo_clima == 2:
            nombre_clima = 'Lluvioso'
            crecimiento_base = CRECIMIENTO_VEGETACION_LLUVIOSO
        elif nuevo_clima == 3:
            nombre_clima == 'Sequía'
            crecimiento_base = CRECIMIENTO_VEGETACION_SEQUIA
        elif nuevo_clima == 4:
            nombre_clima = 'Tormenta'
            crecimiento_base = CRECIMIENTO_VEGETACION_TORMENTA

        if nuevo_clima != condicion_climatica:
            condicion_climatica = nuevo_clima
            print(f"El clima ha cambiado a: {nombre_clima}")
    
    
    # Ajuste por clima extremo
    if condicion_climatica == 3:  # Sequía
        crecimiento_base = crecimiento_base * 0.7  # Reducción adicional en sequía
    elif condicion_climatica == 4:  # Tormenta
        # 30% de probabilidad de daño a la vegetación en tormenta
        if random.random() < 0.3:
            daño = random.randint(5, 15)
            cantidad_vegetacion -= daño
            print(f"¡La tormenta ha dañado {daño} unidades de vegetación!")
    
    # Aplicar crecimiento con límite máximo
    cantidad_vegetacion += int(crecimiento_base)
    if cantidad_vegetacion > MAX_VEGETACION:
        cantidad_vegetacion = MAX_VEGETACION
    
    # 2. Eventos aleatorios (10% de probabilidad)
    if random.random() < 0.1:
        tipo_evento = random.randint(1, 3)
        
        if tipo_evento == 1:  # Enfermedad
            especie_afectada = random.randint(1, 2)
            if especie_afectada == 1 and poblacion_conejos > 0:  # Enfermedad en conejos
                perdida = int(poblacion_conejos * 0.15)  # 15% de mortalidad
                poblacion_conejos -= perdida
                print(f"¡Una enfermedad ha afectado a la población de conejos! -{perdida} conejos")
            elif especie_afectada == 2 and poblacion_zorros > 0:  # Enfermedad en zorros
                perdida = int(poblacion_zorros * 0.15)  # 15% de mortalidad
                poblacion_zorros -= perdida
                print(f"¡Una enfermedad ha afectado a la población de zorros! -{perdida} zorros")
        
        elif tipo_evento == 2:  # Migración
            especie_migrante = random.randint(1, 2)
            if especie_migrante == 1:  # Migración de conejos
                cantidad = random.randint(1, 5)
                poblacion_conejos += cantidad
                print(f"¡{cantidad} conejos han migrado al ecosistema!")
            else:  # Migración de zorros
                cantidad = random.randint(1, 3)
                poblacion_zorros += cantidad
                print(f"¡{cantidad} zorros han migrado al ecosistema!")
        
        elif tipo_evento == 3 and condicion_climatica == 3:  # Incendio (solo en sequía)
            daño_vegetacion = int(cantidad_vegetacion * 0.3)  # 30% de daño a la vegetación
            cantidad_vegetacion -= daño_vegetacion
            poblacion_conejos = int(poblacion_conejos * 0.8)  # 20% de mortalidad en conejos
            poblacion_zorros = int(poblacion_zorros * 0.9)  # 10% de mortalidad en zorros
            print(f"¡Un incendio ha devastado el ecosistema! -{daño_vegetacion} vegetación, -{int(poblacion_conejos * 0.2)} conejos, -{int(poblacion_zorros * 0.1)} zorros")
    
    # 3. Alimentación de los conejos
    consumo_total = poblacion_conejos * CONSUMO_VEGETACION_POR_CONEJO
    if consumo_total <= cantidad_vegetacion:
        cantidad_vegetacion -= consumo_total
    else:
        # No hay suficiente vegetación para todos
        conejos_alimentados = cantidad_vegetacion // CONSUMO_VEGETACION_POR_CONEJO
        conejos_hambrientos = poblacion_conejos - conejos_alimentados
        
        # Los conejos hambrientos tienen una probabilidad de morir
        muertes_conejos = int(conejos_hambrientos * 0.5)  # 50% de los hambrientos mueren
        poblacion_conejos -= muertes_conejos
        
        if muertes_conejos > 0:
            print(f"{muertes_conejos} conejos han muerto por falta de alimento")
        
        cantidad_vegetacion = 0  # Se consume toda la vegetación disponible
    
    # 4. Caza de zorros
    if poblacion_zorros > 0:
        conejos_cazados = min(poblacion_conejos, poblacion_zorros * CONSUMO_CONEJOS_POR_ZORRO)
        poblacion_conejos -= conejos_cazados
        
        # Si no hay suficientes conejos para todos los zorros
        if conejos_cazados < poblacion_zorros * CONSUMO_CONEJOS_POR_ZORRO:
            zorros_hambrientos = poblacion_zorros - (conejos_cazados // CONSUMO_CONEJOS_POR_ZORRO)
            # Suponemos al menos un zorro debe morir de hambre
            muertes_zorros = 1
            if zorros_hambrientos > 1:
                muertes_zorros = int(zorros_hambrientos * 0.3)  # 30% de los hambrientos mueren
            
            poblacion_zorros -= muertes_zorros
            
            if muertes_zorros > 0:
                print(f"{muertes_zorros} zorros han muerto por falta de presas")
    
    # 5. Reproducción de conejos
    # La tasa depende del clima y la disponibilidad de vegetación
    tasa_reproduccion = TASA_REPRODUCCION_CONEJOS
    
    # Modificar tasa según el clima
    if condicion_climatica == 2:  # Lluvioso
        tasa_reproduccion *= 1.2  # Mejor reproducción con más vegetación
    elif condicion_climatica == 3:  # Sequía
        tasa_reproduccion *= 0.8  # Menor reproducción con menos recursos
    
    # Modificar tasa según la vegetación disponible
    if cantidad_vegetacion < UMBRAL_VEGETACION:
        tasa_reproduccion *= 0.5  # Menor reproducción con poca vegetación
    
    # Calcular nuevos nacimientos
    nuevos_conejos = int(poblacion_conejos * tasa_reproduccion)
    poblacion_conejos += nuevos_conejos
    
    # Limitar por capacidad máxima
    if poblacion_conejos > MAX_CONEJOS:
        exceso = poblacion_conejos - MAX_CONEJOS
        poblacion_conejos = MAX_CONEJOS
        print(f"El ecosistema no puede sostener a {exceso} conejos más. Población limitada a {MAX_CONEJOS}.")
    
    # 8. Reproducción de zorros
    # La tasa depende de la disponibilidad de conejos
    tasa_reproduccion = TASA_REPRODUCCION_ZORROS
    
    # Modificar tasa según disponibilidad de presas
    if poblacion_conejos < UMBRAL_CONEJOS:
        tasa_reproduccion *= 0.5  # Menor reproducción con pocas presas
    
    # Calcular nuevos nacimientos
    nuevos_zorros = int(poblacion_zorros * tasa_reproduccion)
    poblacion_zorros += nuevos_zorros
    
    # Limitar por capacidad máxima
    if poblacion_zorros > MAX_ZORROS:
        exceso = poblacion_zorros - MAX_ZORROS
        poblacion_zorros = MAX_ZORROS
        print(f"El ecosistema no puede sostener a {exceso} zorros más. Población limitada a {MAX_ZORROS}.")
    
    # Mostrar estadísticas del ciclo
    print(f"Vegetación: {cantidad_vegetacion} unidades")
    print(f"Población de conejos: {poblacion_conejos}")
    print(f"Población de zorros: {poblacion_zorros}")

    # 8. Verificar condiciones de terminación
    if (poblacion_conejos <= 0 or poblacion_zorros <= 0) and ciclo_actual >= 5: # Dejamos que a partir del quinto ciclo termine porque de otra manera siempre terminará con los conejos extintos
        print("\n¡Una especie se ha extinto!")
        if poblacion_conejos <= 0:
            print("Los conejos se han extinto.")
            poblacion_conejos = 0
        if poblacion_zorros <= 0:
            print("Los zorros se han extinto.")
            poblacion_zorros = 0
        simulacion_activa = False
