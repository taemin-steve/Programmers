def solution(genres, plays):
    # genres = ["classic", "pop", "classic", "classic", "pop"]
    # plays = [800, 600, 150, 800, 2500]
    answer = []
    tupleList = []
    for i in range(len(genres)):
        tupleList.append((genres[i],plays[i],i))
    # print(tupleList)
    hash_map_sum = {}
    hash_map_num = {}
    for i in tupleList:
        if i[0] not in hash_map_sum:
            hash_map_sum[i[0]] = i[1]
        else:
            hash_map_sum[i[0]] = hash_map_sum[i[0]] + i[1]
        
        if i[0] not in hash_map_num:
            hash_map_num[i[0]] = [(i[1], i[2])]
            print(hash_map_num[i[0]])
        else:
            hash_map_num[i[0]].append((i[1], i[2]))
            
            hash_map_num[i[0]].sort(key = lambda x:(-x[0],x[1]))
            
            if(len(hash_map_num[i[0]])>2):               
                hash_map_num[i[0]].pop()
            print(hash_map_num[i[0]])
    hash_map_sum = dict(sorted(hash_map_sum.items(), key=lambda x: x[1], reverse=True))
    # print(hash_map_sum)
    # print(hash_map_num)
    for key in hash_map_sum.keys():
        for i in hash_map_num[key]:
            answer.append(i[1])
    # print(answer)
    return answer
