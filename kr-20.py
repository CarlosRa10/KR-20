#El coeficiente de Kuder-Richardson 20 (KR-20) es un método para evaluar la consistencia interna de una medida basada en datos dicotómicos, como "correcto" o "incorrecto". 
#Con esta formula pude sacar la confiabilidad de mi trabajo de grado
#Las puntuaciones para KR-20 van de 0 a 1, donde 0 no es confiable y 1 es perfecta. constituye un "aceptable" KR-20 puntuación depende del tipo de prueba. En general, una puntuación superior a 0,5 se considera generalmente razonable.
#Si es mayor a 0.70 es mas que aceptable
#Sirve para sacar la confiabilidad de un proyecto utilizando las preguntas que previamente elegiste para la población
#Solo evalua 10 preguntas
#Preguntas con respuestas cerradas(si o no)
#Responde preguntas Dicotomicas
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