#균형잡힌 문자열인가??? 소괄호 대괄호가 맞게 짝지어져 있는가??
def check(st, s):
    for i in range(len(s)):
        if s[i] == '(': 
            st.append("(")
        elif s[i] == '[': 
            st.append("[")
        elif s[i] == ')':
            if st and st[-1]== '(':
                st.pop()
            else:
                return "no"
        elif s[i] == ']':
            if st and st[-1]== "[":
                st.pop()
            else:
                return "no"  
    if not st:
        return "yes"
    else:
        return "no"
                

while True:
    s = input()
    if s == '.':
        break
    st = []
    print(check(st, s))