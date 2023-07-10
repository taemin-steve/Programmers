def solution(n):
    answer=0
    arr=list(str(n))
    for i in range(len(arr)):
        answer+=int(arr[i])
    print(answer)
    return(answer)