#l,r : 정렬 대상 인덱스
def merge_sort(l,r):
    if l == r:
        return
    m = (l+r)//2
    merge_sort(l,m)
    merge_sort(m+1,r)
    merge(l,r,m)

def merge(l, r, m):
    pass

arr = [2,9,3,1,4,4,7,8,11]
N = len(arr)
merge_sort(0,N-1)
print(arr)