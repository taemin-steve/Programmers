from sys import stdin, stdout
from collections import Counter
input = stdin.readline

def best_Album(genres, plays):
    answer = []
    dict = {}
    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]] = [i]
        else:
            dict[genres[i]] = dict.get(genres[i]) + [i] 
    sorted_dict = sorted(dict.items(), key = lambda x : sum(plays[i] for i in x[1]) , reverse= True)
    
    for tuple in sorted_dict:
        sorted_list = sorted(tuple[1] , key= lambda x : plays[x], reverse=True)
        answer = answer + sorted_list[0:2]
    return answer

def best_Album_refactoring(genres, plays):
    answer = []
    dict = {i:[] for i in set(genres)} # genres를 키로 하는 dict 생성, value는 빈 값 
    for i in zip(genres, plays, range(len(genres))):
        dict[i[0]].append([i[1], i[2]]) # [플레이수, index] 로 이어진 list를 원소로 추가 
    genres_sorted = sorted(dict.items(), key= lambda x: sum(i[0] for i in x[1]), reverse=True) #plays 수의 총합이 큰 genres 순으로 정렬
    # lambda식 해석 : x == items(), x[i] == 각 장르의 value([[플레이수, index] ,[플레이수, index] , ... [플레이수, index]] 의  2차원 배열 구조) >> x에 대입
    # i == value의 원소 ([플레이수, index]), sum(i[0]) == sum(플레이수)
    for genre in genres_sorted:
        plays_sorted = sorted(genre[1] , key= lambda x : x[0], reverse=True)
        answer = answer + [i[1] for i in plays_sorted[:2]]
    return answer
            

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# genres = ["pop", "classic", "classic", "classic", "pop"]
# plays = [600, 500, 150, 800, 2500]

print(best_Album_refactoring(genres, plays))
