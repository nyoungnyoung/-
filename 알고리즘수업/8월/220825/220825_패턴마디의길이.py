T = int(input())
for tc in range(1, T + 1):
    word = input()
    pattern = ''
    # 일단 패턴부터 찾아보자! 어떻게 찾지?
    for i in range(len(word)):
        pattern += word[i]
