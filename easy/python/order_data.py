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

def normalize_date(date):
    expected_formats = ["%Y-%m-%d", "%d/%m/%Y"]

    for format in expected_formats:
        try:
            parsed_data = datetime.strptime(date,format)
            return parsed_data.strftime("%Y-%m")
        
        except ValueError:
            continue
    
    return None



def clean_data(data):

    unique_record = set()
    clean_data = list()
    monthly_report = dict()

    for row in data:
        #clean
        doctor = row["doctor"].lower()
        date = row["fecha"]
        patient = row["paciente_id"]
        cost = row["costo"]

        tuple_id = (doctor, date, patient)
        id = row["id"]

        if tuple_id in unique_record:
            continue

        if cost is None:
            continue


        row["costo"] = int(cost)
        row["fecha"] = normalize_date(date)


        if row["fecha"] not in monthly_report:
            monthly_report[row["fecha"]] = {"costo_total": 0, "lista_pacientes": [], "consultas_realizadas": 0}

        monthly_report[row["fecha"]]["costo_total"] += row["costo"]    
        monthly_report[row["fecha"]]["consultas_realizadas"] += 1  
        monthly_report[row["fecha"]]["lista_pacientes"].append(patient)
        
        
        clean_data.append(row)
        unique_record.add(tuple_id)


    for month, data in monthly_report.items():
        monthly_report[month]["costo_promedio"] = monthly_report[month]["costo_total"] / monthly_report[month]["consultas_realizadas"]
        monthly_report[month]["lista_pacientes"] = list(set(monthly_report[month]["lista_pacientes"]))


    return sorted(clean_data, key=lambda x: x["fecha"]), monthly_report


import json

processed_data, monthly_report = clean_data(transacciones_sucias)

print(processed_data)
print(json.dumps(monthly_report, indent=2))
