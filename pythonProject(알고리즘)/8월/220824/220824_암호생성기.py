for tc in range(1, 11):
    T = int(input())
    data = list(map(int, input().split()))
    while data[-1] != 0:            # data의 마지막 원소가 0이 되기 전까지 반복
        for i in range(1, 6):       # i : 1 ~ 5
            password = data.pop(0) - i      # password : data의 첫번째 원소에 i를 빼준 것
            if password <= 0:       # password가 0보다 작거나 같을경우
                data.append(0)      # data 마지막에 0 추가 후 break
                break
            data.append(password)
    print(f'#{T}', end=' ')
    print(*data)