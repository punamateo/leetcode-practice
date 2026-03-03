


# a = set('abracadabra')
# b = set('alacazam')
# a                                  # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
# a - b                              # letters in a but not in b
# {'r', 'd', 'b'}
# a | b                              # letters in a or b or both
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# a & b                              # letters in both a and b
# {'a', 'c'}
# a ^ b                              # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}


# Aquí tienes un ejercicio de "Auditoría de Seguridad", un clásico en las pruebas técnicas de Backend.

# El Ejercicio: "El Auditor de Permisos"
# Imagina que estás gestionando los accesos a una plataforma médica. Tienes tres grupos de permisos (strings) definidos para un usuario:

# permisos_actuales: Los que el usuario tiene ahora mismo.

# permisos_requeridos: Los que necesita para entrar a una nueva función (ej. "Ver Historial").

# permisos_prohibidos: Una "lista negra" de permisos que, por seguridad, un usuario de su nivel nunca debería tener.


# Tu Reto:
# Escribe un pequeño script (o una función) que determine lo siguiente usando operaciones de sets:

# ¿Qué le falta?: Permisos que están en requeridos pero que el usuario no tiene en actuales. (Operación: Diferencia -).

# ¿Qué tiene de más?: Permisos que el usuario tiene pero que no son necesarios para la nueva función. (Operación: Diferencia -).

# ¿Qué se mantiene?: Permisos que el usuario ya tiene y que también son necesarios para la función. (Operación: Intersección &).

# Alerta de Seguridad: ¿Hay algún permiso en actuales que esté en la lista de prohibidos? (Operación: Intersección &).

# Configuración inconsistente: Obtener una lista de permisos que o bien el usuario tiene, o bien son requeridos, pero no ambos al mismo tiempo. (Operación: Diferencia Simétrica ^).


from dataclasses import dataclass
from typing import List , Set

@dataclass(frozen=True)
class Permisos:
    actuales = {"leer_datos", "escribir_datos", "borrar_datos", "exportar_pdf"}
    requeridos = {"leer_datos", "firmar_digital", "exportar_pdf"}
    prohibidos = {"borrar_datos", "acceso_root"}

def get_permisos(permisos: Permisos) -> List[Set]:

    p_faltantes = permisos.requeridos -  permisos.actuales
    p_sobrantes = permisos.actuales - permisos.requeridos
    p_mantiene = permisos.actuales & permisos.requeridos
    p_alerta = permisos.actuales & permisos.prohibidos
    p_inconsistente = permisos.actuales ^ permisos.requeridos

    return [p_faltantes, p_sobrantes, p_mantiene, p_alerta, p_inconsistente]



p = get_permisos(Permisos())

print(p)