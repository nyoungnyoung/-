# 스택 구현해서 값 넣어보기
# class로 구현해보기
class Stack:
    # 속성 : 실제 데이터를 저장할 배열(리스트) - 고정길이, top
    # 기능 : push, pop, peek, size, is_Empty
    def __init__(self, length):
        self.stack = [None] * length
        self.top = -1
        pass

    # 요소를 stack 마지막에 저장하고, 가득차서 못넣을 경우 'overflow' 출력
    def push(self, val):
        if self.is_full():
            print('overflow')
        else:
            self.top += 1
            self.stack[self.top] = val


    # 마지막 요소를 삭제하고, 반환, 요소가 없는 경우 'underflow'
    def pop(self):
        if self.is_empty():
            print('underflow')
            return None
        else:
            self.top -= 1
            return self.stack[self.top + 1]

    # 마지막 요소를 반환, 요소가 없는 경우 'underflow'
    def peek(self):
        if self.is_empty():
            print('underflow')
            return None
        return self.stack[self.top]

    # 현재 요소의 개수 반환
    def size(self):
        return self.top + 1

    # 요소가 없으면 True, 있으면 False 반환
    def is_empty(self):
        if self.top == -1:
            return True
        return False

    # 요소가 가득찼으면 True, 가득차지 않았으면 False 반환
    def is_full(self):
        if self.top == len(self.stack) - 1:
            return True
        return False


my_stack = Stack(10)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
my_stack.push(8)
my_stack.push(9)
my_stack.push(10)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.is_empty())
print(my_stack.is_full())
print(my_stack.size())
print(my_stack.peek())

