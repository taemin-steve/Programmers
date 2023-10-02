# 숫자와 알파벳 소문자로 되어있는 글자가 N줄 
# 숫자를 오름차순으로 정리, 앞에 0이 있으면 생략
# 가장 큰 숫자를 찾아야 한다 >> 연속된 숫자를 찾아야 한다. 
#-----------
# 숫자 찾아서, 오름차순으로 할건데, 0은 생략 가능! 

m = []

for i in range(int(input())):
    s = input()
    # 여기다가 다 넣어서 sort 해서 제출할거임!
    temp = []
    for i in range(len(s)):
        if s[i].isdigit():
            temp.append(s[i])
        elif temp:
            temp_s = "".join(temp)
            m.append(int(temp_s))
            temp.clear()
    if temp:
        temp_s = "".join(temp)
        m.append(int(temp_s))
        temp.clear()
            
m.sort()
for i in m:
    print(i)