words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]

def wordrelay(lst):
    word_relay = []
    for str in words:
        if len(word_relay) == 0:
            word_relay.append(str)
        elif str in word_relay:
            return 


# print(wordrelay(words)) # 5번째 참가자가 탈락하였습니다.


# words = input().lower()
# words = words.split()
# if words[0][-1] == words[1][0] and words[1][-1] == words[2][0]:
#     print('Pass')
# else:s
#     print('Fail')
wordrelay(words)