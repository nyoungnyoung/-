import sys
while True:
    S = sys.stdin.readline().lower()
    count = 0
    if S[0] == '#':
        break
    else:
        for i in S:
            if i in 'aeiou':
                count += 1
        print(count)
