# Módulo de adquisición de conocimiento (Chat con base de datos simple)
import json

# Base de datos precargada de preguntas y respuestas
base_de_conocimiento = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "¿Cómo estás?": "Estoy bien, gracias por preguntar. ¿Y tú?",
    "¿De qué te gustaría hablar?": "Me gustaría hablar sobre cualquier cosa que te interese, ¿tú qué opinas?"
}

def obtener_respuesta(pregunta):
    # Buscar la respuesta en la base de datos
    respuesta = base_de_conocimiento.get(pregunta)
    if respuesta:
        return respuesta
    else:
        return None

def agregar_conocimiento(pregunta, respuesta):
    # Agregar nueva pregunta-respuesta a la base de datos
    base_de_conocimiento[pregunta] = respuesta
    print(f"Nuevo conocimiento agregado: '{pregunta}' -> '{respuesta}'")

def chat():
    print("¡Hola! Soy tu asistente de conocimiento. ¿Cómo puedo ayudarte hoy?")
    while True:
        # Solicitar la pregunta del usuario
        pregunta = input("Tu: ")
        
        # Salir del chat si el usuario dice "salir"
        if pregunta.lower() == "salir":
            print("¡Hasta luego!")
            break
        
        # Buscar la respuesta en la base de datos
        respuesta = obtener_respuesta(pregunta)
        
        if respuesta:
            print(f"Yo: {respuesta}")
        else:
            print("Lo siento, no conozco la respuesta a eso.")
            # Preguntar por una nueva respuesta para agregar
            nueva_respuesta = input(f"¿Cómo debería responder a '{pregunta}'? ")
            agregar_conocimiento(pregunta, nueva_respuesta)
            print("¡Gracias! Ahora conozco la respuesta.")

# Ejecutar el chat
chat()
