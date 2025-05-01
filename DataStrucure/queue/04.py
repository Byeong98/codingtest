"""
숫자의 표현

15는 다음과 같이 4가지로 표현할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution을 완성해 주세요
"""


# 큐를 이용해서 푸는 방법 
"""
1~5까지의 숫자를 더한다. 15와 같으면 answer +=1
1~5애서 6을 더하면 21 이미로 큐에 서 제거한다. 15와 같으면 answer += 1 작으면 다음 값을 저장
4,5,6 에다가 다시 7을 저장 22 다시 15보다 작거나 같아지게 더하며 반복 없으면 다음 수저장
"""

def solution1(n:int) -> int:
    q: list[int] = []
    answer: int = 0
    s:int = 0
    for i in range(1,n+1):
        q.append(i)
        s += i
        while s > n:
            s -= q.pop(0)
        if s == n:
            answer +=1
    return answer

print(solution1(15))
print(solution1(20))

# 교제 풀이
def solution2(n: int) -> int:
    q: list[int] = [1]
    answer: int = 1
    i: int = 1
    total: int = 1
    mid: int = (n + 1) // 2 # 시작점을 제한하기 위한 조건
    while i < mid: # 1 ~ n의 절반 값까지 반복
        i += 1
        total += i
        q.append(i)
        while total > n:
            total -= q.pop(0)
        if total == n:
            answer += 1
    return answer


# 두개의 포인터를 이용하는 방법
def solution3(n: int) -> int:
    answer: int = 1
    total: int = 0
    left: int = 1 # 시작점 
    right: int = 1 # 끝점 
    while right < n: # 끝점이 n 보다 크면 정지
        total += right # 끝점을 점차 증가하여 저장한다. 
        while total > n: # 합의 값이 n보다 크면 시작점을 이동
            total -= left
            left += 1
        if total == n:
            answer += 1
        right += 1
    return answer