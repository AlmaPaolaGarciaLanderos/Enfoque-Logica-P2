#Alma Paola Garcia Landeros  
#21110038  
#6E1  
#Inteligencia Artificial  
#Centro de Enseñanza Tecnica Industrial 

import numpy as np

# Función de probabilidad condicional para aprobar el examen
def probabilidad_aprobar(tiempo_estudio, calidad_material):
    # Definir los parámetros del modelo
    tiempo_estudio_media = 5  # horas
    calidad_material_media = 7  # en una escala de 1 a 10
    
    # Calcular la probabilidad condicional utilizando una distribución normal
    probabilidad = np.exp(-(tiempo_estudio - tiempo_estudio_media)**2 / (2 * 2)) * \
                   np.exp(-(calidad_material - calidad_material_media)**2 / (2 * 2))
    
    return probabilidad

# Calcular la probabilidad de aprobar el examen dado cierto tiempo de estudio y calidad del material
tiempo_estudio = 6  # horas
calidad_material = 8  # en una escala de 1 a 10
prob_aprobacion = probabilidad_aprobar(tiempo_estudio, calidad_material)

print("Probabilidad de aprobar el examen:", prob_aprobacion)
