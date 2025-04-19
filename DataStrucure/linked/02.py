"""
연결 리스트 클래스를 만들고, 노드 추가하기

appendleft(x): 연결 리스트의 처음에 x를 추가한다.
append(x): 연결 리스트의 끝 x를 추가한다.
popleft(): 연결 리스트에서 첫 노드의 값을 반환하고, 노드는 삭제한다.
pop(): 연결 리스트에서 마지막 노드의 값을 반환하고, 노드는 삭제한다.
insert(i, x): 연결 리스트의 i번 인덱스에 x를 추가한다.
remove(x): 연결 리스트에서 값이 x인 노드를 찾아 삭제한다.
reverse(): 연결 리스트를 제자리에서 순서를 뒤집는다.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self): # len() 함수를 사용시 길이 반환
        return self.length
    
    """
    appendleft() 매서드 만들기 
    """
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
            node = Node(data)
        self.length += 1 

# appendleft test
my_list = LinkedList() # LinkedList 객체로 할당
for i in range(4): 
    my_list.appendleft(i) 
print(len(my_list))


my_list.append(4)
print(len(my_list))
