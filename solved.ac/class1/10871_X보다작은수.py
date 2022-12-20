# X랑 리스트의 요소들을 반복하여 비교
# X보다 작으면 : 변수에 차곡차곡 쌓이게!

N, X = map(int, input().split())
N = list(input().split())
numbers = ''


for i in range(len(N)):
    if int(N[i]) < X:
        numbers = numbers + str(N[i]) + ' '

print(numbers)
