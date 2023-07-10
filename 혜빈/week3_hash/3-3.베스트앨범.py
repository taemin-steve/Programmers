def solution(genres, plays):
    answer =[]
    played={} #장르당 재생 횟수 넣을 딕셔너리

###장르당 노래 재생 횟수 딕셔너리: 장르 : [플레이수,고유번호] 쌍으로 삽입
    for i in range(len(genres)):
        if genres[i] in played:
            played[genres[i]].append([plays[i],i])
        else:
            played[genres[i]]=[[plays[i],i]]
    # print(played) #{'classic': [[500, 0], [150, 2], [800, 3]], 'pop': [[600, 1], [2500, 4]]}
    
###장르당 총 재생횟수 더하기
    grRank={} #장르당 총 재생 횟수를 더해 넣을 딕셔너리
    for gr in played.keys(): #장르마다
        pls=played[gr] #pl =[플레이수,고유번호] 배열들
        playSum=0 #장르당 재생 횟수 더할 변수: 장르별로 더할것이기 때문에 for문 안에 선언
        for pl in pls: #한 배열마다
            playSum+=pl[0] #플레이수를 더함
        grRank[gr]=playSum #장르: 플레이수 딕셔너리
    # print(grRank.items()) #dict_items([('classic', 1450), ('pop', 3100)])
    grRank=sorted(grRank.items(),key=lambda x: -x[1])
    #sorted: iterable한 변수를 새 배열로 반환하는 함수
    #grRank.items(): 장르당 재생횟수 
    #key=lambda x: -x[1]   : x 변수에 각 배열의 [1]==플레이 총 횟수를 기준으로 내림차순으로 정렬
    # => 장르당 재생횟수 아이템들을 재생횟수 기준으로 내림차순 정렬 == 플레이수가 높은 장르순으로 정렬 
    print(grRank)
    print(playSum)

###
    for gr in grRank: #장르당 재생횟수 아이템별로
        plRank=sorted(played[gr[0]],key=lambda x:(-x[0],x[1]))
        #played[장르]== [각 재생수,고유번호]를, x[0]=플레이수 기준 내림차순, x[1]=고유번호 기준 오름차순 정렬(장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록하기 위해서)
        topTwo=0 #두개까지 베스트 앨범에 넣기 위해 쓰는 변수  
        # print("plRank: ",plRank) #plRank:  [[800, 3], [500, 0], [150, 2]]
        for pl in plRank: #플레이수가 높은 순으로 정렬된 2차원 배열에서
            answer.append(pl[1]) #고유번호만 뽑고
            topTwo+=1 #노래 수에 1씩 더하기
            if topTwo==2: #노래가 2개씩 뽑히면
                break #종료
    print(answer)
    return answer

solution(["classic","pop","classic","classic","pop"],[500, 600, 150, 800, 2500])

#######dummy code
# ###장르 당 플레이 횟수 딕셔너리에 넣기
#     for i in plays:
#         played[i]=1
#     for j in genres:
#         played[i]=j
#     print("played: ",played)    
#     print("genreCnt: ",genreCnt)
### 장르와 pl을 한 배열로 합침
    # glplList=genres+plays
    # print(glplList)    
# ###각 배열의 인덱스 구하기
#     plIdx=[]
#     grIdx=[]
#     for pl in plays:
#         plIdx.append(plays.index(pl))
#     for gr in genres:
#         grIdx.append(genres.index(gr))
# lenGlpl=int(len(glplList)/2)
    # for pl in glplList[lenGlpl:]:
    #     # for gr in glplList[:lenGlpl]: #장르
    #     played[pl]=glplList[:lenGlpl]
    # print(played)
###genres 내 genre당 수 구하기
    # for gr in genres:
    #     # for pl in plays:
    #     genreCnt[gr]=0
    
    # for gernreCntKey in genreCnt.keys(): 
    #     for gr in genres:
    #         if gernreCntKey==gr:
    #             genreCnt[gernreCntKey]+=1 
###장르, 플레이수를 합친 리스트 만들고 인덱스,장르,플레이 수 순으로 출력 해봄 => 플레이 수 - 장르 쌍으로 딕셔너리 삽입
    # glplList=list(zip(genres,plays))
    # for gr in genres:
    #     # print(i,gr,pl)
    #     played[gr]=pl