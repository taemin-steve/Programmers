# 각 줄마다 N!의 오른쪽 끝에있는 0의 개수를 출력하라. 
# 0의 개수는 결국 10으로 몇번 나눌수 있는지. 
# N!을 직접할수는 없고.. 모듈로연산을 써줘야 하는 부분인데,2의 개수와, 5의 개수만세서 
# N 개에 대해서 longN 사실 5의 개수만 찾아주면 되긴해 
# 5의 배수로 몇번 까지 갈수 있나 확인하면 되겠다. 

for _ in range(int(input())):
    num = int(input())
    count = 0
    divide = 5
    while True:
        if num // divide == 0:
            break
        count += (num // divide)
        divide *= 5
    print(count)