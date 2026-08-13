class LRUCacheNode:
    def __init__(self, key:int):
        self.key = key
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.query_history = {}
        self.lru = None
        self.recent = None
        self.cap = capacity
    
    def update_query_history(self, key):
        tmp = self.query_history[key]
        if not tmp.next:
            return
        
        if not tmp.prev:
            self.lru = tmp.next
        else:
            tmp.prev.next = tmp.next
        
        tmp.next.prev = tmp.prev
        self.recent.next = tmp
        tmp.next = None
        tmp.prev = self.recent
        self.recent = tmp

    def pop_lru(self):
        if self.lru is not None:
            tmp = self.lru
            if tmp.next:
                tmp.next.prev = None
            self.lru = self.lru.next
            tmp.next = None
            return tmp.key
        
        return None

        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_query_history(key)
            '''
            print("="*20)
            print(f"get key {key}")
            print(self.cache)
            print('-'*20)
            print(self.query_history)
            print(f'self.lru.key: f{self.lru.key}')
            print(f'self.recent.key: f{self.recent.key}')
            '''
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.update_query_history(key)
            self.cache[key] = value
            '''
            print("="*20)
            print(f"put existing key {key}")
            print(self.cache)
            print('-'*20)
            print(self.query_history)
            print("~"*20)
            print(f'self.lru.key: f{self.lru.key}')
            print(f'self.recent.key: f{self.recent.key}')
            '''
            return None
        
        if len(self.cache)>=self.cap:
            lru_key = self.pop_lru()
            if lru_key is not None:
                '''
                print(f"pop_key: {lru_key}")
                print(f'self.lru.key: f{self.lru.key}')
                print(f'self.recent.key: f{self.recent.key}')
                '''
                self.cache.pop(lru_key)
                

        self.cache[key] = value
        newNode = LRUCacheNode(key)
        if self.lru is None:
            self.lru = newNode
        
        if self.recent is not None:
            self.recent.next = newNode
            newNode.prev = self.recent
        
        self.recent = newNode
        self.query_history[key] = newNode

        #print(len(self.cache))
        '''
        print("="*20)
        print(f"put key {key}")
        print(self.cache)
        print('-'*20)
        print(self.query_history)
        print('-'*20)
        print(f'self.lru.key: f{self.lru.key}')
        print(f'self.recent.key: f{self.recent.key}')
        '''


        
        



        



        
