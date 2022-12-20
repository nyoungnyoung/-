#       *
#      **
#     ***
#    ****
#   *****

N = int(input())

for i in range(1, N+1):  # 1부터 N까지 반복
    print((N - i) * ' ' + '*' * i)  # N - i 만큼 공백 출력 후 *를 i개만큼 찍어라.
    i += 1
