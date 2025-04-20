"""
# 연결 리스트의 상태를 출력하고, 값을 검핵하기

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
        if self.head == None: # head가 None인 경우 head로 할당.
            self.head = Node(data)
        else:
            node = Node(data) # node 값 선원
            node.next = self.head # node의 다음 값을 head와 같은 값을 참조하게 만들기
            self.head = node # head값과 노드 값 변경
        self.length += 1

    """
    append() 메서드 만들기
    """
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1 
    

    # 연결 리스트 상태 출력
    def __str__(self):
        if self.head is None: 
            return "Linked list is empty"
        res = 'Head' # 연결 리스트의 상태를 나타낼 문자열 변수
        node = self.head # 임시 노드
        while node is not None: # 노드가 None이 아닐 동안 계속 반복
            res += ' -> ' + str(node.data) # 현재 노드 값을 문자열 변수에 저장
            node = node.next # 임시 노드를 다음 값으로 변경
        return res

    def __contains__(self, target):
        if self.head is None: # head가 none이면 False를 반환
            return False
        else:
            node = self.head 
            while node is not None: # 노드가 none일때 까지 반복
                if node.data == target: # 현개 노드의 값이 찾는 값과 같은면 True
                    return True
                node = node.next # 아닌경우 다음 노드로 변경
            return False # 찾는 값이 없으면 False
# __str__ test
my_list = LinkedList()
print(f"아무 것도 없는 경우 : {my_list}")

# 연결 리스트에 값 추가
for i in range(4):
    my_list.append(i)

# 연결 리스트 상태 출력
print(len(my_list))
print(f"값이 있는 경우 : {my_list}")

import random
data = list(range(10, 20))
random.shuffle(data) # 10~19 까지 값을 저장 및 섞음
my_list = LinkedList()
for i in data:
    my_list.append(i)
print(f"연결 리스트의 상태\n{my_list}")
print()
for _ in range(4):
    i = random.randint(5, 25) # 랜덤 숫자 선택
    if i in my_list:
        print(f"{i}는(은) 연결 리스트에 있습니다.")
    else:
        print(f"{i}는(은) 연결 리스트에 없습니다.")