def solution(nums):
    answer = 0
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1        
    dictNum = len(dict)
    listNum = len(nums)
    if(listNum/2 > dictNum):
        answer = dictNum
    else:
        answer = listNum/2 
    return answer


# def solution(nums):
#     answer = 0
#     setNum = len(set(nums))
#     listNum = len(nums)
#     if(listNum/2 > setNum):
#         answer = setNum
#     else:
#         answer = listNum/2 
#     return answer
