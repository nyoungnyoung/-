rest = []
for i in range(10):
    i = int(input())
    rest.append(i % 42)
print(len(set(rest)))
