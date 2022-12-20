def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return      # return을 안써도 되긴함..!

table = [0] * 101
fibo_dp(100)
print(table[100])

# N이 주어진다. 피보나치(N)을 구하시오..
# 0<= N <= 100 의 상황!

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {table[N]}')



# 근데 중간값을 계속 놔둘 필요가 없다면??
# 변수 2개만 갖고도 계산 할 수 있지 않을까??

a = 0
b = 1
n = 20
for _ in range(n-1):
    a, b = b, a + b
print(b)
