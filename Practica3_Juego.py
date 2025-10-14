import json
import os

# --- Configuración del Archivo de Base de Datos ---
ARCHIVO_DATOS = "guess_personajes_data.json" 

def cargar_datos():
    """Carga los personajes desde el archivo JSON o devuelve un diccionario vacío si no existe."""
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    # Base de datos ampliada enfocada en personajes de Cartoon Network (y uno intruso corregido)
    return {
        "Ben Tennyson": {
            "es_humano": "si",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "si",
            "es_superheroe_cartoon": "si",
            "tiene_dispositivo_de_transformacion": "si",
            "viaja_en_el_tiempo": "no",
            "es_alienigena": "no",
            "es_un_villano": "no",
            "es_un_animal_animado": "no"
        },
        "Goku": {
            "es_humano": "no", # Es un Saiyajin
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "no",
            "es_superheroe_cartoon": "si",
            "vuela": "si",
            "usa_traje_naranja": "si",
            "es_alienigena": "si",
            "es_un_villano": "no",
            "es_un_animal_animado": "no"
        },
        "Dexter": {
            "es_humano": "si",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "si",
            "es_un_niño_protagonista": "si",
            "es_superheroe_cartoon": "no",
            "es_cientifico": "si",
            "tiene_un_laboratorio_secreto": "si",
            "es_rubio": "si",
            "es_un_villano": "no",
            "es_un_animal_animado": "no"
        },
        "Las Chicas Superpoderosas (Bombón)": {
            "es_humano": "si",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "si",
            "es_superheroe_cartoon": "si",
            "vuela": "si",
            "es_mujer": "si",
            "es_rubio": "no",
            "tiene_lazo_en_el_cabello": "si",
            "es_un_villano": "no",
            "es_un_animal_animado": "no"
        },
        "Coraje": {
            "es_humano": "no",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "no",
            "es_un_animal_animado": "si",
            "es_un_perro": "si",
            "vive_en_una_granja_aislada": "si",
            "es_rosa": "si",
            "es_un_villano": "no"
        },
        "Finn el Humano": {
            "es_humano": "si",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "si",
            "es_superheroe_cartoon": "no",
            "usa_sombrero": "si",
            "vive_en_un_mundo_post_apocaliptico": "si",
            "es_espadachin": "si",
            "es_un_villano": "no",
            "es_un_animal_animado": "no"
        },
        "Samurai Jack": {
            "es_humano": "si",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "no",
            "es_superheroe_cartoon": "no",
            "usa_sombrero": "no",
            "viaja_en_el_tiempo": "si",
            "es_espadachin": "si",
            "tiene_corte_de_pelo_cuadrado": "si",
            "es_un_villano": "no",
            "es_un_animal_animado": "no"
        },
        "Gumball Watterson": {
            "es_humano": "no",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "si",
            "es_un_animal_animado": "si",
            "es_un_gato": "si",
            "es_azul": "si",
            "tiene_hermano_pez": "si",
            "es_un_villano": "no"
        },
        "Vaca (Vaca y Pollito)": {
            "es_humano": "no",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "no",
            "es_un_animal_animado": "si",
            "vuela": "no",
            "es_una_vaca": "si",
            "viste_de_superheroina_a_veces": "si",
            "es_un_villano": "no"
        },
        "Steven Universe": {
            "es_humano": "si", # Mitad humano, mitad gema
            "tiene_poderes_magicos": "si", # Poderes de gema
            "usa_lentes": "no",
            "es_un_niño_protagonista": "si",
            "es_superheroe_cartoon": "si",
            "vuela": "no",
            "tiene_escudo_magico": "si",
            "toca_ukelele": "si",
            "es_un_villano": "no",
            "es_una_gema": "si",
            "es_un_animal_animado": "no"
        },
        # --- Nuevos Personajes de Cartoon Network ---
        "Mordecai": {
            "es_humano": "no",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "no",
            "es_superheroe_cartoon": "no",
            "es_un_animal_animado": "si",
            "es_un_pajaro": "si",
            "trabaja_en_un_parque": "si",
            "es_azul": "si",
            "es_un_villano": "no"
        },
        "Rigby": {
            "es_humano": "no",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "no",
            "es_superheroe_cartoon": "no",
            "es_un_animal_animado": "si",
            "es_un_mapache": "si",
            "trabaja_en_un_parque": "si",
            "es_marron": "si",
            "es_un_villano": "no"
        },
        "Aku": {
            "es_humano": "no",
            "tiene_poderes_magicos": "si",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "no",
            "es_superheroe_cartoon": "no",
            "es_un_villano": "si",
            "es_una_entidad_oscura": "si",
            "puede_cambiar_de_forma": "si",
            "es_negro_y_rojo": "si",
            "es_un_animal_animado": "no"
        },
        "Perla": {
            "es_humano": "no",
            "tiene_poderes_magicos": "si",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "no",
            "es_superheroe_cartoon": "si",
            "vuela": "no",
            "es_mujer": "si",
            "es_una_gema": "si",
            "usa_lanza": "si",
            "es_un_villano": "no",
            "es_un_animal_animado": "no"
        },
        "Padre (KND)": {
            "es_humano": "si",
            "tiene_poderes_magicos": "no",
            "usa_lentes": "no",
            "es_un_niño_protagonista": "no",
            "es_superheroe_cartoon": "no",
            "es_un_villano": "si",
            "fuma_puro": "si",
            "vive_en_una_mansion": "si",
            "odia_a_los_niños": "si",
            "es_un_animal_animado": "no"
        }
    }

def guardar_datos(datos):
    """Guarda el diccionario de personajes en el archivo JSON."""
    with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print("\n✅ ¡Personaje nuevo guardado! ¡Guess ha aprendido algo! ✅")

def obtener_preguntas(personajes):
    """Genera una lista de preguntas únicas basadas en todas las características de la base de datos."""
    preguntas_unicas = set()
    for caracteristicas in personajes.values():
        for clave in caracteristicas.keys():
            preguntas_unicas.add(clave)
    
    # Lista predefinida para asegurar orden inicial y texto legible de las claves comunes
    mapa_preguntas = {
        "es_humano": "¿Tu personaje es humano?",
        "es_un_niño_protagonista": "¿Tu personaje es un niño o adolescente protagonista?",
        "es_un_animal_animado": "¿Tu personaje es un animal animado (no humano)?",
        "tiene_poderes_magicos": "¿Tu personaje tiene poderes mágicos?",
        "es_superheroe_cartoon": "¿Tu personaje es un superhéroe o vigilante en la serie?",
        "es_un_villano": "¿Tu personaje es un villano principal o recurrente?", # ¡Nueva pregunta!
        "vuela": "¿Tu personaje vuela?",
        "usa_lentes": "¿Tu personaje usa lentes?",
        "es_mujer": "¿Tu personaje es una chica/mujer?",
        "es_alienigena": "¿Tu personaje es un alienígena?",
        "usa_sombrero": "¿Tu personaje usa sombrero o gorra?",
        "es_una_gema": "¿Tu personaje es una gema?", # ¡Nueva pregunta!
        # Las demás se generarán automáticamente
    }

    # Combina las preguntas fijas con cualquier clave nueva
    lista_preguntas = []
    # Usamos las claves del mapa_preguntas primero para un orden más lógico
    for clave, texto in mapa_preguntas.items():
        if clave in preguntas_unicas:
             lista_preguntas.append((texto, clave))
             preguntas_unicas.remove(clave)

    # Añadir las restantes claves que no estaban en el mapa predefinido
    for clave in preguntas_unicas:
        texto = f"¿Tu personaje tiene la característica: {clave.replace('_', ' ').capitalize()}?"
        lista_preguntas.append((texto, clave))
        
    return lista_preguntas

# --------------------------------------------------------------------------------
# Las funciones de adivinación y aprendizaje permanecen sin cambios funcionales.
# --------------------------------------------------------------------------------

def guess_personajes_con_aprendizaje(): 
    print("🤖 ¡Bienvenido al **Guess** con Aprendizaje! (Especial Cartoon Network) 🧠")
    print("Piensa en un personaje de Cartoon Network. Responderé 'si' o 'no'.")

    personajes = cargar_datos()
    preguntas = obtener_preguntas(personajes)
    posibles_personajes = list(personajes.keys())
    respuestas_usuario = {}
    
    # --- Bucle de Preguntas y Filtrado ---
    for pregunta_texto, clave_caracteristica in preguntas:
        if len(posibles_personajes) <= 1:
            break

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
            print("🎉 ¡Lo logré! ¡Soy **Guess**!")
        else:
            print("😔 Vaya, me equivoqué. ¡Enséñame quién es para que **Guess** aprenda!")
            aprender_personaje(personajes, respuestas_usuario)

    else:
        # Adivinanza fallida o personaje no encontrado
        print("\n😥 ¡No lo pude adivinar! No tengo ese personaje en mi base de datos.")
        aprender_personaje(personajes, respuestas_usuario)

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
    print("\nAhora, dime las características de este nuevo personaje. ¡Así **Guess** aprenderá!")
    
    # Obtener todas las claves únicas de características de toda la base
    todas_las_claves = set()
    for caracteristicas in personajes.values():
        todas_las_claves.update(caracteristicas.keys())

    # Preguntar por las que NO se preguntaron antes o que no tienen respuesta
    for clave_caracteristica in todas_las_claves:
        if clave_caracteristica not in nuevas_caracteristicas:
            # Crea un texto de pregunta legible
            texto_pregunta = clave_caracteristica.replace('_', ' ').capitalize()
            
            respuesta = input(f"¿Tu personaje '{nombre_nuevo}' tiene la característica: {texto_pregunta}? (si/no/omite): ").lower()
            if respuesta in ["si", "no"]:
                nuevas_caracteristicas[clave_caracteristica] = respuesta

    # 4. Guardar el nuevo personaje y las características
    personajes[nombre_nuevo] = nuevas_caracteristicas
    guardar_datos(personajes)

# Ejecutar el juego
if __name__ == "__main__":
    guess_personajes_con_aprendizaje()
