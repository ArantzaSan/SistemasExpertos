import random

def simulador_clue():
    """
    Simulador simplificado del juego Clue (Cluedo) con 5 finales narrativos.
    """ 
    # 1. Definición de Componentes
    personajes = {
        "Menta": "Profesor Menta (Arqueólogo)",
        "Rosa": "Srta. Rosa (Novelista)",
        "Mostaza": "Coronel Mostaza (Militar)",
        "Púrpura": "Sra. Púrpura (Botánica)",
        "Negro": "Dr. Negro (Astrofísico)"
    }
    locaciones = {
        "Salon": "Salón Principal",
        "Biblioteca": "Biblioteca",
        "Invernadero": "Invernadero",
        "Cocina": "Cocina",
        "Estudio": "Estudio"
    }
    armas = {
        "Candelabro": "Candelabro",
        "Cuerda": "Cuerda de seda",
        "Tuberia": "Tubería de Plomo",
        "Puñal": "Puñal",
        "Botella": "Botella Rota"
    }

    # 2. Definición Aleatoria del Crimen (La Verdad)
    culpable_clave = random.choice(list(personajes.keys()))
    locacion_clave = random.choice(list(locaciones.keys()))
    arma_clave = random.choice(list(armas.keys()))

    # Versiones legibles para el final
    culpable_verdad = personajes[culpable_clave]
    locacion_verdad = locaciones[locacion_clave]
    arma_verdad = armas[arma_clave]

    # --- INICIO DEL JUEGO ---
    print("\n" + "="*50)
    print("      🔍 SIMULADOR PROTOTIPO DE CLUE 🔍")
    print("="*50)

    print("\nEl Sr. Blanco ha sido encontrado sin vida en la Mansión. Su misión es simple: encontrar la verdad.")
    print("Debe acusar a **un personaje**, en **una locación**, con **un arma**.\n")

    # Mostrar opciones al jugador
    print("--- 👤 PERSONAJES ---")
    for k, v in personajes.items():
        print(f"[{k}] - {v}")
    print("\n--- 📍 LOCACIONES ---")
    for k, v in locaciones.items():
        print(f"[{k}] - {v}")
    print("\n--- 🔪 ARMAS ---")
    for k, v in armas.items():
        print(f"[{k}] - {v}")

    # 3. Conjetura del Jugador
    print("\n" + "-"*30)
    conjetura_culpable = input("Acusación (Personaje - clave): ").strip()
    conjetura_locacion = input("Ubicación (Locación - clave): ").strip()
    conjetura_arma = input("Herramienta (Arma - clave): ").strip()
    print("-" * 30 + "\n")

    # 4. Evaluación y Narrativa de los 5 Finales (Historias)

    # ----------------------------------------------------
    # FINAL 1: CASO RESUELTO (Acierto Total)
    # ----------------------------------------------------
    if (conjetura_culpable == culpable_clave and
        conjetura_locacion == locacion_clave and
        conjetura_arma == arma_clave):

        print("🎊 ¡ACUSACIÓN CORRECTA! 🎊")
        print("\n**FINAL 1: EL CASO RESUELTO.**")
        print(f"Usted ha descubierto la verdad: fue el **{culpable_verdad}**,"
              f" quien cometió el crimen en el **{locacion_verdad}** usando el **{arma_verdad}**."
              "\nLa codicia fue el móvil. El culpable es detenido sin resistencia. El Sr. Blanco descansa en paz. La justicia ha prevalecido.")

    # ----------------------------------------------------
    # FINAL 2: LA PISTA FALSA (Falla en el Culpable, Acierta Locación y Arma)
    # ----------------------------------------------------
    elif (conjetura_locacion == locacion_clave and
          conjetura_arma == arma_clave):

        print("❌ ¡ACUSACIÓN ERRÓNEA! - Culpable Incorrecto, Arma y Locación Correctas.")
        print("\n**FINAL 2: LA PISTA FALSA.**")
        print(f"Usted acertó el lugar (**{locacion_verdad}**) y el arma (**{arma_verdad}**), ¡pero no el autor!"
              f"\nLa persona que usted acusó, {personajes.get(conjetura_culpable, 'el extraño')}, tiene una coartada de hierro. "
              "Mientras el verdadero asesino, el **Profesor Menta**, con su mente de arqueólogo astuto, "
              "destruye la única prueba que lo incrimina, un papel quemado que usted ignoró. El caso se enfría "
              "y el crimen queda impune, el Profesor Menta vive libre.")

    # ----------------------------------------------------
    # FINAL 3: LA VENGANZA SILENCIOSA (Falla Locación, Acierta Culpable y Arma)
    # ----------------------------------------------------
    elif (conjetura_culpable == culpable_clave and
          conjetura_arma == arma_clave):

        print("❌ ¡ACUSACIÓN ERRÓNEA! - Locación Incorrecta, Culpable y Arma Correctas.")
        print("\n**FINAL 3: LA VENGANZA SILENCIOSA.**")
        print(f"Usted señaló al **{culpable_verdad}** con el **{arma_verdad}**, ¡pero el crimen no fue en el {locaciones.get(conjetura_locacion, 'lugar equivocado')}!"
              f"\nEl asesino, al verse tan cerca de ser descubierto, intenta escapar, provocando un gran revuelo."
              f"\nEn la confusión, el Coronel Mostaza, sintiendo que la justicia no será suficiente, toma la ley en sus manos. "
              f"Se escucha un grito. El culpable nunca es llevado ante la justicia. El Coronel Mostaza desaparece sin dejar rastro.")

    # ----------------------------------------------------
    # FINAL 4: EL SEÑUELO INÚTIL (Falla Arma, Acierta Culpable y Locación)
    # ----------------------------------------------------
    elif (conjetura_culpable == culpable_clave and
          conjetura_locacion == locacion_clave):

        print("❌ ¡ACUSACIÓN ERRÓNEA! - Arma Incorrecta, Culpable y Locación Correctas.")
        print("\n**FINAL 4: EL SEÑUELO INÚTIL.**")
        print(f"Usted atrapó al **{culpable_verdad}** en el **{locacion_verdad}**, ¡pero falló el arma! Creyó que era un {armas.get(conjetura_arma, 'objeto irrelevante')}. "
              "Resulta que el verdadero arma del crimen, un diminuto trozo de **Tubería de Plomo**, estaba aún en el bolsillo "
              "del abrigo del culpable. Lo usó para despistar. En el interrogatorio, el asesino explota de risa, y logra "
              "convencer al jurado de que la policía 'plantó' el arma en su bolsillo para culparlo. El jurado lo declara inocente por 'duda razonable'.")

    # ----------------------------------------------------
    # FINAL 5: LA CONFUSIÓN GENERAL (Falla en 2 o 3 Elementos - Caso Abierto)
    # ----------------------------------------------------
    else:
        print("❌ ¡ACUSACIÓN COMPLETAMENTE ERRÓNEA! - Múltiples Fallas.")
        print("\n**FINAL 5: LA CONFUSIÓN GENERAL.**")
        print("Su acusación fue errónea en dos o más puntos. Las pistas se mezclan, las coartadas se desmoronan "
              "y todos los sospechosos parecen igualmente culpables e inocentes."
              f"\nLa policía, agotada y sin pruebas sólidas, declara que el crimen fue un 'accidente desafortunado' "
              f"y cierra el caso. El **{culpable_verdad}** celebra en secreto su victoria y planifica su próximo gran golpe. Nadie volverá a buscar la verdad.")

    print("\n" + "="*50)
    print(f"           ✅ VERDAD OCULTA: {culpable_verdad}, en el {locacion_verdad}, con el {arma_verdad}. ✅")
    print("="*50)

# Ejecutar el simulador
simulador_clue()
