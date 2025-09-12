# Regla: Si llueve, entonces la calle está mojada
def modus_tollens(llueve, calle_mojada):
    if llueve and not calle_mojada:
        return "Contradicción: debería estar mojada"
    elif not calle_mojada:
        return "No está lloviendo (Modus Tollens)"
    else:
        return "No se puede concluir con certeza"

# Premisas
llueve = None          # Valor desconocido a evaluar
calle_mojada = False   # Sabemos que la calle NO está mojada

# Aplicar Modus Tollens
resultado = modus_tollens(True, calle_mojada)
print(resultado)
