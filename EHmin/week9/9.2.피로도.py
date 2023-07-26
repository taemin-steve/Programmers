import itertools

def solution(k, dungeons):
    answer = []
    
    #순열 생성 
    nPr = list(itertools.permutations(dungeons, len(dungeons)))
    
    #각각의 순열에서 돌 수 있는 최대 던전수 저장 
    for element in nPr:
        clear_num = 0
        fatigue = k 
        for d in element:
            if fatigue >= d[0]:
                fatigue -= d[1]
                clear_num += 1
            else:
                break
        answer.append(clear_num)
        
    # max 값 리턴 
    return max(answer)

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))