words = []
count = 0
while True:
    word = input()
    if word in words:
        print(words[count])
        break
    elif word == 'done':
        break
    else:
        words.append(word)
        count += 1
        if count == 1:
            continue
        else:
            if words[count - 2][-1] != words[count - 1][0]:
                print(count)
                break
            else:
                continue
