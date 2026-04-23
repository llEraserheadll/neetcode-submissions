class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    #remove from the left
    def remove(self,node):
        prv = node.prev
        nxt = node.next

        prv.next = nxt
        nxt.prev = prv

    #insert from the right
    def insert(self,node):
        prv  = self.right.prev
        nxt = self.right

        prv.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prv


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

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

