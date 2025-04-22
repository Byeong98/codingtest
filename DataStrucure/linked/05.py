"""
임의 위치에 노드를 추가하고, 노드 삭제하기
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.hade = None
        self.length = 0
    
    def __len__(self):
        return self.length 
    
    def appendleft(self, data):
        if self.hade is None:
            self.hade = Node(data)
        else:
            node = Node(data)
            node.next = self.hade
            self.hade = node
        self.length += 1
    
    def append(self, data):
        if self.hade is None:
            self.hade = Node(data)
        else:
            node = self.hade
            while node.next is not None:
                node = node.next
            node.next = Node(data)
            self.length += 1

    def __str__(self):
        if self.hade is None:
            return "Linked list is empty"
        node = self.hade
        res = "Hade"
        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        return res


    def __contains__(self, target):
        if self.hade is None:
            return False
        node = self.hade
        while node is not None:
            if node.data is target:
                return True
            node = node.next
        return False
    
    def popleft(self):
        if self.hade is None:
            return None
        node = self.hade
        self.hade = self.hade.next
        self.length -= 1

        return node.data
    
    def pop(self):
        if self.hade is None:
            return None
        node = self.hade
        while node.next is not None:
            prev = node
            node = node.next
        if node == self.hade:
            self.hade = None
        else:
            prev.next = None
        self.length -= 1
        return node.data
    
    """
    remove 메서드
    특정 값을 찾아서 삭제한다. 
    특정 값의 전에 값과 다음 값을 이어준다.
    
    """
    def remove(self, target):
        if self.hade is None:
            return False
        node = self.hade # 임시노드
        # 임시노드 값이 None 이거나 찾는 값이면 정지
        while node is not None and node.data != target:
            prev = node # 임시노드 값을 저장 (임시노드 전의 값을 저장)
            node = node.next 
        if node is None: # 임시노드 값이 None 이면 False
            return False
        if node == self.hade: # 임시 노드값이 가장 앞에 값이면 hade 다음 값으로 변경
            self.hade = self.hade.next
        else: # 아니면 이어 주기 
            prev.next = node.next
        self.length -= 1
        return True
    
    """
    insert 메서드 
    특정 인덱스에 data를 삽입한다.
    """
    def insert(self, i, data):
        if i <= 0:
            self.appendleft(data)
        elif i > self.length:
            self.append(data)
        else:
            node = self.hade
            for _ in range(i - 1):
                node = node.next
            new_node = Node(data) # 새로운 노드 생성
            new_node.next = node.next # 새로운 노드가 임시 노드로 다음 값으로 변경
            node.next = new_node # 임시노드 다음 값을 새로운 노로 변경
            self.length+=1


import random
data = list(range(1,11))
my_list = LinkedList()
for i in data:
    my_list.append(i)

print(f"리스트 상태 확인 : {my_list}\n 길이 :{len(my_list)} ")

# remove test
for _ in range(10):
    i = random.randint(1,11)
    if my_list.remove(i):
        print(f"{i} 삭제 리스트 상태 확인 : {my_list}")
    else:
        print(f"{i}가 연결 리스트에 없습니다.")

print(f"리스트 상태 확인 : {my_list}\n 길이 :{len(my_list)} ")



# insert test
data = list(range(1,11))
my_list = LinkedList()
for i in data:
    my_list.append(i)

print(f"리스트 상태 확인 : {my_list}\n 길이 :{len(my_list)} ")

for _ in range(3):
    i = random.randint(1,20)
    data = random.randint(10, 20)
    my_list.insert(i, data)
    print(f"{data}를(을) 연결 리스트의 {i}인덱스에 삽입했습니다.")
    print(f"연결 리스트의 길이 = {len(my_list)},  {my_list}\n")
