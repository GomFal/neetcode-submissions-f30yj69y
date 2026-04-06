class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None 

class LRUCache:
    def __init__(self, capacity: int):
        # We initialize the cache using a linked list because with this DS we can stablish the order of entrance
        # Of the nodes, and we can make in O(1) time by stablishing most left and most right nodes, which reference
        # The start and end of the linked list and make insertions and deletes in O(1) time.
        self.capacity = capacity
        self.cache = {}     # We associate the keys with the nodes

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        


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
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            if len(self.cache) > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]


        




        
