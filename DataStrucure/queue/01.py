"""
Queue

큐는 선입선출(First in First Out, FIFO)방식으로 버스정류장에 줄을 서서 앞사람이 먼저 들어가는 방법이다. 
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        if self.front is None:
            self.front = self.rear = Node(data)
        else:
            node = Node(data)
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        node = self.front
        if self.front == self.rear: # 큐에 노드가 한개만 있는경우
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return node.data
    
    def is_empty(self):
        return self.front is None
    

q = Queue()

for i in range(3):
    q.enqueue(chr(ord("A") + i))
    print(f"Enqueue data = {q.rear.data}")
print()

while not q.is_empty():
    print(f"Dequeue data = {q.dequeue()}")


# Queue 뒤집기 

# 스택을 이용하는 방법
def reverse_queue(q:Queue) -> None:
    s = []
    while not q.is_empty():
        s.append(q.dequeue())
    while s: # 스택에거 반대로 값을 꺼내 저장
        q.enqueue(s.pop())


# Queue 출력함수
def display(q:Queue) -> None:
    node = q.front
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# 스택 이용 뒤집기 함수 테스트
q = Queue()
for i in range(4):
    q.enqueue(chr(ord("A")+i))

display(q)

reverse_queue(q)
display(q)

# 재귀함수를 이용하는 방법
def reverse_queue_recursive(q: Queue) -> None:
    if not q.is_empty(): # 큐의 값이 있는지 확인 / 재귀적으로 큐의 값이 없을 시 함수 종료
        data = q.dequeue() # 큐의 front 값을 빼서 저장
        reverse_queue_recursive(q) # 큐의 값이 없을때까지 반복
        q.enqueue(data) # 제귀가 종료된 후 값을 저장 / 마지막 값을 가장 최근에 뽑았으니 역순으로 저장된다.



q = Queue()
for i in range(4):
    q.enqueue(i)

display(q)

reverse_queue_recursive(q)
display(q)