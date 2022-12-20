# A와 B가 가위바위보를 하였다.
# 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
# A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.


data = list(map(int,input().split()))

# 1 : 가위 2 : 바위 3: 보
# data[0]을 기준으로 검사
# data[0] == 1 : data[1]이 2면 지고, 3이면 이김
# data[0] == 2 : data[1]이 3면 지고, 1이면 이김
# data[0] == 3 : data[1]이 1면 지고, 2이면 이김

winner = 'A'
if data[0] == 1:
    if data[1] == 2:
        winner == 'B'
elif data[0] == 2:
    if data[1] == 3:
        winner == 'B'
else:
    if data[1] == 1:
        winner == 'B'

print(winner)