def f(n):         # 팩토리얼 n! 1! = 1
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

for i in range(21):
    print(i, f(i))

# 사실 팩토리얼을 사용할 일이 잘 없긴 하다..!
# 그래도 구현하는 방법은 알고 있어야 함!