"""
연결 리스트를 뒤집는 과정

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
    
    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1

    def __str__(self):
        if self.head is None:
            return "Linked list is empty."
        node = self.head
        res = "Head"
        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        return res
    
    def __contains__(self, target):
        if self.head is None:
            return False
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            node = node.next
        return False
    
    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data
    
    def pop(self):
        if self.head is None:
            return None
        node = self.head
        while node.next is not None:
            prev = node
            node = node.next
        if node == self.head:
            self.head = None
        else:
            prev.next = None
        self.length -= 1
        return node.data
    
    def remove(self, target):
        if self.head is None:
            return False
        node = self.head
        while node is not None and node.data != target:
            prev = node
            node = node.next
        if node is None:
            return None
        if node == self.head:
            self.head = self.head.next
        else:
            prev.next = node.next
        self.length -= 1
        return True
    
    def insert(self, i, data):
            if i <= 0:
                self.appendleft(data)
            elif i > self.length:
                self.append(data)
            else:
                node = self.head
                for _ in range(i-1):
                    node = node.next
                new_node = Node(data)
                new_node.next = node.next
                node.next = new_node
                self.length += 1

    """
    reverse 메서드 만들기

    head -> 1 -> 2 -> 3 -> 4 이런 상태의 연결리스트를 
    반대로 head -> 4 -> 3 -> 2 -> 1 만들어 줘야한다. 
    노드가 가리크는 값을 반대로 만들어 주는게 핵심이다.
    """
    def reverse(self):
        if self.length < 2:
            return
        prev = None # 반대로 저장할 노드
        ahead = self.head.next # 다음 head값을 저장 할 노드
        while ahead is not None: # ahead가 none 일때까지 반복
            self.head.next = prev # head가 prev를 가키게한다
            prev = self.head # prev를 head로 변경
            self.head = ahead # head 값을 head 다금 값으로 변경
            ahead = ahead.next # ahead를 ahead 다음 값으로 변경
        self.head.next = prev


import random
my_list = LinkedList()
for i in range(10):
    my_list.append(i)
print(f"연결 리스트의 상태\n연결 리스트의 길이 = {len(my_list)},  {my_list}")
print()
my_list.reverse()
print(f"연결 리스트를 뒤집은 후\n연결 리스트의 길이 = {len(my_list)},  {my_list}")