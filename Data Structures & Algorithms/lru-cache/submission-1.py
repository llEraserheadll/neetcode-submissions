class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.right,self.left = Node(0,0),Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self,node):
        #remove from the list
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
    
    def insert(self,node):
        # insert from the right
        next  = self.right
        prev = self.right.prev

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
