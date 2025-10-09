import json
import os

# --- Configuración del Archivo de Base de Datos ---
ARCHIVO_DATOS = "akinator_personajes_data.json"

def cargar_datos():
    """Carga los personajes desde el archivo JSON o devuelve un diccionario vacío si no existe."""
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    # Base de datos inicial si el archivo no existe
    return {
        "Harry Potter": {
            "es_humano": "si",
            "tiene_poderes_magicos": "si",
            "usa_lentes": "si",
            "es_protagonista_de_libros": "si",
            "vive_en_un_mundo_de_magia": "si",
            "tiene_una_cicatriz_famosa": "si"
        },
        "Superman": {
            "es_humano": "no",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "si",
            "es_protagonista_de_comics": "si",
            "vuela": "si",
            "es_un_superheroe": "si"
        },
        "Mickey Mouse": {
            "es_humano": "no",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_animal_animado": "si",
            "es_un_raton": "si",
            "usa_guantes_blancos": "si"
        }
    }

def guardar_datos(datos):
    """Guarda el diccionario de personajes en el archivo JSON."""
    with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print("\n✅ ¡Personaje nuevo guardado! ¡He aprendido algo! ✅")

def obtener_preguntas(personajes):
    """Genera una lista de preguntas únicas basadas en todas las características de la base de datos."""
    preguntas_unicas = set()
    for caracteristicas in personajes.values():
        for clave in caracteristicas.keys():
            preguntas_unicas.add(clave)
    
    # Lista predefinida para asegurar orden inicial y texto legible
    mapa_preguntas = {
        "es_humano": "¿Tu personaje es humano?",
        "tiene_poderes_magicos": "¿Tu personaje tiene poderes mágicos?",
        "usa_lentes": "¿Tu personaje usa lentes?",
        "es_protagonista_de_libros": "¿Tu personaje es protagonista de libros?",
        "vuela": "¿Tu personaje vuela?",
        "es_un_animal_animado": "¿Tu personaje es un animal animado?",
        # Puedes añadir más aquí, pero la función las generará automáticamente si aparecen en la base
    }

    # Combina las preguntas fijas con cualquier clave nueva
    lista_preguntas = []
    for clave in preguntas_unicas:
        texto = mapa_preguntas.get(clave, f"¿Tu personaje tiene la característica '{clave}'?")
        lista_preguntas.append((texto, clave))
        
    return lista_preguntas

# --------------------------------------------------------------------------------

def akinator_personajes_con_aprendizaje():
    print("🤖 ¡Bienvenido al Akinator con Aprendizaje! 🧠")
    print("Piensa en un personaje. Responderé 'si' o 'no'.")

    personajes = cargar_datos()
    preguntas = obtener_preguntas(personajes)
    posibles_personajes = list(personajes.keys())
    respuestas_usuario = {}
    
    # --- Bucle de Preguntas y Filtrado ---
    for pregunta_texto, clave_caracteristica in preguntas:
        if len(posibles_personajes) <= 1:
            break # Terminamos el bucle si solo queda una o ninguna opción

        # Filtra si la pregunta es relevante para lo que queda
        relevante = any(clave_caracteristica in personajes[p] for p in posibles_personajes)
        
        if not relevante:
            continue
            
        respuesta = input(f"\n{pregunta_texto} (si/no): ").lower()
        while respuesta not in ["si", "no"]:
            print("❌ Por favor, responde con 'si' o 'no'.")
            respuesta = input(f"{pregunta_texto} (si/no): ").lower()

        respuestas_usuario[clave_caracteristica] = respuesta

        # Aplicar el filtro: mantiene solo a los personajes que coinciden
        nuevos_posibles = []
        for p_nombre in posibles_personajes:
            p_caracteristicas = personajes[p_nombre]
            
            # 1. Si el personaje tiene la característica definida y coincide con la respuesta
            if clave_caracteristica in p_caracteristicas and p_caracteristicas[clave_caracteristica] == respuesta:
                nuevos_posibles.append(p_nombre)
            
            # 2. Si el personaje no tiene la característica definida y el usuario responde 'no'
            # Asumimos que si no está definido, la respuesta es "no tiene esa característica"
            elif clave_caracteristica not in p_caracteristicas and respuesta == 'no':
                 nuevos_posibles.append(p_nombre)

        posibles_personajes = nuevos_posibles
        
    # --- Fase de Adivinanza y Aprendizaje ---
    
    if len(posibles_personajes) == 1:
        # Adivinanza exitosa
        personaje_adivinado = posibles_personajes[0]
        print(f"\n💡 ¡Adiviné! Tu personaje es {personaje_adivinado}.")
        respuesta_final = input("¿Es correcto? (si/no): ").lower()
        if respuesta_final == "si":
            print("🎉 ¡Lo logré! ¡Soy un genio!")
        else:
            print("😔 Vaya, me equivoqué. ¡Enséñame quién es para que aprenda!")
            aprender_personaje(personajes, respuestas_usuario) # LLAMA A LA FUNCIÓN DE APRENDIZAJE

    else:
        # Adivinanza fallida o personaje no encontrado
        print("\n😥 ¡No lo pude adivinar! No tengo ese personaje en mi base de datos.")
        aprender_personaje(personajes, respuestas_usuario) # LLAMA A LA FUNCIÓN DE APRENDIZAJE

def aprender_personaje(personajes, respuestas_usuario):
    """Guía al usuario para añadir el personaje no adivinado a la base de datos."""
    
    # 1. Pedir el nombre del nuevo personaje
    nombre_nuevo = input("¿Cuál era el nombre de tu personaje?: ").strip()
    if not nombre_nuevo:
        print("Operación cancelada.")
        return

    # 2. Iniciar la recolección de características
    nuevas_caracteristicas = {}
    
    # Usar todas las respuestas ya dadas
    for clave, respuesta in respuestas_usuario.items():
        nuevas_caracteristicas[clave] = respuesta
        
    # 3. Preguntar por las características restantes de la base de datos
    print("\nAhora, dime las características de este nuevo personaje. ¡Así aprenderé!")
    
    # Obtener todas las claves únicas de características de toda la base
    todas_las_claves = set()
    for caracteristicas in personajes.values():
        todas_las_claves.update(caracteristicas.keys())

    # Preguntar por las que NO se preguntaron antes o que no tienen respuesta
    for clave_caracteristica in todas_las_claves:
        if clave_caracteristica not in nuevas_caracteristicas:
            # Crea un texto de pregunta legible si es una clave nueva
            texto_pregunta = clave_caracteristica.replace('_', ' ').capitalize()
            
            respuesta = input(f"¿Tu personaje '{nombre_nuevo}' es {texto_pregunta}? (si/no/omite): ").lower()
            if respuesta in ["si", "no"]:
                nuevas_caracteristicas[clave_caracteristica] = respuesta
            # Si responde 'omite' (o cualquier otra cosa), se salta y esa característica no se guarda para el personaje

    # 4. Guardar el nuevo personaje y las características
    personajes[nombre_nuevo] = nuevas_caracteristicas
    guardar_datos(personajes)

# Ejecutar el juego
if __name__ == "__main__":
    akinator_personajes_con_aprendizaje()
