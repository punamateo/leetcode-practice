
"""
Escenario:
Tienes un volcado de logs de una plataforma. Cada log tiene un user_id, una action y un timestamp (en formato ISO).

Tu Tarea (Puro Python):

Conteo de Acciones: Generar un resumen de cuántas veces hizo cada acción cada usuario.

Acciones Únicas: Listar qué acciones distintas realizó cada usuario (sin repetir).

Tiempo de Sesión: Para cada usuario, calcula la diferencia de tiempo (en segundos) entre su primera y su última acción del día.
"""


from datetime import datetime

logs = [
    {"user_id": 1, "action": "login", "timestamp": "2026-02-24T10:00:00"},
    {"user_id": 2, "action": "login", "timestamp": "2026-02-24T10:05:00"},
    {"user_id": 1, "action": "view_page", "timestamp": "2026-02-24T10:10:00"},
    {"user_id": 1, "action": "view_page", "timestamp": "2026-02-24T10:15:00"},
    {"user_id": 2, "action": "logout", "timestamp": "2026-02-24T10:20:00"},
    {"user_id": 1, "action": "logout", "timestamp": "2026-02-24T10:30:00"},
]

from collections import defaultdict


def count_log_activity_dd(logs):
    log_dict = defaultdict(lambda: defaultdict(int))

    for log in logs:
        user = log["user_id"]
        log_dict[user][log["action"]] += 1

    return log_dict


def count_log_activity(logs):
    log_dict = dict()

    for log in logs:
        user = log["user_id"]
        action = log["action"]
        current_dt = datetime.fromisoformat(log["timestamp"])

        if user not in log_dict:
            log_dict[user]= {"first_ts": current_dt, "last_ts": current_dt, "actions": {}}


        if current_dt < log_dict[user]["first_ts"]:
            log_dict[user]["first_ts"] = current_dt
        if current_dt > log_dict[user]["last_ts"]:
            log_dict[user]["last_ts"] = current_dt

        log_dict[user]["session_time"] = (log_dict[user]["last_ts"] -log_dict[user]["first_ts"]).total_seconds()

        if log["action"] not in log_dict[user]["actions"]:
            log_dict[user]["actions"][log["action"]] = 1
        else:
            log_dict[user]["actions"][log["action"]] += 1



    return log_dict


print(count_log_activity(logs))
