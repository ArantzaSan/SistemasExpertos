class AdivinaQuien:
    def __init__(self, personajes):
        self.personajes = personajes
        self.nombres_personajes = list(personajes.keys())
        
        # Estado del juego de la IA (Personajes activos)
        self.posibles_personajes_ia = set(self.nombres_personajes)
        
        # El personaje secreto del JUGADOR (la IA debe adivinar este)
        self.personaje_secreto_jugador = random.choice(self.nombres_personajes)
        
        # El personaje secreto de la IA (el jugador debe adivinar este)
        self.personaje_secreto_ia = random.choice(self.nombres_personajes)

        # Usado por la IA para optimizar preguntas
        self.atributos_disponibles = list(list(personajes.values())[0].keys())
        
        print("--- Simulador Adivina Quién? ---")
        print(f"Tu personaje secreto es: **{self.personaje_secreto_ia}**\n")
        print(f"Objetivo: Adivinar el personaje secreto del oponente (IA: {self.personaje_secreto_jugador}).")
        print("-" * 30)

    # ----------------------------------------------------
    # Lógica de la IA (Aprendizaje / Búsqueda Binaria)
    # ----------------------------------------------------

    def seleccionar_pregunta_optima(self):
        """
        Implementa la estrategia de Búsqueda Binaria para "aprender" y elegir
        la pregunta que divide de manera más equitativa el conjunto de posibles
        personajes restantes.
        """
        mejores_opciones = []
        min_desviacion = float('inf')
        
        # Si queda solo un personaje posible, la acción óptima es adivinar
        if len(self.posibles_personajes_ia) == 1:
            return "ADIVINAR", list(self.posibles_personajes_ia)[0]

        # Iterar sobre todos los posibles atributos y valores
        for atributo in self.atributos_disponibles:
            valores_unicos = set(self.personajes[nombre][atributo] 
                                for nombre in self.posibles_personajes_ia)

            for valor in valores_unicos:
                pregunta = f"¿Tu personaje tiene el atributo **{atributo}** igual a **{valor}**?"
                
                # Contar cuántos personajes responden 'Sí' y cuántos 'No'
                conteo_si = 0
                for nombre in self.posibles_personajes_ia:
                    if self.personajes[nombre][atributo] == valor:
                        conteo_si += 1
                
                conteo_no = len(self.posibles_personajes_ia) - conteo_si
                
                # La desviación mide qué tan desequilibrada está la división (cuanto más cerca de 0, mejor)
                desviacion = abs(conteo_si - conteo_no)
                
                # Estrategia de Búsqueda Binaria (minimizar la desviación)
                if desviacion < min_desviacion:
                    min_desviacion = desviacion
                    mejores_opciones = [(atributo, valor)]
                elif desviacion == min_desviacion:
                    mejores_opciones.append((atributo, valor))

        # Elegir una de las mejores preguntas (la que divide mejor)
        if mejores_opciones:
            atributo_optimo, valor_optimo = random.choice(mejores_opciones)
            return "PREGUNTAR", (atributo_optimo, valor_optimo)
        
        return "PREGUNTAR", ("genero", "mujer") # Pregunta de reserva

    def actualizar_posibilidades_ia(self, atributo, valor, respuesta):
        """
        Actualiza el conjunto de personajes posibles de la IA en base a la respuesta del jugador.
        Esto es el mecanismo de descarte o "aprendizaje".
        """
        personajes_a_eliminar = set()
        for nombre in self.posibles_personajes_ia:
            cumple_criterio = (self.personajes[nombre][atributo] == valor)
            
            if (respuesta == "si" and not cumple_criterio) or \
               (respuesta == "no" and cumple_criterio):
                personajes_a_eliminar.add(nombre)
                
        self.posibles_personajes_ia -= personajes_a_eliminar
        print(f"-> La IA descartó {len(personajes_a_eliminar)} personajes.")
        print(f"-> Personajes restantes para la IA: {len(self.posibles_personajes_ia)}")
        print("-" * 30)

    # ----------------------------------------------------
    # Ejecución del Juego
    # ----------------------------------------------------

    def turno_ia(self):
        print("--- TURNO DE LA IA ---")
        
        # La IA aplica su algoritmo de "aprendizaje" para elegir la mejor jugada
        accion, datos = self.seleccionar_pregunta_optima()
        
        if accion == "ADIVINAR":
            personaje_adivinado = datos
            print(f"**La IA ADIVINA**: ¿Tu personaje es **{personaje_adivinado}**?")
            
            if personaje_adivinado == self.personaje_secreto_jugador:
                print("¡CORRECTO! La IA ha ganado el juego.")
                return True
            else:
                print(f"INCORRECTO. La IA pierde este turno. ¡Tu personaje era **{self.personaje_secreto_jugador}**! El jugador gana por error de la IA.")
                return True # El juego termina si se adivina incorrectamente
        
        elif accion == "PREGUNTAR":
            atributo, valor = datos
            pregunta_mostrada = f"¿Tu personaje tiene el atributo **{atributo}** igual a **{valor}**?"
            print(f"**La IA PREGUNTA**: {pregunta_mostrada}")
            
            # Simular la respuesta del jugador
            # La respuesta es SI si el personaje secreto del jugador cumple el atributo
            if self.personajes[self.personaje_secreto_jugador][atributo] == valor:
                respuesta = "si"
            else:
                respuesta = "no"

            print(f"(Respuesta de tu personaje secreto: **{respuesta.upper()}**)")
            
            # La IA "aprende" de la respuesta y actualiza sus posibilidades
            self.actualizar_posibilidades_ia(atributo, valor, respuesta)
            return False

    def turno_jugador(self):
        print("--- TU TURNO (JUGADOR) ---")
        print("Puedes: **PREGUNTAR** (ej: ¿Tiene pelo rubio?) o **ADIVINAR** (ej: Es Beto)")
        
        while True:
            jugada = input("Ingresa tu jugada (PREGUNTA/ADIVINA): ").strip().lower()

            if jugada.startswith("pregunta"):
                pregunta = input("Ingresa la pregunta (ej. color_pelo negro): ").strip().lower().split()
                if len(pregunta) == 2 and pregunta[0] in self.atributos_disponibles:
                    atributo, valor = pregunta
                    
                    # Verificar si el atributo y valor son válidos
                    if any(self.personajes[p].get(atributo) == valor for p in self.nombres_personajes):
                        # Responder al jugador sobre su personaje secreto de la IA
                        respuesta = self.personajes[self.personaje_secreto_ia][atributo]
                        if respuesta == valor:
                            print(f"(Respuesta del personaje secreto de la IA: **SI**)")
                        else:
                            print(f"(Respuesta del personaje secreto de la IA: **NO**)")
                        break
                    else:
                         print("¡Atributo o valor no válido! Revisa la lista de personajes. Intenta de nuevo.")
                else:
                    print(f"Formato de pregunta incorrecto. Debe ser: [atributo] [valor]. Atributos: {', '.join(self.atributos_disponibles)}. Intenta de nuevo.")

            elif jugada.startswith("adivina"):
                nombre_adivinado = input("¿Qué personaje crees que es? (Nombre): ").strip()
                if nombre_adivinado == self.personaje_secreto_ia:
                    print(f"¡CORRECTO! Adivinaste el personaje **{self.personaje_secreto_ia}**. ¡Has ganado!")
                    return True
                else:
                    print(f"INCORRECTO. ¡Tu personaje no era {nombre_adivinado}! El personaje secreto de la IA era **{self.personaje_secreto_ia}**. La IA gana la partida.")
                    return True
            else:
                print("Comando no reconocido. Ingresa 'PREGUNTA' o 'ADIVINA'.")

        return False

    def jugar(self):
        juego_terminado = False
        turno_actual = 1
        
        while not juego_terminado:
            print(f"\n======== TURNO {turno_actual} ========")
            
            # El jugador siempre comienza en esta simulación
            juego_terminado = self.turno_jugador()
            if juego_terminado:
                break
                
            # Pequeña pausa para simular el turno del oponente
            time.sleep(1)
            
            juego_terminado = self.turno_ia()
            if juego_terminado:
                break

            turno_actual += 1
            
        print("\n======== JUEGO TERMINADO ========")


# ----------------------------------------------------
# Inicializar y Ejecutar
# ----------------------------------------------------
if __name__ == "__main__":
    juego = AdivinaQuien(PERSONAJES)
    juego.jugar()
