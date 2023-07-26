from collections import deque

def solution(n, wires):
    answer = n

    for i in range(n - 1): # i번째 간선제거
        L = set()
        R = set()
        L.add(wires[i][0]) 
        R.add(wires[i][1])

        heap = deque(wires)
        heap.rotate(-i)
        heap.popleft()
        while heap:
            a, b = heap.popleft()
            if a in L or b in L:
                L.add(a)
                L.add(b)
            elif a in R or b in R:
                R.add(a)
                R.add(b)
            else:
                heap.append([a, b])
        print(L, R)
        answer = min(abs(len(L) - len(R)), answer)
    return answer

if __name__ == "__main__":
    print(min(3,3))