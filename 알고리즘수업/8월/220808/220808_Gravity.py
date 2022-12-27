import sys
T = int(sys.stdin.readline())
for t in range(1, T+1):
    N = int(sys.stdin.readline())
    room = list(map(int, sys.stdin.readline()))
    # 각 테스트 케이스별 문제 풀이
    # 가장 많이 떨어지는 상자의 낙차는 가장 왼쪽 상자도 아니고, 가장 높은 상자도 아니다!!
    # 각 열의 가장 꼭대기 상자가 떨어지는 낙차 구하고, 그 중에서 가장 큰 값 출력
    # 낙차 구하는 방법???
    # 0번열의 낙차를 구해보자
    # 1번열부터 N-1번열까지 반복해서 높이 비교

    # 0번 열의 낙차 구하는 작업
    # 0번부터 N-2열까지 구하도록...변경하기
    # cnt 중에서 제일 큰 값 저장하기 위한 변수가 피룡함

    result = 0       # 제일 큰 값을 넣기 위한 변수 선언, 초기화는 0으로
    for j in range(N-1):
        cnt = 0
        for i in range(j+1, N):     # 내 오른쪽에 있는거부터 비교
            if room[i] < room[j]:
                cnt += 1            # 나는 cnt들 중에 제일 큰 cnt를 뽑고 싶어요
        if cnt > result:            # cnt를 계속 비교해서, 제일 큰 값을 저장하기
            result = cnt

    # 정답 출력
    print(f'# {t} {result}')


