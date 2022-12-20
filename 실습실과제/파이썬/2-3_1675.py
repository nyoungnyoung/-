words = input().lower()
words = words.split()
if words[0][-1] == words[1][0] and words[1][-1] == words[2][0]:
    print('Pass')
else:
    print('Fail')
