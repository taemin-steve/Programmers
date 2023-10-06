# 오큰수를 구하고 싶어 
# 오큰수는 나보다 오른쪽에 있으면서 나보다 큰수 중에서 가장 왼쪽에 있는 수야 
# 마지막 수의 경우 혹은 내가 제일 크면 -1 나옴
# 인덱스는 1부터 시작하는 형태 
# N < 1,000,000 백만.. N제곱은 어렵고 N 안에 풀어야 할거같으넫 
# 아이디어는 내가 오큰 수를 못구했다면 어쨋든 다음놈이 먼저 오큰수를 구해야 나도 구할 수 있다! 
# 짝지어주기 문제는 stack 
# 약간 bubble bubble 느낌으로 쭉 터지는 거면 stack 관계성을 유의 하자 
# 얘가 못하면 얘도 못하지 않을까? 라는 개념 
# 자동으로 내림차순으로 쌓임

from collections import defaultdict

N = int(input())

a = list(map(int, input().split())) # 입력받음

# ans = defaultdict(int) #딕셔너리 초기화 
ans = [-1 for _ in range(N)]

# for i in a:
#     ans[i] = -1
    
st = [] # stack 추가  스텍에는 숫자 넣을거야 

for i in range(N):
    while st and st[-1][0] < a[i]:
        item = st.pop()
        ans[item[1]] = a[i]
    st.append([a[i],i]) # 값이랑 index 같이 넣어주기 


print(*ans)

# f = []
# for i in a:
#     f.append(ans[i])
    
# print(*f)
    





