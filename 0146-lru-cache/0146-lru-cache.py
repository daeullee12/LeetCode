class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.cache = {} # map key to Node
        # left: LRU, right: most recent 
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        node.prev.next, node.next.prev = node.prev.next.next, node.next.prev.prev
    
    def insert(self, node):
        node.prev, node.next = self.right.prev, self.right
        self.right.prev.next, self.right.prev = node, node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:


        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capa:
            # remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
            

    
    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)