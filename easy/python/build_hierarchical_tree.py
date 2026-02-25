# # build a hierarchical tree
# Reto A: El Transformador de Jerarquías (Nivel Senior)
# Este es el reto más probable porque mencionaron explícitamente "relaciones jerárquicas simples".

# Enunciado:
# Recibes una lista de diccionarios que representan categorías de una base de datos. 
# La lista está "plana", pero cada elemento puede tener un parent_id. 
# Tu objetivo es escribir una función build_tree(data) 
# que devuelva una única lista con los nodos raíz, 
# donde cada nodo tenga una lista de sus hijos en una propiedad llamada children.

items = [
    {"id": "1", "name": "James", "parent_id": "2"},
    {"id": "2", "name": "Marco", "parent_id": ""},
    {"id": "3", "name": "Mateo", "parent_id": "5"},
    {"id": "4", "name": "Adrian", "parent_id": "2"},
    {"id": "5", "name": "Bob", "parent_id": ""},
    {"id": "6", "name": "Carlos", "parent_id": "2"},
    {"id": "7", "name": "Jose", "parent_id": "6"},
    {"id": "8", "name": "Richard", "parent_id": "6"}
];


def build_tree_recursive(items, parent_id = ""):
    tree = []
    for item in items:
        if item["parent_id"] == parent_id:
            node = item.copy()
            node["children"] = build_tree_recursive(items, parent_id=node["id"])
            tree.append(node)

    return tree


def build_tree_optimized(items):
    items_dict = {item["id"]: {**item, "children": []} for item in items}
    tree = []

    for item in items: 
        node_id = item["id"]
        parent_id = item["parent_id"]

        if parent_id == "":
            tree.append(items_dict[node_id])

        else:
            items_dict[parent_id]["children"].append(items_dict[node_id])

    return tree



if __name__ == "__main__":
    result = build_tree_recursive(items)
    import json
    print(json.dumps(result, indent=2))