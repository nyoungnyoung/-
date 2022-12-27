# 원형큐
# 데이터가 저장될 배열 필요
# front, rear 변수 필요
# 기능 : enQueue, deQueue, peek, is_Empty, is_Full, queue_print(임의로 만든 기능)


class Queue:
    def __init__(self, N):
        self.queue = [None] * N
        self.front = 0
        self.rear = 0

    def enQueue(self, data):    # rear 뒤쪽에 요소 넣기
        if not self.is_full():      # 가득 차있지 않을때만 작업
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = data
        else:
            raise IndexError

    def deQueue(self):     # front에 있는 요소 삭제 및 반환
        # 이렇게 한다고 삭제까지 되나?? 궁금궁금
        # 사실 삭제가 안되는게 맞음! 덮어씌우는거!!
        if not self.is_empty():
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]
        return None

    def peek(self):     # 가장 앞쪽에 있는 요소(front 뒤쪽의 값)를 반환
        if not self.is_empty():     # 비어있지 않으면
            return self.queue[(self.front + 1) % len(self.queue)]
        return None     # 비어있으면 그냥 None 반환

    def is_empty(self):
        return self.front == self.rear      # 같으면 True(비어있다) / 다르면 False(비어있지 않다)

    def is_full(self):
        return (self.rear + 1) % len(self.queue) == self.front  # 같으면 True(가득 차 있다) / 다르면 False(가득 차지 않았다)

    def queue_print(self):
        # front + 1 ~ rear 요소들 출력하기
        #      1        4 일땐 별 문제 없지만 그 반대일 때는 문제가 발생함
        # while문으로 해결해보자
        idx = self.front
        while idx != self.rear:     # 같지 않으면 계속 반복
            idx = (idx + 1) % len(self.queue)
            print(self.queue[idx], end=' ')
        print()


T = 10
for _ in range(T):
    tc = input()
    data = list(map(int, input().split()))
    queue = Queue(9)
    for d in data:
        queue.enQueue(d)

    cnt = 0
    while True:
        # 제일 앞 요소 빼서, cnt를 빼고 뒤에 넣기
        num = queue.deQueue()
        num = num - (cnt) % 5 - 1      # 첫 cnt를 1로 설정하고 num - (cnt) % 5로 설정해줘도 됨
        if num < 0:
            num = 0
        queue.enQueue(num)
        cnt += 1
        if num == 0:
            break

    print(f'#{tc}', end=' ')
    queue.queue_print()


