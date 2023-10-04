#VPS 찾기 

for _ in range(int(input())):
    s = input()
    st = []
    flag = True
    for i in range(len(s)):
        if s[i] == '(':
            st.append("(")
        elif st:
            st.pop()
        else:
            flag = False
            break
    if flag and len(st) == 0:
        print("YES")
    else:
        print("NO")
        
### 이렇게 Flag를 세우고 싶지 않다면 함수를 만들어서 접근하는 방법도 있음!
### >> 그렇게 하면 바로 return을 해주면서 해결 가능하다.