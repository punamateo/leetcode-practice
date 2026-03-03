# El Ejercicio: "El Constructor de Perfil Único (Golden Record)"
# Imagina que recibes una lista de "actualizaciones" de un perfil de usuario. Estas actualizaciones vienen de diferentes sistemas (Legacy, Mobile, Web) y cada una tiene una prioridad.

# Tu objetivo: Usar reduce para fusionar todos estos diccionarios en un único objeto final.

# Las Reglas de Fusión:
# Si un campo (como email) aparece en varias actualizaciones, prevalece el que tenga el número de prioridad más alto.

# Si el campo es una lista (como intereses), no sustituyas; fusiona las listas eliminando duplicados.

# Si el campo no existe en el acumulador, añádelo.


actualizaciones = [
    {"usuario": "gemini_user", "email": "old@mail.com", "prioridad": 1, "intereses": ["filosofía"]},
    {"usuario": "gemini_user", "email": "new@mail.com", "prioridad": 5, "intereses": ["programación"]},
    {"usuario": "gemini_user", "telefono": "+591-123456", "prioridad": 3, "intereses": ["música"]},
    {"usuario": "gemini_user", "email": "temp@mail.com", "prioridad": 2, "intereses": ["filosofía", "python"]},
]



from functools import reduce
def fusionar_datos(data):

    def consolidar(acc, curr):
        prioridad_actual = curr["prioridad"]
        intereses = curr["intereses"]

        for campo, valor in curr.items():
            if campo in ["prioridad", "intereses", "usuario"]:
                continue
            
            prioridad_previa = acc["prioridades"].get(campo,0)

            if prioridad_actual > prioridad_previa:
                acc["data"][campo] = valor
                acc["prioridades"][campo] = prioridad_actual

        acc["data"]["intereses"] = list(set(acc["data"]["intereses"] + intereses))

        return acc

    inicial = {"data": {"usuario": "gemini_user", "intereses": []}, "prioridades": {}}
    new_data = reduce(consolidar, data,inicial)

    return new_data


print(fusionar_datos(actualizaciones))