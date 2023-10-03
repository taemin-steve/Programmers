# 각 팀이 몇분동안 이기고 있었는지 출력하세요
# 골이 들어간 횟수 N, (1<=N<=100)
# 득점팀, 번호 
# 이거 split(":") 해서 각각 map(int) 해주면 분, 초로 나눌수 있음 
# 비기고 있을때 기록 >> 다시 비기게 될 때 까지 기록 // 

score = [0,0]
win = [-1]
winning_time = [0]
wt_0 = 0
wt_1 = 0

for _ in range(int(input())):
    team, time = input().split()
    
    m, s = map(int, time.split(':'))
    winning_time.append(m*60 + s) #시간 초로 변환
    
    score[int(team) - 1] += 1 # 승자 기록
    if score[0] > score[1]: win.append(0)
    elif score[0] < score[1]: win.append(1)
    else: win.append(-1)
    
winning_time.append(48*60)

for i in range(len(win)): 
    if win[i] == -1:
        continue
    elif win[i] == 0:
        wt_0 += (winning_time[i+1] - winning_time[i])
    elif win[i] == 1:
        wt_1 += (winning_time[i+1] - winning_time[i]) 
        
print("%02d:"%(wt_0//60)+ "%02d"%(wt_0%60))
print("%02d:"%(wt_1//60)+ "%02d"%(wt_1%60))
