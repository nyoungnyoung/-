def change(num, n):
    tmp = '0123456789ABC'
    result = ''
    if num == 0:
        return '0'
    while num:
        result = tmp[num % n] + result
        num = num // n
    return result

def solution(n, t, m, p):
    answer = ''
    tmp = ''
    for i in range(t * m):
        tmp += change(i, n)
    for i in range(t):
        answer += tmp[(p-1)+(m*i)]
    return answer

