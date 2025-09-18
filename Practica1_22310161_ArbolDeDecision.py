import pandas as pd
import matplotlib.pyplot as plt

# Paso 1: Crear un conjunto de datos de ejemplo
data = {
    "Temperatura": ["Alta", "Alta", "Baja", "Baja", "Alta", "Baja", "Alta", "Baja", "Alta", "Baja"],
    "Humedad": ["Alta", "Baja", "Alta", "Baja", "Alta", "Alta", "Baja", "Baja", "Baja", "Alta"],
    "Nublado": ["Sí", "Sí", "No", "No", "Sí", "Sí", "No", "Sí", "No", "Sí"],
    "Llevar_paraguas": ["Sí", "No", "Sí", "No", "Sí", "Sí", "No", "No", "No", "Sí"]
}

# Convertimos los datos a un DataFrame (opcional, pero útil)
df = pd.DataFrame(data)

# Paso 2: El "entrenamiento" manual del árbol de decisión
# Basado en la lógica de los datos de ejemplo, las reglas parecen ser:
# 1. Si la Humedad es Alta y la Temperatura es Baja, llevas paraguas.
# 2. Si la Humedad es Alta y la Temperatura es Alta, llevas paraguas.
# 3. Si la Humedad es Baja y la Temperatura es Alta, NO llevas paraguas.
# 4. Si la Humedad es Baja y la Temperatura es Baja, NO llevas paraguas.
# En este caso, la variable "Nublado" no parece ser un factor decisivo.
# Concluimos que la Humedad es el factor principal en este set de datos simplificado.

def predecir_paraguas(temperatura, humedad, nublado):
    """
    Función que simula un árbol de decisión simple con lógica if/else.
    """
    if humedad == "Alta":
        return "Sí"
    else:  # Humedad es Baja
        return "No"

# Paso 3: Realizar predicciones con la nueva lógica
# Nuevos días para predecir (usamos los valores de texto originales)
nuevos_dias = [
    {"Temperatura": "Alta", "Humedad": "Baja", "Nublado": "No"},  # Día 1
    {"Temperatura": "Baja", "Humedad": "Alta", "Nublado": "Sí"}   # Día 2
]

print("---")
# Predicción
for i, dia in enumerate(nuevos_dias):
    prediccion = predecir_paraguas(dia["Temperatura"], dia["Humedad"], dia["Nublado"])
    print(f"Día {i+1} - Llevar paraguas: {prediccion}")

# Nota: La visualización del árbol con matplotlib no es posible sin scikit-learn.
# El código para graficar se ha eliminado.
