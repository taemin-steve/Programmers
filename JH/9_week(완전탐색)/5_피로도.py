from itertools import permutations

# 던전리스트의 순열을 구한뒤 순차적으로 탐험하면서 탐험할 수 있는 최대 던전 수를 구함
def solution(k, dungeons):
    answer = 0

    for p in permutations(dungeons, len(dungeons)): 
        now = k
        cnt = 0 
        for need, spend in p:
            if now >= need:
                now -= spend
                cnt += 1 
        answer = max(answer, cnt)

    return answer
