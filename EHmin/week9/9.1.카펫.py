def solution(brown, yellow):
    center = factorization(yellow)
    for x,y in center:
        if (x+2) * (y+2) == yellow + brown:
            return [x+2, y+2] 

def factorization(n):
    ret = []
    for i in range(int(n/2) + 1):
        if n % (i+1) == 0:
            if n//(i+1) >= i+1:
                ret.append([n//(i+1), i+1])
    return ret
            

brown = 10
yellow = 2

print(solution(brown, yellow))