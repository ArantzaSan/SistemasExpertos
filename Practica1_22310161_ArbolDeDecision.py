import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Paso 1: Crear un conjunto de datos de ejemplo
# Datos: [Temperatura (Alta/Baja), Humedad (Alta/Baja), Nublado (Sí/No)]
# Etiqueta: Llevar paraguas (Sí/No)
data = {
    "Temperatura": ["Alta", "Alta", "Baja", "Baja", "Alta", "Baja", "Alta", "Baja", "Alta", "Baja"],
    "Humedad": ["Alta", "Baja", "Alta", "Baja", "Alta", "Alta", "Baja", "Baja", "Baja", "Alta"],
    "Nublado": ["Sí", "Sí", "No", "No", "Sí", "Sí", "No", "Sí", "No", "Sí"],
    "Llevar_paraguas": ["Sí", "No", "Sí", "No", "Sí", "Sí", "No", "No", "No", "Sí"]
}

# Convertimos los datos a un DataFrame
df = pd.DataFrame(data)

# Paso 2: Preprocesar los datos
# Convertimos las columnas categóricas (Texto) en valores numéricos
df['Temperatura'] = df['Temperatura'].map({"Alta": 1, "Baja": 0})
df['Humedad'] = df['Humedad'].map({"Alta": 1, "Baja": 0})
df['Nublado'] = df['Nublado'].map({"Sí": 1, "No": 0})
df['Llevar_paraguas'] = df['Llevar_paraguas'].map({"Sí": 1, "No": 0})

# Paso 3: Separar las características (X) y la etiqueta (y)
X = df.drop("Llevar_paraguas", axis=1)  # Características
y = df["Llevar_paraguas"]  # Etiqueta

# Paso 4: Entrenar el árbol de decisión
clf = DecisionTreeClassifier(criterion="entropy")  # Usamos entropía como medida de impureza
clf = clf.fit(X, y)

# Paso 5: Visualizar el árbol de decisión
plt.figure(figsize=(10, 8))
tree.plot_tree(clf, filled=True, feature_names=X.columns, class_names=["No", "Sí"])
plt.show()

# Paso 6: Realizar predicciones
# Nuevos días para predecir
# Día 1: Temperatura alta, Humedad baja, No nublado
# Día 2: Temperatura baja, Humedad alta, Nublado
nuevos_dias = [
    [1, 0, 0],  # Día 1
    [0, 1, 1]   # Día 2
]

# Predicción
predicciones = clf.predict(nuevos_dias)
for i, pred in enumerate(predicciones):
    print(f"Día {i+1} - Llevar paraguas: {'Sí' if pred == 1 else 'No'}")

pip install scikit-learn
