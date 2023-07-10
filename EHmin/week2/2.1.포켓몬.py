from sys import stdin, stdout
input = stdin.readline
# print = stdout.write

def get_most_various_PKM(nums):
    PKM_num = len(nums)
    PK_set = set(nums)
    if PKM_num/2 > len(PK_set):
        return len(PK_set)
    else :
        return int(PKM_num / 2)
    
# def solution(ls):
#     return min(len(ls)/2, len(set(ls))) 
# 어떻게 분기가 아니라 더 작은걸 뽑으면 된다고 접근을 한거지?
# 대소 비교를 통해서 분기문이 갈리는경우 Min, Max 접근이 가능하다. 
    

nums = list(map(int,input().split()))
print(get_most_various_PKM(nums))