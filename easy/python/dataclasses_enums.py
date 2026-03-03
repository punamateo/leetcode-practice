# El Escenario: "El Sistema de Staff Médico"
# Tienes una lista de empleados. Cada uno tiene un rol, un departamento y un salario. Algunos datos vienen "sucios" (strings en lugar de categorías).

# Tu Reto:
# Define un Enum para los Roles (DOCTOR, ENFERMERO, ADMINISTRATIVO).

# Define una Dataclass llamada Empleado que contenga: id, nombre, rol (el Enum), departamento y salario.

# Implementa una función limpiar_staff: Debe recibir una lista de diccionarios "sucios" y devolver una lista de objetos Empleado.

# Operación Extra: Usa un defaultdict para agrupar a los empleados por Departamento y calcular el presupuesto total de salarios por cada uno.


# Escribe la función procesar_nomina(data) que:

# Convierta cada diccionario en un objeto Empleado.

# Retorne un reporte (usando defaultdict) que se vea así:
# {"Diagnóstico": 8000, "Oncología": 4500, ...}

staff_sucio = [
    {"id": 1, "nombre": "Dr. House", "rol": "doctor", "depto": "Diagnóstico", "salario": 5000},
    {"id": 2, "nombre": "Wilson", "rol": "DOCTOR", "depto": "Oncología", "salario": 4500},
    {"id": 3, "nombre": "Cuddy", "rol": "administrativo", "depto": "Dirección", "salario": 6000},
    {"id": 4, "nombre": "Chase", "rol": "enfermero", "depto": "Diagnóstico", "salario": 3000},
]


from dataclasses import dataclass
from enum import Enum, auto
from collections import defaultdict
from typing import List

class Rol(Enum):
    DOCTOR = auto()
    ADMINISTRATIVO = auto()
    ENFERMERO = auto()

    @classmethod
    def from_str(cls, name: str):

        try:
            enum_result = cls[name.strip().upper()]
        except KeyError:
            raise ValueError(f" {name} it is not supported")


@dataclass(frozen=True)
class Empleado():
    id: str
    nombre: str
    rol: Rol
    departamento: str
    salario: int


def limpiar_staff(empleados: List[dict]) -> List[Empleado]:

    emp_limpio = list()
    for emp in empleados:
        id = emp["id"]
        nombre = emp["nombre"]
        rol = Rol.from_str(emp["rol"])
        departamento = emp["depto"]
        salario = emp["salario"]

        limpio_ = Empleado(
            id=id,
            nombre=nombre,
            rol=rol,
            departamento=departamento,
            salario=salario
        )

        emp_limpio.append(limpio_)

    return emp_limpio


def calcular_presupuesto(list_empleados: List[Empleado]) -> dict:
    presupuesto_departamento = defaultdict(int)
    empleados_depto = defaultdict(list)

    for empleado in list_empleados:
        presupuesto_departamento[empleado.departamento] += empleado.salario
        empleados_depto[empleado.departamento].append(empleado.nombre)

    return presupuesto_departamento, empleados_depto

staff = limpiar_staff(staff_sucio)

presupuesto, empleados_depto = calcular_presupuesto(staff)
print(presupuesto)
print(empleados_depto)