# 90~100 : A
# 80~89 : B
# 70~79 : C
# 60~69 : D
# else : F

grade = int(input())
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')