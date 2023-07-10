def solution(citations):
    citations.sort(reverse=True)
    for citationNum in range(citations[0],-1,-1):
        overNum = 0
        for citation in citations:
            if(citation >= citationNum):
                overNum = overNum + 1
        if(overNum>=citationNum):
            return citationNum
        

print(solution([3, 0, 6, 1, 5]))