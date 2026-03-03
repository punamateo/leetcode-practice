# https://leetcode.com/problems/lru-cache/


class CacheElem:
    def __init__(self,value: int, age_bit: int):
        self.value = value
        self.age_bit = age_bit

    def __str__(self):
        return f"value={self.value}, age_bit={self.age_bit}"

from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.lru_dict = dict()
        self.global_age_bit = 0
        self.lru = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            prev_age = self.cache[key].age_bit
            self.cache[key].age_bit = self.global_age_bit
            del self.lru_dict[prev_age]
            self.lru_dict[self.global_age_bit] = key
            self.global_age_bit += 1

            return self.cache[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:            
        
        def get_next_lru_age_bit() -> int:
            lru_age_bit = self.lru

            while lru_age_bit not in self.lru_dict:
                lru_age_bit += 1

            return lru_age_bit

        if key in self.cache:
            prev_age = self.cache[key].age_bit
            self.cache[key] = CacheElem(value=value, age_bit=self.global_age_bit)
            del self.lru_dict[prev_age]
            self.lru_dict[self.global_age_bit] = key
        
        elif len(self.cache) >= self.capacity:
            self.lru = get_next_lru_age_bit()
            lru_key = self.lru_dict[self.lru]
            del self.cache[lru_key]
            del self.lru_dict[self.lru]

            self.cache[key] = CacheElem(value=value,age_bit=self.global_age_bit)
            self.lru_dict[self.global_age_bit] = key
    
        else: 
            self.lru_dict[self.global_age_bit] = key
            self.cache[key] = CacheElem(value=value, age_bit=self.global_age_bit)
        
        self.global_age_bit += 1



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
# expected: [None,-1,None,-1,None,None,2,6]


def print_cache_array(cache):

    cache_str = "{"
    for key, value in cache.items():
        cache_str += f"(key={key}, value={str(value)}) "

    cache_str += "}"

    print(cache_str)


lRUCache = LRUCache(2)
print(lRUCache.get(2))   
print_cache_array(lRUCache.cache)
   # -1
lRUCache.put(2, 6)
print_cache_array(lRUCache.cache)

print(lRUCache.get(1)) 
print_cache_array(lRUCache.cache)
     # -1
lRUCache.put(1, 5)
print_cache_array(lRUCache.cache)

lRUCache.put(1, 2)
print_cache_array(lRUCache.cache)

print(lRUCache.lru_dict)

print(lRUCache.get(1))      # 2
print(lRUCache.get(2))      # 6    

