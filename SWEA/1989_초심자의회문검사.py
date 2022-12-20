# T개의 테스트 케이스, 회문이면 1, 아니면 0
# input : 문자열!
# len(str) // 2 만큼 잘라서 비교
# str[ : len(str) // 2] == str[-1 : len(str) // 2: -1] : 1
# 아니면 0

T = int(input())
t = 0
for i in range(T):
    str = input()
    if len(str) % 2 != 0:
        if str[:len(str)//2] == str[-1:len(str)//2:-1]:
            t += 1
            print(f'#{t} 1')
        else:
            t += 1
            print(f'#{t} 0')
    else:
        if str[:len(str)//2] == str[-1:len(str)//2-1:-1]:
            t += 1
            print(f'#{t} 1')
        else:
            t += 1
            print(f'#{t} 0')

# list = [1, 2, 3, 4, 5, 6, 7]
# print(list[-1:len(list) // 2:-1])
