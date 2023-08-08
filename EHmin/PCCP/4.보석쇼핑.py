from collections import defaultdict

def solution(gems):
    d = defaultdict(int)
    for i in set(gems):
        d[i] = 0
    max_gem = len(d.keys()) # gem의 종류의 수를 미리 저장
    
    min_pointer_distance = len(gems) # 구간 최소거리 
    l = 0 # left pointer
    r = 0 # right pointer
    
    # 이전 포인터들의 위치를 기억. 한번에 업데이트 해주기 위해서 저장 
    pre_l = l 
    pre_r = r
    
    #return 할 답
    answer_l = 0
    answer_r = 0
    
    d = defaultdict(int)
    d[gems[l]] += 1 #첫번째는 미리 넣어주기 
    
    while r < len(gems):
        # 업데이트
        if pre_l != l:
            d[gems[pre_l]] -= 1
            if d[gems[pre_l]] == 0:
                del d[gems[pre_l]] # 만약 보석의 개수가 0이라면 key 값 제거 
            pre_l = l
        elif pre_r != r:
            pre_r = r
            d[gems[pre_r]] += 1
        
        if r-l > min_pointer_distance: # 만약 구간의 길이가 기존보다 크다면, 구간 거리 감소를 위해 l을 이동
            l += 1
        elif len(d) == max_gem: # 모든 보석이 있다면 >> 왼쪽 증가
            if r-l < min_pointer_distance:
                min_pointer_distance = r - l
                answer_l = l + 1
                answer_r = r + 1
            l += 1
        else: #뭣도 아니면 오른쪽 증가 
            r += 1
            
    return [answer_l, answer_r]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))