###예제 경우의 수
# solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) 
#headgear의 경우: 노란 모자, 초록 터번, 안 쓰기 / eyewear의 경우: 파란 썬글라스, 안 쓰기 => 3*2 - 1(아무것도 착용 안 하는 경우) = 5
# solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
#face의 경우: 마스크, 파란 선글라스, 메이크업 ,안 쓰기 => 3+1 -1(아무것도 안 하는 경우) =3 

def solution(clothes):
    answer=1 #곱셈을 위해 1로 초기화
    closet={} #옷 종류와 이름을 짝지어 넣을 딕셔너리 
    dict={} #옷 종류에 따른 옷 이름이 각각 몇 개 있는지 셀 딕셔너리
    
    for cloth in clothes: #2차원 배열 내 1차원 배열마다
        clothName=cloth[0] #배열의 첫번째는 옷 이름
        clothType=cloth[1] #배열의 두번째는 옷 종류
        closet[clothName]=clothType #옷 이름 : 옷 종류로 딕셔너리 선언- 중복 value를 가질 수 없으므로
        dict[clothType]=0 #옷 종류당 옷을 세야 하므로 옷 종류:0으로 선언
           
    for i in closet.values(): #옷의 종류마다
        if i in dict.keys(): #딕셔너리의 옷 값과 일치하면
            dict[i]+=1 #1씩 더해 옷 종류당 옷 개수를 셈 
    # print("closet: ", closet)
    # print("dict: ",dict)
    
    for i in dict.values(): #옷 종류당 옷 개수만큼
        answer*=(i+1) #옷을 안 입었을 경우를 포함하기 위해 1씩 더한 수를 곱해 모든 경우의 수를 구함
    answer=answer-1 #아무것도 입지 않은 경우를 빼기 위해 -1
    
    # print(answer)
    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) 
#headgear의 경우: 노란 모자, 초록 터번, 안 쓰기 / eyewear의 경우: 파란 썬글라스, 안 쓰기 => 3*2 - 1(아무것도 착용 안 하는 경우) = 5
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
#face의 경우: 마스크, 파란 선글라스, 메이크업 ,안 쓰기 => 3+1 -1(아무것도 안 하는 경우) =3 