from itertools import permutations
# import deque

def solution(expression):
    answer = []
    operation_rank = permutations("+-*", 3)
    operator_list = []
    digit_list = []
    
    stack = []
    for i in range(len(expression)):
        if expression[i] >= '0' and expression[i] <= "9":
            stack.append(expression[i])
        else:
            digit_list.append(int("".join(stack)))
            operator_list.append(expression[i])
            stack.clear()
    if stack:
        digit_list.append(int("".join(stack)))
    
    for operators in operation_rank:
        d = digit_list.copy()
        o = operator_list.copy()
        
        for op in operators:
            while op in o:
                idx = o.index(op)
                ans = 0
                if op == "+":
                    ans = d[idx] + d[idx+1]
                elif op == "-":
                    ans = d[idx] - d[idx+1]
                elif op == "*":
                    ans = d[idx] * d[idx+1]
                d[idx] = ans
                d.pop(idx+1)
                o.pop(idx)
        answer.append(abs(d[0]))

    return max(answer)

print(solution("100-200*300-500+20"))