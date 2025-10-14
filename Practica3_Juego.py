import json
import os

# --- Códigos de Color ANSI (para una interfaz más bonita en la terminal) ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# --- Configuración del Archivo de Base de Datos ---
ARCHIVO_DATOS = "guess_personajes_data.json" 

def cargar_datos():
    """Carga los personajes desde el archivo JSON o devuelve un diccionario vacío si no existe."""
    # (Mantenemos la base de datos de Cartoon Network ampliada)
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    return {
        "Ben Tennyson": {
            "es_humano": "si", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "si", "es_superheroe_cartoon": "si",
            "tiene_dispositivo_de_transformacion": "si", "es_un_villano": "no",
            "es_un_animal_animado": "no"
        },
        "Goku": {
            "es_humano": "no", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "no", "es_superheroe_cartoon": "si",
            "vuela": "si", "usa_traje_naranja": "si", "es_alienigena": "si",
            "es_un_villano": "no", "es_un_animal_animado": "no"
        },
        "Dexter": {
            "es_humano": "si", "tiene_poderes_magicos": "no", "usa_lentes": "si",
            "es_un_niño_protagonista": "si", "es_superheroe_cartoon": "no",
            "es_cientifico": "si", "tiene_un_laboratorio_secreto": "si",
            "es_rubio": "si", "es_un_villano": "no", "es_un_animal_animado": "no"
        },
        "Las Chicas Superpoderosas (Bombón)": {
            "es_humano": "si", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "si", "es_superheroe_cartoon": "si",
            "vuela": "si", "es_mujer": "si", "tiene_lazo_en_el_cabello": "si",
            "es_un_villano": "no", "es_un_animal_animado": "no"
        },
        "Coraje": {
            "es_humano": "no", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "no", "es_un_animal_animado": "si",
            "es_un_perro": "si", "vive_en_una_granja_aislada": "si", "es_rosa": "si",
            "es_un_villano": "no"
        },
        "Finn el Humano": {
            "es_humano": "si", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "si", "es_superheroe_cartoon": "no",
            "usa_sombrero": "si", "vive_en_un_mundo_post_apocaliptico": "si",
            "es_espadachin": "si", "es_un_villano": "no", "es_un_animal_animado": "no"
        },
        "Samurai Jack": {
            "es_humano": "si", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "no", "es_superheroe_cartoon": "no",
            "usa_sombrero": "no", "viaja_en_el_tiempo": "si", "es_espadachin": "si",
            "tiene_corte_de_pelo_cuadrado": "si", "es_un_villano": "no", "es_un_animal_animado": "no"
        },
        "Gumball Watterson": {
            "es_humano": "no", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "si", "es_un_animal_animado": "si",
            "es_un_gato": "si", "es_azul": "si", "tiene_hermano_pez": "si",
            "es_un_villano": "no"
        },
        "Vaca (Vaca y Pollito)": {
            "es_humano": "no", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "no", "es_un_animal_animado": "si",
            "vuela": "no", "es_una_vaca": "si", "viste_de_superheroina_a_veces": "si",
            "es_un_villano": "no"
        },
        "Steven Universe": {
            "es_humano": "si", "tiene_poderes_magicos": "si", "usa_lentes": "no",
            "es_un_niño_protagonista": "si", "es_superheroe_cartoon": "si",
            "vuela": "no", "tiene_escudo_magico": "si", "toca_ukelele": "si",
            "es_un_villano": "no", "es_una_gema": "si", "es_un_animal_animado": "no"
        },
        "Mordecai": {
            "es_humano": "no", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "no", "es_superheroe_cartoon": "no",
            "es_un_animal_animado": "si", "es_un_pajaro": "si",
            "trabaja_en_un_parque": "si", "es_azul": "si", "es_un_villano": "no"
        },
        "Rigby": {
            "es_humano": "no", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "no", "es_superheroe_cartoon": "no",
            "es_un_animal_animado": "si", "es_un_mapache": "si",
            "trabaja_en_un_parque": "si", "es_marron": "si", "es_un_villano": "no"
        },
        "Aku": {
            "es_humano": "no", "tiene_poderes_magicos": "si", "usa_lentes": "no",
            "es_un_niño_protagonista": "no", "es_superheroe_cartoon": "no",
            "es_un_villano": "si", "es_una_entidad_oscura": "si",
            "puede_cambiar_de_forma": "si", "es_negro_y_rojo": "si", "es_un_animal_animado": "no"
        },
        "Perla": {
            "es_humano": "no", "tiene_poderes_magicos": "si", "usa_lentes": "no",
            "es_un_niño_protagonista": "no", "es_superheroe_cartoon": "si",
            "vuela": "no", "es_mujer": "si", "es_una_gema": "si", "usa_lanza": "si",
            "es_un_villano": "no", "es_un_animal_animado": "no"
        },
        "Padre (KND)": {
            "es_humano": "si", "tiene_poderes_magicos": "no", "usa_lentes": "no",
            "es_un_niño_protagonista": "no", "es_superheroe_cartoon": "no",
            "es_un_villano": "si", "fuma_puro": "si", "vive_en_una_mansion": "si",
            "odia_a_los_niños": "si", "es_un_animal_animado": "no"
        }
    }

def guardar_datos(datos):
    """Guarda el diccionario de personajes en el archivo JSON."""
    with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f"\n{Colors.GREEN}✅ ¡Personaje nuevo guardado! ¡Guess ha aprendido algo! ✅{Colors.ENDC}")

def obtener_preguntas(personajes):
    """Genera una lista de preguntas únicas basada en todas las características."""
    preguntas_unicas = set()
    for caracteristicas in personajes.values():
        preguntas_unicas.update(caracteristicas.keys())
    
    # Lista predefinida de orden y texto legible
    mapa_preguntas = {
        "es_humano": "¿Tu personaje es humano? 🧍",
        "es_un_niño_protagonista": "¿Tu personaje es un niño o adolescente protagonista? 👦👧",
        "es_un_animal_animado": "¿Tu personaje es un animal animado (no humano)? 🐻🐱",
        "tiene_poderes_magicos": "¿Tu personaje tiene poderes mágicos? ✨",
        "es_superheroe_cartoon": "¿Tu personaje es un superhéroe o vigilante en la serie? 🦸",
        "es_un_villano": "¿Tu personaje es un villano principal o recurrente? 😈",
        "vuela": "¿Tu personaje vuela? ✈️",
        "usa_lentes": "¿Tu personaje usa lentes? 👓",
        "es_mujer": "¿Tu personaje es una chica/mujer? 🚺",
        "es_alienigena": "¿Tu personaje es un alienígena? 👽",
        "usa_sombrero": "¿Tu personaje usa sombrero o gorra? 🧢",
        "es_una_gema": "¿Tu personaje es una gema? 💎",
    }

    lista_preguntas = []
    # Usar las claves predefinidas para un orden lógico
    for clave, texto in mapa_preguntas.items():
        if clave in preguntas_unicas:
             lista_preguntas.append((texto, clave))
             preguntas_unicas.remove(clave)

    # Añadir las restantes
    for clave in preguntas_unicas:
        texto = f"¿Tu personaje tiene la característica: {clave.replace('_', ' ').capitalize()}?"
        lista_preguntas.append((texto, clave))
        
    return lista_preguntas

# --------------------------------------------------------------------------------

def guess_personajes_con_aprendizaje(): 
    # --- Interfaz Principal Mejorada ---
    print(f"\n{Colors.HEADER}{Colors.BOLD}======================================================={Colors.ENDC}")
    print(f"{Colors.BLUE}{Colors.BOLD}🤖 ¡BIENVENIDO A GUESS! (Adivinador de Cartoon Network) 🧠{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}======================================================={Colors.ENDC}")
    print("Piensa en un personaje de Cartoon Network. Yo haré las preguntas.")
    print(f"Responde solo: {Colors.CYAN}'si'{Colors.ENDC} o {Colors.CYAN}'no'{Colors.ENDC}.\n")

    personajes = cargar_datos()
    preguntas = obtener_preguntas(personajes)
    posibles_personajes = list(personajes.keys())
    respuestas_usuario = {}
    
    # --- Bucle de Preguntas y Filtrado ---
    for i, (pregunta_texto, clave_caracteristica) in enumerate(preguntas):
        if len(posibles_personajes) <= 1:
            break

        # Mostrar progreso (opcional)
        if len(posibles_personajes) > 5:
            print(f"[{i+1}] Quedan {Colors.WARNING}{len(posibles_personajes)}{Colors.ENDC} posibles personajes.")
        
        relevante = any(clave_caracteristica in personajes[p] for p in posibles_personajes)
        
        if not relevante:
            continue
            
        respuesta = input(f"{Colors.CYAN}{pregunta_texto} {Colors.ENDC}(si/no): ").lower()
        while respuesta not in ["si", "no"]:
            print(f"{Colors.FAIL}❌ Por favor, responde con 'si' o 'no'.{Colors.ENDC}")
            respuesta = input(f"{Colors.CYAN}{pregunta_texto} {Colors.ENDC}(si/no): ").lower()

        respuestas_usuario[clave_caracteristica] = respuesta

        # Aplicar el filtro: mantiene solo a los personajes que coinciden
        nuevos_posibles = []
        for p_nombre in posibles_personajes:
            p_caracteristicas = personajes[p_nombre]
            
            if clave_caracteristica in p_caracteristicas and p_caracteristicas[clave_caracteristica] == respuesta:
                nuevos_posibles.append(p_nombre)
            elif clave_caracteristica not in p_caracteristicas and respuesta == 'no':
                 nuevos_posibles.append(p_nombre)

        posibles_personajes = nuevos_posibles
        
    # --- Fase de Adivinanza y Aprendizaje Mejorada ---
    
    print(f"\n{Colors.HEADER}-------------------------------------------------------{Colors.ENDC}")
    
    if len(posibles_personajes) == 1:
        personaje_adivinado = posibles_personajes[0]
        print(f"{Colors.GREEN}{Colors.BOLD}💡 ¡Adiviné! Tu personaje es {personaje_adivinado}.{Colors.ENDC}")
        respuesta_final = input("¿Es correcto? (si/no): ").lower()
        
        if respuesta_final == "si":
            print(f"{Colors.GREEN}🎉 ¡Lo logré! ¡Soy Guess! 🎉{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}😔 Vaya, me equivoqué.{Colors.ENDC} ¡Enséñame quién es para que Guess aprenda!")
            aprender_personaje(personajes, respuestas_usuario)

    else:
        print(f"{Colors.FAIL}😥 ¡No lo pude adivinar!{Colors.ENDC} No tengo ese personaje en mi base de datos.")
        
        if posibles_personajes:
             print(f"Pude reducirlo a: {Colors.WARNING}{', '.join(posibles_personajes)}{Colors.ENDC}")
        
        aprender_personaje(personajes, respuestas_usuario)

    print(f"{Colors.HEADER}-------------------------------------------------------{Colors.ENDC}\n")

def aprender_personaje(personajes, respuestas_usuario):
    """Guía al usuario para añadir el personaje no adivinado a la base de datos."""
    
    nombre_nuevo = input(f"{Colors.BLUE}¿Cuál era el nombre de tu personaje?: {Colors.ENDC}").strip()
    if not nombre_nuevo:
        print("Operación cancelada.")
        return

    nuevas_caracteristicas = {}
    for clave, respuesta in respuestas_usuario.items():
        nuevas_caracteristicas[clave] = respuesta
        
    print(f"\n{Colors.BOLD}✏️ Ahora, dime las características de este nuevo personaje. ¡Así Guess aprenderá!{Colors.ENDC}")
    
    todas_las_claves = set()
    for caracteristicas in personajes.values():
        todas_las_claves.update(caracteristicas.keys())

    for clave_caracteristica in todas_las_claves:
        if clave_caracteristica not in nuevas_caracteristicas:
            texto_pregunta = clave_caracteristica.replace('_', ' ').capitalize()
            
            respuesta = input(f"¿Tu personaje '{nombre_nuevo}' tiene la característica: {Colors.CYAN}{texto_pregunta}{Colors.ENDC}? (si/no/omite): ").lower()
            if respuesta in ["si", "no"]:
                nuevas_caracteristicas[clave_caracteristica] = respuesta

    personajes[nombre_nuevo] = nuevas_caracteristicas
    guardar_datos(personajes)

# Ejecutar el juego
if __name__ == "__main__":
    guess_personajes_con_aprendizaje()
