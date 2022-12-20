def count_vowels(word):
    cnt = 0
    for i in word:
        if i in 'aeiou':
            cnt += 1
    return cnt


print(count_vowels('apple'))  # => 2
print(count_vowels('banana'))  # => 3
