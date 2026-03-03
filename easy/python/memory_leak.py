import tracemalloc

# El culpable: Una lista global que nunca se limpia
registry = []

class UserSession:
    def __init__(self, user_id):
        self.user_id = user_id
        self.data = ["data" * 1000] * 100  # Simulamos carga pesada

def process_request(user_id):
    session = UserSession(user_id)
    registry.append(session)  # <--- LEAK: Referencia persistente
    return f"Procesado {user_id}"

# Monitoreo de memoria
tracemalloc.start()

for i in range(1000):
    process_request(i)
    if i % 200 == 0:
        current, peak = tracemalloc.get_traced_memory()
        print(f"Paso {i}: Memoria actual {current / 10**6:.2f}MB, Pico {peak / 10**6:.2f}MB")

tracemalloc.stop()