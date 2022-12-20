import sys

while True:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break

    result = 'no'
    if N == N[::-1]:
        result = 'yes'

    print(result)