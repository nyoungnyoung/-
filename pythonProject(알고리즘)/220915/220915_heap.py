# 최대힙
# 최대 높이 3인 트리를 이용해서 heap 구현하기
heap = [None] * 16
# 마지막 원소를 가리키는 변수
heap_count = 0


# 연산은 두 가지
def heap_push(value):
    global heap_count
    # 1. 마지막 위치에 value 넣기
    heap_count += 1
    heap[heap_count] = value
    # 2. 부모 노드랑 비교해서 자식 노드가 더 크면 바꿔주기(반복-current가 root가 될때까지)
    current = heap_count
    parent = current // 2
    # current가 1보다 큰 동안 반복, current가 1이되면 루트라는거
    # 현재 노드가 root가 아니고, 자식 노드가 부모보다 더 크면 바꿔라!
    while current > 1 and heap[current] > heap[parent]:      
        heap[current], heap[parent] = heap[parent], heap[current]
        current = parent
        parent = current // 2

def heap_pop():
    global heap_count
    # 1. root 반환
    result = heap[1]
    # 2. 마지막 요소를 root위치에 복사하기
    heap[1] = heap[heap_count]
    heap[heap_count] = None
    heap_count -= 1
    # 3. 부모노드랑 자식노드가 더 크면 바꿔주기(반복)
    parent = 1
    child = parent * 2  # 일단은 왼쪽자식
    if child + 1 <= heap_count:     # 오른쪽 노드가 존재한다는뜻
        if heap[child] < heap[child+1]:
            child += 1
    while child <= heap_count and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heap_count:
            if heap[child] < heap[child+1]:
                child += 1
    return result

heap_push(2)
heap_push(4)
heap_push(1)
heap_push(6)
heap_push(7)
heap_push(5)
print(heap_pop())
print(heap_pop())
print(heap_pop())
print(heap_pop())
print(heap_pop())
print(heap_pop())