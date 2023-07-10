from sys import stdin, stdout
from collections import Counter
input = stdin.readline
# print = stdout.write

def set_of_difference(participant, completion):
    dic_p = Counter(participant)
    dic_c = Counter(completion)
    for key, value in dic_p.items():
        if dic_c[key] != value:
            return key
        
    # for name in participant: # 이렇게 하면 시간 초과 매번 비교도, remove도 비효율적
    #     if name not in completion:
    #         return name
    #     else:
    #         completion.remove(name)

participant = list(input().split())
completion = list(input().split())
print(set_of_difference(participant, completion))