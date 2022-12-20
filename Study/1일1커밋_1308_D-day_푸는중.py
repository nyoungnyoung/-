import sys
Y, M, D = int(sys.stdin.readline().split())
dY, dM, dD = int(sys.stdin.readline().split())

# 연월일 빼가지고 연*(365*366)/월*(31or30)/일 더해주면 된당
year, month, day = dY - Y, dM - M, dD - D

# 일단 Y랑 dY사이에 윤년이 몇번있는지 확인 해야함!
# 윤년 있는 해에는 366일이니까