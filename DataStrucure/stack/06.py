"""
자신보다 큰 원소 찾기

음이 아닌 정수 배열이 주어졌을 때, 각 원소의 오른쪽에 있는 원소 중에서 현재 원소보다 큰 값을 출력하되, 가장 근접한 원소를 출력하라. 현재 원소보다 큰 값이 없으면 -1을 출력하라.

예시 1

입력: [4, 5, 2, 25]
출력:
4 --> 5
5 --> 25
2 --> 25
25 --> -1
예시 2

입력: [13, 7, 6, 12]
출력:
13 --> -1
7 --> 12
6 --> 12
12 --> -1
"""

# 이중 반복문 풀이
def solution1(data:list[int]):
    for i in range(len(data)):
        ne: int = -1
        for j in data[i+1:]:
            if data[i] < j:
                ne = j
                break
        print(ne)

# solution1([4, 5, 2, 25])
# solution1([13, 7, 6, 12])

# 스텍을 이용한 풀이 
def solution2(arr:list[int]):
    n:int = len(arr) # 리스트 길이
    s:list[int] = []
    res:list[int] = [-1] * n # 반환할 데이터 리스트 기본 값은 -1
    for i in range(n-1, -1, -1):
        while s:
            if s[-1] > arr[i]:
                res[i] = s[-1]
                break
            else:
                s.pop()

        s.append(arr[i]) # 값을 저장 
    
    for i in res:
        print(i)

solution2([4, 5, 2, 25])


# 스텍을 이용한 풀이
def solution3(arr:list[int]):
    n:int = len(arr)
    s:list[int] = []
    res:list[int] = [-1]*n
    for i in range(n-1, -1, -1):
        while s and s[-1] <= arr[i]: # 스택에 값이 있고 스택 마지막 값이 클때 까지 반복
            s.pop()
        
        if s: 
            res[i] = s[-1] # 스택의 마지막 값이 가장 가까운 큰값
        
        s.append(arr[i]) # 스택에 값을 저장 
    
    # 답 출력
    for i in res:
        print(i)


solution3([4, 5, 2, 25])