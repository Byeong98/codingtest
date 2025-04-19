"""
연결 리스트 

연속된 메모리 공간에 저장하는 것이 아닌 각데이터가 다은 데이터의 위치를 저장하는 방식이다.
각 노드는 여로 연결되는 다음 노드를 참조 한다.

배열은 인덱스를 통해 쉽게 접근이 가능하지만 삭제와 삽입이 빈번이 일어나는 경우 메모리 공간 확부하고 원소들을 이동시켜야 하는 단점이 있다.
자료의 양이 정해져 있지 않거나 삽입과 삭제가 빈번하게 일어날 경우 연결 리스트가 적합하다.
"""

class Node:
    def __init__(self, data):
        self.data = data  #data는 값을 가리키는 변수(속성, attribute)
        self.next = None  #next는 다음 노드를 가리키는 변수


"""
1. 첫째 노드를 만들고 head라는 이름표를 붙인다. (head에 첫째 노드를 할당)
2. 둘째 노드를 만들고, head의 next가 둘째 노드를 가리키도록 한다.
3. 셋째 노드를 만들고, head의 next의 next가 셋째 노드를 가리키도록 한다.
"""

head = Node(1)
head.next = Node(2)
head.next.next = (Node(3))


# 연결 리스트 출력
node = head # 변수저장
while node: # node가 None이 아닐때까지 반복
    print(node.data)
    node = node.next

# 마지막 노드에 새로운 값 추가
node = head
while node:
    if node is None:
        node = Node(4)
        break
    node = node.next

# 불필요한 값 제거
node = head
while node.next:
    node = node.next
node = Node(4)
print(node.data)


# node 0 추가
node = Node(0)
node.next = head 
head = node 