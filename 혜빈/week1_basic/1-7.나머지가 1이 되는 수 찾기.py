def solution(n):
    x=1
    for i in range(1,n+1):
        if (n%i==1):
            print(i)
            x=i
            break
    return(x) 