"""
Reto 1: Limpieza de Transacciones (Estilo Stripe)
El problema: Recibes un JSON con transacciones bancarias. Algunas están duplicadas y otras tienen montos en formato de texto que deben ser convertidos.

Tarea: 1. Elimina duplicados basándote en el id.
2. Suma el total de amount solo para las transacciones con estado "success".
3. Retorna un diccionario con el total por moneda (currency).
"""


data = [
    {"id": 1, "amount": "100.50", "currency": "USD", "status": "success"},
    {"id": 2, "amount": "50.00", "currency": "EUR", "status": "success"},
    {"id": 1, "amount": "100.50", "currency": "USD", "status": "success"}, # Duplicado
    {"id": 3, "amount": "20.00", "currency": "USD", "status": "failed"},  # No sumar
    {"id": 4, "amount": "30.25", "currency": "EUR", "status": "success"}
]


def stripe_style(data):
    #eliminar duplicados
    ids_list = set()
    total_by_currency = {}
    unique_data = []

    for row in data:
        if row["id"] in ids_list:
            continue
        ids_list.add(row["id"])

        unique_data.append(row)


        if row["status"] == "failed":
            continue

        if not row["currency"] in total_by_currency.keys():
            total_by_currency[row["currency"]] = 0


        total_by_currency[row["currency"]] += float(row["amount"])

    return total_by_currency


print(stripe_style(data))

