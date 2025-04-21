"""
연결 리스트에서 노드 꺼내기

1. 임시 노드를 만들고, head로 할당
2. head를 다음 노드로 이동

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght = 0

    def __len__(self):
        return self.lenght
    
    # 연결 리스트에 처음 값에 추가
    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.lenght += 1
    
    # 연결 리스트 마지막 값에 추가
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.lenght += 1

    # 연결 리스트 값 출력
    def __str__(self):
        if self.head is None:
            return "Linked list is empty"
        else:
            node = self.head
            res = "Head"
            while node is not None:
                res += " -> " + str(node.data)
                node = node.next
            return res
    
    # 연결 리스트에 값 찾기
    def __contains__(self, target):
        if self.head is None:
            return False
        else: 
            node = self.head
            while node is not None:
                if node.data is target:
                    return True
                node = node.next
            return False
        
    
    def popleft(self):
        if self.head is None:
            return None
        else:
            node = self.head # 임시 노드를 선언 
            self.head = self.head.next # 임시 노드의 다음 값을 head로 변경
            self.lenght -= 1 # 길이 하나 갑속
            return node.data
        
    """
    pop 연결 리스트의 마지막 노드값의 데이터르 반환하고 삭제 한다.
    중요 포인트는 마지막 값을 반환하가 마지막 앞의 값을 None 값으로 변경해 줘야 한다. 
    """
    def pop(self):
        if self.head is None:
            return None
        node = self.head # 임시 노드 선원
        while node.next is not None: # 다음 노드가 None일때 까지 반복
            prev = node # 임시 노들 값을 저장
            node = node.next # 다음 노드 값으로 변경
        # 임시 노드 값이 head와 같으면 None
        if node == self.head: 
            self.head = None
        else:
            # 임시 노드 앞에 값을 None 값으로 변경
            prev.next = None
        self.lenght -= 1
        return node.data

        

my_linked = LinkedList()
for i in range(4):
    my_linked.append(i)

print(f" 길이 : {len(my_linked)}, 상태 : {my_linked}")

for _ in range(4):
    print(f"{my_linked.pop()}를(을) 꺼낸 후: 길이 = {len(my_linked)}, {my_linked}")


print(f"연결 리스트가 비었을 때 꺼낸 값은 {my_linked.pop()}")
