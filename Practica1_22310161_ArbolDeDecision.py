# Definición de los datos
data = [
    {"Temperatura": "Alta", "Humedad": "Alta", "Nublado": "Sí", "Llevar_paraguas": "Sí"},
    {"Temperatura": "Alta", "Humedad": "Baja", "Nublado": "Sí", "Llevar_paraguas": "No"},
    {"Temperatura": "Baja", "Humedad": "Alta", "Nublado": "Sí", "Llevar_paraguas": "Sí"},
    {"Temperatura": "Baja", "Humedad": "Baja", "Nublado": "No", "Llevar_paraguas": "No"},
    {"Temperatura": "Alta", "Humedad": "Alta", "Nublado": "No", "Llevar_paraguas": "No"},
    {"Temperatura": "Baja", "Humedad": "Baja", "Nublado": "Sí", "Llevar_paraguas": "Sí"},
    {"Temperatura": "Alta", "Humedad": "Baja", "Nublado": "No", "Llevar_paraguas": "No"},
]

# Función para convertir las categorías en valores numéricos
def convertir_a_numerico(valor):
    if valor == "Alta":
        return 1
    elif valor == "Baja":
        return 0
    elif valor == "Sí":
        return 1
    elif valor == "No":
        return 0
    return valor

# Función para entrenar el árbol de decisión simple
def entrenar_arbol(data):
    # Separamos las características de la etiqueta
    X = []
    y = []
    
    for ejemplo in data:
        X.append([convertir_a_numerico(ejemplo["Temperatura"]),
                  convertir_a_numerico(ejemplo["Humedad"]),
                  convertir_a_numerico(ejemplo["Nublado"])])
        y.append(convertir_a_numerico(ejemplo["Llevar_paraguas"]))
    
    # Ahora tenemos dos listas: X (características) y y (etiquetas)
    # Simularemos un árbol de decisión con reglas basadas en la temperatura y el nublado

    # Árbol de decisión simple: primer nodo basado en la temperatura
    # Si la temperatura es alta, no llevará paraguas, si es baja, mirar el nublado
    def arbol_decision(temperatura, humedad, nublado):
        if temperatura == 1:  # Temperatura alta
            return "No"  # No llevar paraguas
        elif temperatura == 0:  # Temperatura baja
            if nublado == 1:  # Si está nublado
                return "Sí"  # Llevar paraguas
            else:
                return "No"  # No llevar paraguas
        return "No"

    return arbol_decision

# Entrenamos el árbol de decisión
arbol = entrenar_arbol(data)

# Paso 2: Hacer predicciones
# Nuevos datos para predecir si se debe llevar paraguas
nuevos_dias = [
    {"Temperatura": "Alta", "Humedad": "Baja", "Nublado": "No"},  # Día 1
    {"Temperatura": "Baja", "Humedad": "Alta", "Nublado": "Sí"},  # Día 2
    {"Temperatura": "Baja", "Humedad": "Baja", "Nublado": "No"},  # Día 3
]

# Predicciones
for i, dia in enumerate(nuevos_dias):
    respuesta = arbol(convertir_a_numerico(dia["Temperatura"]),
                      convertir_a_numerico(dia["Humedad"]),
                      convertir_a_numerico(dia["Nublado"]))
    print(f"Día {i + 1} - Llevar paraguas: {respuesta}")
