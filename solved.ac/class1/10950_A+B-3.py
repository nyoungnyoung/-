# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스마다 A+B를 출력한다.

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)
