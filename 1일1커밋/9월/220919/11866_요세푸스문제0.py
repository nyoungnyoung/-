# 1 ~ N번까지 N명의 사람이 원을 이루고 앉음
# K(<= N)가 주어지면, 순서대로 K번째 사람을 제거함
# 한사람이 제거되면 남은 사람들로 이루어진 원을 따라 
# N명의 사람들이 모두 제거될 때까지 계속 진행
# 원에서 사람들이 제거되는 순서를(N, K)-요세푸스 순열
# 해당 순열 구하는 프로그램 작성하시오

from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
queue = deque(i for i in range(1, N+1))
result = []     # 요세푸스 순열 담을 변수
while queue:    # 큐가 빌 때까지 반복
    for i in range(K-1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))
print(f'<{", ".join(result)}>')