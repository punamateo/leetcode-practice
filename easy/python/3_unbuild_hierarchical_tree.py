tree = [
  {
    "id": "2",
    "name": "Marco",
    "parent_id": "",
    "children": [
      {
        "id": "1",
        "name": "James",
        "parent_id": "2",
        "children": []
      },
      {
        "id": "4",
        "name": "Adrian",
        "parent_id": "2",
        "children": []
      },
      {
        "id": "6",
        "name": "Carlos",
        "parent_id": "2",
        "children": [
          {
            "id": "7",
            "name": "Jose",
            "parent_id": "6",
            "children": []
          },
          {
            "id": "8",
            "name": "Richard",
            "parent_id": "6",
            "children": []
          }
        ]
      }
    ]
  },
  {
    "id": "5",
    "name": "Bob",
    "parent_id": "",
    "children": [
      {
        "id": "3",
        "name": "Mateo",
        "parent_id": "5",
        "children": []
      }
    ]
  }
]


def flatten_tree(tree):
    flat_list = [] 

    def flatten(tree):
        for elem in tree:
            flat_list.append(elem)

            if elem["children"]:
                flatten(elem["children"])  
    
    flatten(tree)

    return flat_list



flat_tree = flatten_tree(tree)
print(flat_tree)
print(len(flat_tree))

