#https://leetcode.com/problems/design-hashmap/

from dataclasses import dataclass

class Node:
    def __init__(self,key,value,next):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        next = "node" if self.next else "None"
        return f"Node(key={self.key},value={self.value}, next={next})"


class MyHashMap:

    def __init__(self):
        self.hash_key = 2069
        self.map  = [None for _ in range(self.hash_key)]
        
    def put(self, key: int, value: int) -> None:

        hash = key % self.hash_key

        new_node = Node(
                key=key,
                value=value,
                next=None
            )
        if self.map[hash] == None:

            self.map[hash] = new_node
            return

        current_node = self.map[hash]
        last_node = None

        while current_node:
            if current_node.key == key:
                current_node.value = value
                return

            last_node = current_node
            current_node = current_node.next

        last_node.next = new_node


    def get(self, key: int) -> int:
        hash = key % self.hash_key
        current_node = self.map[hash]

        if current_node is None:
            return -1
        
        while current_node:
                if current_node.key == key:
                    return current_node.value 
                current_node = current_node.next

        return -1
            
    def remove(self, key: int) -> None:
        hash = key % self.hash_key
        current_node = self.map[hash]
        prev = None

        while current_node:
            if current_node.key == key: 
                if prev == None:
                    self.map[hash] = current_node.next
                else:
                    prev.next = current_node.next
                return 
            prev = current_node
            current_node = current_node.next


        


# Your MyHashMap object will be instantiated and called as such:\

myHashMap = MyHashMap()
myHashMap.put(1, 1);
myHashMap.put(999, 2);

print(str(myHashMap.map[999]))


# param_2 = obj.get(key)
# obj.remove(key)