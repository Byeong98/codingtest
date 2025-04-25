"""
스택 현하기

후입선출의 원칙에 따라 데이터를 관리한다. 
프링글스 과자를 생각하면 된다. 맨위에 있는 것부터 뽑는 방식을 생각하면 된다.

1. push(data) : 자료 data를 넣는 작업, appendleft와 같다.
2. pop() : 자료를 꺼내는 작업, 연결리스트의 popleft와 같음.
3. peek(): 마지막에 넣은 자료를 확인하는 작업.
4. is_empty() : 빅 스택인지 확인
"""

class Node:
    def __init__(self, data):
        self.data= data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # 데이터를 가장 top에 추가
    def push(self, data):
        if self.top is None: # top이 빈 값인경우 Node 가 top
            self.top = Node(data)
        else:
            node = Node(data) # 임시노드 
            node.next = self.top # 임시 노드의 다음 값을 top과 연결
            self.top = node # top 값을 노드로 변경

    def pop(self):
        if self.top is None: # top이 빈 값이면 none을 반환
            return None
        node = self.top # 임시노드 선언
        self.top = self.top.next # top 노드 다음 값을 top 노드로 선언
        return node.data # top 노드값 반환
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data # 마지막에 넣은 값은 반환
    
    def is_empty(self):
        return self.top is None
    

my_stack = Stack()
for i in range(4):
    my_stack.push(i)
    print(f"Push data = {my_stack.peek()}")

while not my_stack.is_empty():
    print(f" Pop data = {my_stack.pop()}")

print(f"Peek data = {my_stack.peek()}")