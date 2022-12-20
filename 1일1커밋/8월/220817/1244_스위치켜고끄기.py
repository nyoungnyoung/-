import sys
N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))


def change(n):
    if switch[n-1] == 0:
        switch[n-1] = 1
    else:
        switch[n-1] = 0


def boy(n):
    for i in range(1, N+1):
        if i % n == 0:
            change(i)


def girl(n):
    change(n)
    for i in range(1, N+1):
        if n - i < 1 or n + i > N:
            break
        if switch[n - i - 1] == switch[n + i - 1]:
            change(n - i)
            change(n + i)
        else:
            break


S = int(sys.stdin.readline())
for _ in range(S):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        boy(b)
    else:
        girl(b)

for i in range(1, N+1):
    print(switch[i - 1], end=' ')
    if i % 20 == 0:
        print()
