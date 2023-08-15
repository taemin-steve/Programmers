from queue import PriorityQueue

q = PriorityQueue()



class Data:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __lt__(self, other):
        return self.b > other.b
    
a = Data(1,3)
b = Data(3,1)


q.put(a)
q.put(b)

print(q.get().b)