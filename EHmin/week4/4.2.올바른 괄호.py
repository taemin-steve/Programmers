def solution(s):
    answer = True
    stack = []
    for word in s:
        if word == "(":
            stack.append("(")
        elif word == ")":
            if len(stack) == 0:
                return False
            stack.pop()
            
    if len(stack) > 0:
        answer = False
    return answer

print(solution("(()("))