def f(n):
    if ch1[n] == 0 or ch2[n] == 0:
        return value[n]

    elif value[n] == '+':
        value[n] = f(ch1[n]) + f(ch2[n])
        return value[n]

    elif value[n] == '-':
        value[n] = f(ch1[n]) - f(ch2[n])
        return value[n]

    elif value[n] == '*':
        value[n] = f(ch1[n]) * f(ch2[n])
        return value[n]

    elif value[n] == '/':
        value[n] = f(ch1[n]) / f(ch2[n])
        return value[n]


for tc in range(1, 11):

    N = int(input())
    value = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    for t in range(N):
        line_list = list(input().split())
        V = int(line_list[0])

        if len(line_list) == 2:
            value[V] = int(line_list[1])
        else:
            value[V] = line_list[1]
            ch1[V] = int(line_list[2])
            ch2[V] = int(line_list[2])

    f(1)
    print(value[1])