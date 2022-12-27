

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    a, b = len(A), len(B)
    cnt, i = 0, 0     # b의 개수 cnt
    # i가 a-b+1보다 작은동안 반복(i가 a-b보다 커지면 반복문 종료)
    while i < a - b + 1:
        for j in range(b):
            if A[i+j] != B[j]:
                i += 1
                break
        else:
            cnt += 1
            # i에 B의 길이만큼 더해줘야 중복 방지 가능!
            i += b
    # while문 다 돌고 난 후 cnt 개수에 a - (cnt * b) 더해준 결과 출력
    cnt += a - (cnt * b)
    print(f'#{tc} {cnt}')





    # for문 쓰면 중복되는 문자열 거를수가 없게 됨!
    # # a - b + 1 만큼 문자열 비교
    # for i in range(a - b + 1):
    #     for j in range(b):
    #         # A의 문자열이 B의 문자열과 같지 않으면 for문 탈출
    #         if A[i+j] != B[j]:
    #             break
    #     # break에 걸리지 않으면? B가 A에 1개 포함되는거!
    #     else:
    #         b_cnt += 1
    # # A 문자열 다 돌고 난 후 b_cnt 개수에
    # # a - (b_cnt * b) 더해 준 결과를 result에 저장
    # result = b_cnt + a - (b * b_cnt)
    # print(f'#{tc} {result}')
