#딕셔너리
#정렬 방법도 있음
def solution(p, c):
    # p.sort()
    # c.sort()
    dic1 = {}
    dic2 = {}
    
    for i in p:
        if i not in dic1:
            dic1[i] = 1
        else:
            dic1[i] += 1
            
    for i in c:
        if i not in dic2:
            dic2[i] = 1
        else:
            dic2[i] += 1
    # print(dic1)
    # print(dic2)
    for i in dic1:
        if i not in dic2:
            return i
        else:
            if dic1[i] != dic2[i]:
                return i
