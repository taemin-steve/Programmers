#발음이 가능한 비밀번호를 만들고 싶어 !
# a,e,i,o,u는 반드시 꼭하나 이상 포함
# 모음 or 자음 연속 3개이상 오면 안됨
# 같은 글자 연속 두번 ㄱㅊ but ee, oo 가능

mo = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input()
    if s == "end":
        break
    
    is_a = False
    is_dup = False
    is_triple = False
    
    for i in range(len(s)):
        if s[i] in mo: 
            is_a = True
            
        if i == len(s) - 1:
            continue
        if s[i] == s[i+1]:
            if s[i] == 'e' or s[i]== 'o':
                continue
            else:
                is_dup = True
                
        if i == len(s) - 2:
            continue
        count = 0
        for j in range(3):
            if s[i+j] in mo:
                count += 1
        if count == 3 or count == 0:
            is_triple = True

    if is_a and not is_dup and not is_triple:
        print("<" + s + "> is acceptable.")
    else:
        print("<" + s + "> is not acceptable.")
