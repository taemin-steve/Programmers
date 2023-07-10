def solution(s):
    answer=True
    numP=0
    numY=0
    for i in (s):
        if i=='p' or i=='P':
            numP+=1
        elif i=='y' or i=='Y':
            numY+=1
    if numP!=numY:
        answer=False
    elif numP==numY:
        answer=True
    print(answer)
    return(answer)
