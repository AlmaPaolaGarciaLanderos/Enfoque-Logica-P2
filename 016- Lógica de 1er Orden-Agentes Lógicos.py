#Alma Paola Garcia Landeros  
#21110038  
#6E1  
#Inteligencia Artificial  
#Centro de Enseñanza Tecnica Industrial 

class AgenteLogico:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def tomar_decision(self, estado):
        for regla in self.base_conocimiento:
            condiciones, decision = regla[:-1], regla[-1]
            if all(condicion(estado) for condicion in condiciones):
                return decision

        return None  # No se pudo tomar una decisión

# Ejemplo de uso
base_conocimiento = [
    ((lambda x: x['temperatura'] > 30, lambda x: x['humedad'] < 0.5), 'Encender el aire acondicionado'),
    ((lambda x: x['temperatura'] < 10, lambda x: x['humedad'] > 0.8), 'Encender la calefacción'),
    ((lambda x: x['temperatura'] > 20, lambda x: x['humedad'] > 0.6), 'Abrir las ventanas'),
]

agente = AgenteLogico(base_conocimiento)

# Estado actual
estado_actual = {'temperatura': 25, 'humedad': 0.7}

# Tomar una decisión basada en el estado actual
decision = agente.tomar_decision(estado_actual)

if decision:
    print("Se ha decidido:", decision)
else:
    print("No se pudo tomar una decisión.")
