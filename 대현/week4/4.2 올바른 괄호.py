def solution(s):
    box = []
    answer = True
    for i in (s):
        if(i == "("):
            box.append("(")
        else: 
            if(box == []):
                return False
            else:
                box.pop()
    if(box == []):
        answer = True
    else:
        answer = False
    return answer
