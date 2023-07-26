from itertools import permutations
from collections import deque
from collections import defaultdict

def solution(expression):
    answer = []
    b = ['1','3']
    d = defaultdict(int)
    for word in expression:
        d[word] += 1
    # permutation으로 모든 케이스 저장
    nPr = list(permutations("+-*", 3))
    # print(nPr)
    # print(expression)
    
    # 모든 케이스에 대해서 값 answer에 append
    for priority in nPr:
        expression_copy = expression
        
        #우선 순위에 맞춰서 먼저 계산을 진행
        for operator in priority:
            for _ in range(d[operator]):
                stack = []
                exp = deque(expression_copy)
                a = ""
                b = ""
                #큐에서 스택으로 하나씩 넘기다가
                
                while True:
                    stack.append(exp.popleft())
                    if stack[-1] == operator: # 원하는 연산자 만났을때 양쪽 숫자에 괄호 추가 
                        for i in range(3):
                            if i == len(stack) -1:
                                a = stack[:-2]
                                break
                            if i == 3:
                                a = stack[-4:-1]
                                break
                            if stack[-(i+2)] >='0' and stack[-(i+2)] <='9':
                                # print('stack')
                                # print(stack[-(i+2)])
                                continue
                            a = stack[-(i+2):-1]
                        
                        expression_copy = expression_copy.replace(str(a), '(' + str(a))
                        print(expression_copy)
                        
                        exp = "".join(exp)
                        for i in range(3):
                            if i == len(exp) -1:
                                b = exp
                                break
                            if i == 3:
                                b = exp[0:3]
                                break
                            if exp[i] >'0' and exp[i] <'9':
                                    continue
                            b = exp[0:i-1]
                            
                        exp = exp.replace(b, b + ')')
                        print()
                        expression_copy += exp
                        # print(expression_copy)
                        # print(expression_copy)
                        break
                        
        # print(expression_copy)
        answer.append(eval(expression_copy))
    
#     max값 리턴
    
    return max(list(map(abs,answer)))

expression = "100-200*300-500+20"

print(solution(expression))

# while True:
#     if True:
#         continue
#     print('a')

if '0' >='0' and '0' <='9':
    print("aaaaa")