def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(21):
    print(i, fibo(i))

# 중복호출이 굉장히 많이 등장하기 때문에
# 30 넘어가면 겁나 느려짐...  그래서 memoization이용하는거!
# memo이용해서 구현한 코드 참고하기!!
