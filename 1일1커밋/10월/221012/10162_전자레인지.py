import sys
T = int(sys.stdin.readline())
# T를 10으로 나눈 나머지가 0이 아니면 주어진 버튼으로 만들 수 없는 수임!
if T % 10 != 0:
    print(-1)
else:
    # 제일 큰 단위 버튼부터 눌러보기
    for i in [300, 60, 10]:
        # T를 버튼 시간으로 나눈 몫을출력해주고 나머지를 다시 T에 저장!
        print(T//i, end=' ')
        T = T % i
