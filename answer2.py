import time
import math

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} 
        self.access_times = {}
        self.weight = {} 

    def put(self, key, value, weight):
        if len(self.cache) >= self.capacity:
            min_score_key = min(self.weight, key=lambda k: self.weight[k])
            del self.cache[min_score_key]
            del self.access_times[min_score_key]
            del self.weight[min_score_key]

        self.cache[key] = value
        self.access_times[key] = time.time()
        self.weight[key] = weight
        
    
    def get(self, key):
        if key in self.cache:
            self.access_times[key] = time.time()

            score = self.weight[key] * (math.log(time.time() - self.access_times[key] + 1) + 1)

            return self.cache[key], score
        else:
            return -1, 0 

cache = Cache(3) 

cache.put("A", 1, 3)
cache.put("B", 2, 3)
cache.put("C", 3, 1)

print(cache.get("A"))
print(cache.get("B")) 
print(cache.get("C"))
print(cache.get("D")) 

cache.put("D", 1, 2)

print(cache.get("A"))
print(cache.get("B")) 
print(cache.get("C"))
print(cache.get("D"))

'''
The computational complexity of get(key) is O(1) because it involves simple dictionary lookups, which have constant time complexity.

The computational complexity of put(key, value, weight) is O(1) on average. However, in the worst case, when the cache is full and it needs to remove the item with the minimum weight, it becomes O(N), where N is the capacity of the cache. This is because finding the minimum weight requires iterating through all the items in the cache to determine which one to evict.
'''