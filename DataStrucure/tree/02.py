"""
재귀 순회 함수 만들기

순회한는 것 자체가 재귀이므로, 재귀 함수로 만들면 구현하는 과정을 이해하기 쉽다.
"""

# 전위 순회 함수 만들기
# 방문할 노드의 인덱스가 트리 크기를 넘어가면 종료한다.
def preorder(tree, i=0):
    if i < len(tree): # 방문할 인덱스가 트리 크기를 넘지 않는 경우
        print(tree[i], end=' ')
        left = 2*i+1
        right = left + 1
        if left < len(tree) and tree[left] is not None:
            preorder(tree, left)
        if right < len(tree) and tree[right] is not None:
            preorder(tree, right)

tree = ["A", "B", "C", "D", "E", "F", None, "G"]
# preorder(tree)

# 방문 결과를 리스트로 반환
def preorder_list(tree, i=0):
    if i < len(tree):
        res = [tree[i]]
        left = 2*i+1
        right = left + 1
        if left < len(tree) and tree[left] is not None:
            res += preorder_list(tree, left)
        if right < len(tree) and tree[right] is not None:
            res += preorder_list(tree, right)
        return res
    

print(preorder_list(tree))


# 방문 결과를 리스트로 반환 -> 함수 안에 함수 정의

def preorder3(tree):
    def _preorder3(tree, i=0):
        if i < len(tree):
            res.append(tree[i])
            left = 2*i+1
            right = left +1
            if left < len(tree) and tree[left] is not None:
                _preorder3(tree, left)
            if right < len(tree) and tree[right] is not None:
                _preorder3(tree, right)          

    res = []
    _preorder3(tree)
    return res

print(preorder3(tree))


# 코드 단축하기 
"""
if left < len(tree) and tree[left] is not None: 와 같은 코드는 반복해서 쓸 필요가 없다고 한다.
재귀함수의 기본 종료 조건으로 넣으면 코드가 짧아진다. 
"""

def preorder4(tree):
    def _preorder4(i=0):
        if i >= len(tree) or tree[i] is None: # i의 값이 tree의 길이보다 길거나 같으면 정지, tree가 None이면 정지
            return
        res.append(tree[i])
        _preorder4(2*i+1) # 재귀 적으로 왼쪽 자식 
        _preorder4(2*i+2) # 재귀 적으로 오른쪽 자식

    res = []
    _preorder4()
    return res

print(preorder4(tree))

# 중위 순회 함수 만들기
# 중위 순회는 왼쪽 노드 -> 현재(부모) 노드 -> 오른쪽 노드 순으로 변경

def inorder(tree):
    def _inorder(i=0):
        if i >= len(tree) or tree[i] is None: 
            return
        _inorder(2*i+1) # 왼쪽 노드 저장 
        res.append(tree[i]) # 부모 노드 저장
        _inorder(2*i+2) # 오른쪽 노드 저장
    res = []
    _inorder()
    return res

print(inorder(tree))
# 후위 순회 함수 만들기 
# 후위 순회도 순서만 왼쪽 -> 오늘쪽 -> 현재로 변경하면 된다.

def postorder(tree):
    def _postorder(i=0):
        if i >= len(tree) or tree[i] is None: 
            return
        _postorder(2*i+1) # 왼쪽 노드 저장 
        _postorder(2*i+2) # 오른쪽 노드 저장
        res.append(tree[i]) # 부모 노드 저장
    res = []
    _postorder()
    return res

print(postorder(tree))