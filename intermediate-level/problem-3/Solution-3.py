from collections import OrderedDict
class LRUCache(object):
    from collections import OrderedDict
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    def __init__(self, capacity):
        self.cache=OrderedDict()
        self.capacity=capacity
    def get(self,key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key,last=True)
        return self.cache[key]
    def put(self,key:str,value:int):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)
        return self.cache[key]
x=LRUCache(2)
x.put("a",1)
x.put("b",2)
x.put("c",3)
print(x.cache)
print(x.get("b"))
print(x.cache)

