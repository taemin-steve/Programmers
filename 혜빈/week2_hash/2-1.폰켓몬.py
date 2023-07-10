#1. set
# def solution(nums): 
#     answer = 0  #답변 초기화
#     mari=int(len(nums)/2)  #데려갈 수 있는 최대 폰켓몬 수
#     m=len(set(nums)) #중복 제거한 폰켓몬 종류
    
#     if mari < m: #종류보다 최대 폰켓몬 수가 작으면
#         answer=mari #폰켓몬 수만큼 데려갈 수 있음
#     else: #아니라면
#         answer=m   #종류만큼 데려갈 수 있음 
#     return answer

#2. hash
def solution(nums):
    answer=0
    pkm={}
    mari=len(nums)//2
    for num in nums:
        pkm[num]=1
  
    answer=min(len(pkm.keys()),mari)
    print(answer) 
    return answer

solution([3,3,3,2,2,4])
solution([3,1,2,3])
solution([3, 3, 3, 2, 2, 2])