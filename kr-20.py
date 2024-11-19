def kr20(respuestas):
    """Calcula el coeficiente KR-20."""
    num_personas = len(respuestas)
    num_preguntas = len(respuestas[0])
    
    # Calcular la proporción de respuestas correctas
    p = [sum(respuestas[i]) / num_preguntas for i in range(num_personas)]
    
    # Calcular la varianza de las puntuaciones
    varianza_respuestas = sum((x - sum(p) / num_personas) ** 2 for x in p) / num_personas
    
    # Calcular la varianza total
    varianza_total = sum((sum(respuestas[i]) - sum(p) / num_personas) ** 2 for i in range(num_personas)) / num_personas

    # Calcular KR-20
    if varianza_total == 0:
        return 0
    return (num_preguntas / (num_preguntas - 1)) * (1 - (varianza_respuestas / varianza_total))

# Inicializar respuestas
num_personas = 15
num_preguntas = 10
respuestas = []

# Obtener respuestas de las personas
for i in range(num_personas):
    print(f"Ingrese las respuestas para la persona {i + 1} (1 para 'Sí', 0 para 'No'):")
    persona_respuestas = []
    for j in range(num_preguntas):
        while True:
            respuesta = input(f"Pregunta {j + 1}: ")
            if respuesta in ['1', '0']:
                persona_respuestas.append(int(respuesta))
                break
            else:
                print("Por favor, ingrese 1 para 'Sí' o 0 para 'No'.")
    respuestas.append(persona_respuestas)

# Calcular KR-20
coeficiente_kr20 = kr20(respuestas)
print(f"\nEl coeficiente KR-20 es: {coeficiente_kr20:.4f}")