# 큐 제일 앞에 있는 문서의 중요도 확인
# 나머지 문서 중 현재 문서보다 중요도가 높은 문서가 있다면
# 현재 문서를 큐에 다시 넣기 / 아니면 바로 인쇄
# M번째 문서가 몇번째로 인쇄되었는지 출력
from collections import deque
import sys

T = int(sys.stdin.readline())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while M > -1:
        if queue[0] == max(queue):
            del queue[0]
            cnt += 1
            M -= 1
        else:
            top = queue.popleft()
            queue.append(top)
            if M == 0:
                M = len(queue) - 1
            else:
                M -= 1
    print(cnt)

