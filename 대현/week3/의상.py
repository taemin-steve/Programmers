def solution(clothes):
    answer = 1
    hash_map = {}
    for cloth in clothes:
        if cloth[1] not in hash_map:
            hash_map[cloth[1]] = 1
        else:
            hash_map[cloth[1]] = hash_map[cloth[1]] + 1
    # print(hash_map)
    for i in hash_map.values():
        answer = answer * (i+1)
            
    return answer-1
