def solution(s):
    # 1.괄호의 총 개수가 짝수여야 함
    # 2.(와 )의 개수가 같아야 함
    # 3.처음은 (, 마지막은 )여야 함

    ##stack을 통해 풀기
    # 1. 스택에 쌓기(append)
    # 2. 스택에 ()가 쌓이면 pop
    answer = True
    st=[]
    for ss in s:
        if ss=='(':
            st.append(ss) # '('만 스택에 쌓음
        else: # ')' 라면
            if st==[]: #스택이 비어있다면 == 첫번째가 ')'로 시작한다면
                answer=False 
                break
            else: # 요소가 ')'이고, 이미 스택 내에 '('가 있다면 
                st.pop()   #맨 뒤의 '('을 pop 한다 <- ')'이 '('을 만났을 때 
    if st!=[]: #'('와 ')'의 짝이 맞아 스택 내 전부가 pop 되어 빈 스택이 됐다면
        answer=False
    # print(st)
    # print(answer)
    return answer

solution("()()")
solution("(())()")
solution(")()(") #F
solution("(()(") #F
solution("())(()") #issue 
