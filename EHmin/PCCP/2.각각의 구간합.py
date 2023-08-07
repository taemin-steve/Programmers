 #입력과 출력을 자유롭게 작성해주세요
N = int(input())
l = list(map(int, input().split()))
M = int(input())

acc_sum = [0]
for i in range(N):
    acc_sum.append(acc_sum[-1] + l[i])

for i in range(M):
    si, ei = map(int,input().split())
    print(acc_sum[ei] - acc_sum[si-1])