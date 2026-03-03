"""
Tu Reto
Escribe una función en Python (código limpio y senior) que haga lo siguiente:

Limpieza:

1. Elimina duplicados exactos (mismo doctor, fecha y paciente). Ojo con las mayúsculas/minúsculas en el nombre del doctor. X

2. Ignora los registros que no tengan costo. X

3. Asegúrate de que todos los costos sean enteros (int). X

Procesamiento de Fechas: X

4. Normaliza todas las fechas para poder agruparlas por Mes. (Cuidado con el formato DD/MM/YYYY vs YYYY-MM-DD). X

5. Agrupación y Conteo:

Devuelve un reporte que muestre por cada Mes:

El Costo Total.

El Promedio de costo por consulta.

La lista de Pacientes Únicos que fueron atendidos ese mes.

"""


transacciones_sucias = [
    {"id": 1, "doctor": "Dr. House", "costo": "500", "fecha": "2026-01-15", "paciente_id": 101},
    {"id": 2, "doctor": "dr. house", "costo": 500, "fecha": "2026-01-15", "paciente_id": 101}, # Duplicado (mismo doctor, fecha, paciente)
    {"id": 3, "doctor": "Dr. Strange", "costo": 1200, "fecha": "02/10/2026", "paciente_id": 102}, # Fecha en otro formato
    {"id": 4, "doctor": "Dr. House", "costo": 300, "fecha": "2026-01-20", "paciente_id": 103},
    {"id": 5, "doctor": "Dr. Strange", "costo": None, "fecha": "2026-02-15", "paciente_id": 104}, # Costo faltante
    {"id": 6, "doctor": "DR. STRANGE", "costo": 800, "fecha": "2026-02-20", "paciente_id": 105},
    {"id": 7, "doctor": "Dr. Grey", "costo": 450, "fecha": "2026-03-05", "paciente_id": 101},
    {"id": 8, "doctor": "Dr. House", "costo": 500, "fecha": "2026-01-15", "paciente_id": 101}, # Otro duplicado
]

from datetime import datetime
from functools import reduce
from itertools import groupby

def normalize_date(date):
    expected_formats = ["%Y-%m-%d", "%d/%m/%Y"]

    for format in expected_formats:
        try:
            parsed_data = datetime.strptime(date,format)
            return parsed_data.strftime("%Y-%m")
        
        except ValueError:
            continue
    
    return None


from collections import defaultdict
from datetime import datetime

# --- 1. El Generador (La Tubería Lazy) ---
def clean_stream(data):
    seen = set()
    for row in data:
        # Extraer y normalizar (Paso 1-4)
        doc = str(row.get("doctor", "")).strip().upper()
        date = normalize_date(row.get("fecha", ""))
        cost = row.get("costo")
        patient_id = row.get("paciente_id")

        if not date or cost is None:
            continue
            
        # Deduplicación
        record_id = (doc, date, patient_id)
        if record_id in seen:
            continue
        seen.add(record_id)

        # PASO 5: Aquí se detiene y entrega

        yield {
            "mes": date,
            "costo": cost,
            "paciente_id": patient_id
        }
  


# --- 2. El Procesador (Consumo Lazy) ---
def generate_report_lazy(raw_data):
    # Usamos defaultdict para ir acumulando los resultados por mes "al vuelo"
    # El valor inicial es un diccionario con los contadores en cero
    reporte = defaultdict(lambda: {"total": 0, "count": 0, "patients": set()})

    # IMPORTANTE: Aquí no hay sorted(). 
    # El bucle 'for' le pide un registro al generador, lo procesa y lo "tira".
    for registro in clean_stream(raw_data):
        mes = registro["mes"]
        
        # Actualizamos el reporte del mes correspondiente
        reporte[mes]["total"] += int(registro["costo"])
        reporte[mes]["count"] += 1
        reporte[mes]["patients"].add(registro["paciente_id"])
        
        # En este punto, el objeto 'registro' ya no se necesita y Python 
        # puede liberar esa memoria. Solo nos queda el acumulado en 'reporte'.

    # Formateo final (opcional, para que sea legible)
    resultado_final = {}
    for mes, stats in reporte.items():
        resultado_final[mes] = {
            "total_recaudado": stats["total"],
            "promedio": stats["total"] / stats["count"],
            "pacientes_unicos": len(stats["patients"])
        }
    
    return resultado_final



def clean_and_report_with_groupby(data):
    # 1. Limpieza y Normalización (generamos una lista limpia primero)
    # Aquí usaríamos tu lógica de 'tuple_id' y 'normalize_date'
    cleaned_list = []
    seen = set()

    def transform_row(row):
        return {
            "doctor": row["doctor"].lower(),
            "mes": normalize_date(row["fecha"]),
            "costo": int(row["costo"]),
            "paciente_id": row["paciente_id"]

        }


    # clean_data = filter(lambda x: x["costo"] is not None, data)
    # transformed_data = map(transform_row, clean_data)

    for row in data:
        doc = row["doctor"].lower()
        date = normalize_date(row["fecha"])
        cost = row["costo"]
        if not date or cost is None or (doc, date, row["paciente_id"]) in seen:
            continue
        
        cleaned_list.append({
            "mes": date,
            "costo": int(cost),
            "paciente_id": row["paciente_id"]
        })
        seen.add((doc, date, row["paciente_id"]))

    # # 2. ORDENAR: groupby NO funciona si no está ordenado

    cleaned_list.sort(key= lambda x: x["mes"], reverse=True)
    cleaned_list_2 = sorted(cleaned_list, key=lambda x: x["costo"], reverse=True)

    reporte_final = {}

    for mes, grupo_mensual in groupby(cleaned_list, key= lambda x: x["mes"]):

        # lista_mensual = list(grupo_mensual)
        # costos = [r["costo"] for r in lista_mensual]
        # pacientes = {r["paciente_id"] for r in lista_mensual}


        reporte_final[mes] = reduce(lambda acc, curr: {
            "total_recaudado": acc["total_recaudado"] + curr["costo"],
            "pacientes_unicos": acc["pacientes_unicos"] | {curr["paciente_id"]},
            "conteo": acc["conteo"] + 1
        }, grupo_mensual, {"total_recaudado": 0, "pacientes_unicos": set(), "conteo": 0})

        reporte_final[mes]["pacientes_unicos"] = len(reporte_final[mes]["pacientes_unicos"])
        reporte_final[mes]["promedio"] = reporte_final[mes]["total_recaudado"] / reporte_final[mes]["conteo"]


        # reporte_final[mes] = {
        #     "total_recaudado": sum(costos),
        #     "pacientes_unicos": sum(pacientes),
        #     "promedio": sum(costos) / len(costos)
        # }
    return reporte_final



import json

print(json.dumps(generate_report_lazy(transacciones_sucias),indent=2))