import sys
sys.stdin = open('Ladder_input.txt', 'r')

for _ in range(1,11):
    tc=int(input())
    ladder=[list(map(int,input().split())) for _ in range(100)]
    ni=99
    nj=0
    for j in range(99):
        if ladder[99][j]==2:
            nj=j
    while ni > 0:
        if -1<nj-1<100 and ladder[ni][nj-1]==1: #왼쪽으로
            nj=nj-1
            ladder[ni][nj] = 1
        elif -1<nj+1<100 and ladder[ni][nj+1]==1: #오른쪽으로
            nj=nj+1
            ladder[ni][nj] = 1
        elif -1<ni-1<100 and ladder[ni-1][nj]==1: #위로
            ni=ni-1
            ladder[ni][nj] = 1
    print(f'#{tc} {nj}')