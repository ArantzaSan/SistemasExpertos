def modus_ponens(premisa1, premisa2):
    """
    Premisa 1: una función que verifica si P entonces Q (condicional)
    Premisa 2: verifica si P es verdadero
    
    La función devuelve Q si ambas premisas son verdaderas, de lo contrario devuelve None.
    """
    P_implies_Q, P = premisa1, premisa2
    
    # Verificar si P y P->Q son verdaderos
    if P_implies_Q[0] and P:
        return P_implies_Q[1]  # Q
    else:
        return None

# Ejemplo:
# Premisa 1: Si estudio, apruebo
# Premisa 2: Estudio
premisa1 = (True, "Aprobo")  # "Si estudio, apruebo"
premisa2 = True             # "Estudio"

resultado = modus_ponens(premisa1, premisa2)

if resultado:
    print("Con Modus Ponens, podemos concluir:", resultado)
else:
    print("Las premisas no permiten concluir algo.")
