"""
단어를 역순으로 출력하기

주어진 문자열을 역순으로 반환하는 함수를 작성하라.
입력: s = “aircraft”
출력: “tfarcria”

문자열의 슬라이싱이나 반복문, 정렬을 이용하면 쉽게 풀수 있지만 "역순"이란 단어는 스택을 떠 올릴수 있다.

"""

def solution(word:str) -> str :
    return word[::-1]


class Node:
    def __init__(self, data):
        self.data= data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None: 
            self.top = Node(data)
        else:
            node = Node(data)  
            node.next = self.top 
            self.top = node 

    def pop(self):
        if self.top is None: 
            return None
        node = self.top 
        self.top = self.top.next 
        return node.data 
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data 
    
    def is_empty(self):
        return self.top is None


def solution2(word:str) -> str:
    answer = ""
    s = Stack()
    for w in word:
        s.push(w)
    
    while not s.is_empty():
        answer += str(s.pop())
    return answer

st = "aircraft"
print(f"입력 : {st}, 반화 : {solution(st)}") 
print(f"입력 : {st}, 반화 : {solution2(st)}") 