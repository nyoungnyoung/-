N = input().split()
verifyN = 0

for i in range(len(N)):   # N list의 길이만큼 반복
    # N[i]를 제곱한 걸 verifyN에 계속 더해주기
    verifyN += int(N[i])**2
    i += 1

print(verifyN % 10)
