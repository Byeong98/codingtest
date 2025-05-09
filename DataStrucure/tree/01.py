"""
트리 / Tree

족보의 가계도나 조직도를 떠올리면 된다. 또는 마인드맵

어려운 만ㄹ로는 그래프(graph)의 한 형태로 순솬이 없는 연결 그래프라 한다.

노드 : 트리를 구성하는 기분 요소, 값과 하위 노드를 가르키는 포인터를 가진다.
간선 : 노드와 노드를 연결한 선

이진트리와 순회 방법

전위 순회 : 현재 노드 -> 오른쪽 노드 -> 왼쪽노드
중위 순회 : 왼쪽 노드 -> 현재 노드 -> 오른쪽 노드
후위 순회 : 왼쪽 노드 -> 오른쪽 노드 -> 현재 노드

이진트리를 표현하는 두가지 방법

1. 배열을 이용하는 방식 
트리의 각 노드를 배열의 인덱스로 나타내는 방식으로 레벨순서대로 저장한다.

부모 노드가 인덱스 n일 때:
    왼쪽 자식 노드의 인덱스: 2 × n + 1
    오른쪽 자식 노드의 인덱스: 2 × n + 2
자식 노드가 인덱스 n일 때:
    부모 노드의 인덱스: (n - 1) // 2
"""



tree = ["A", "B", "C", "D", "E", "F", None, "G"]

# 자식 노드와 부모노드 찾기 
def tree_print(arr:list[str]) -> None:
    n:int = len(arr)
    for i in range(n):
        if arr[i] is not None: # 현재 노드가 None이 아닐때
            print(f"Parent: {tree[i]}", end=", ")
            left = 2*i+1
            right = 2*i+2

            if left < n and arr[left] is not None: # 왼쪽 자식이 배열 범위 안에 있을때
                print(f"left:{arr[left]}", end=', ')
            if right < n and arr[right] is not None: # 오른쪽 자식이 배열 범위 안에 있을때
                print(f"right:{arr[right]}", end=', ')
            print()

tree_print(tree)

# 부모 노드 찾기
def tree_Parent(arr:list[int]) -> None:
    n:int = len(arr)
    for i in range(1,n):
        if arr[i] is not None: # 현재 노드가 None이 아닐때 
            parent:int = (i-1)//2
            print(f"Parent of {arr[i]}: {arr[parent]}")

tree_Parent(tree)