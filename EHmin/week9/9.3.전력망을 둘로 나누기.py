import itertools
from collections import deque

def solution(n, wires):
    answer = []
    for i in range(n - 1):
        tree1 = []        
        tree2 = []
        
        tree1.append(wires[i][0])
        tree2.append(wires[i][1])
        deq = wires.copy()
        deq.remove(wires[i])
        deq = deque(deq)
        print(deq)
        
        while deq:
            item = deq.popleft()
            print(item)
            if item[0] in tree1:
                tree1.append(item[1])
            elif item[1] in tree1:
                tree1.append(item[0])
            elif item[0] in tree2:
                tree2.append(item[1])
            elif item[1] in tree2:
                tree2.append(item[0])
            else:
                deq.append(item)
        
        answer.append(abs(len(tree1) - len(tree2)))    
    return min(answer) 
        
                
        
        
        
n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

print(solution(n, wires))