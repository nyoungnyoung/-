def div_sum(n):
    sum_n = n                   
    while n > 10:           
        sum_n += n % 10
        n = n // 10
    sum_n += n
    return sum_n

N = int(input())
result = 0
for i in range(N):
    if div_sum(i) == N:
        result = i
        break

print(result)