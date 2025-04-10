"""
숫자 변환하기 

문제 설명
자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.

x에 n을 더합니다
x에 2를 곱합니다.
x에 3을 곱합니다.
자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

제한사항
1 ≤ x ≤ y ≤ 1,000,000
1 ≤ n < y
입출력 예
x	y	n	result
10	40	5	2
10	40	30	1
2	5	4	-1
입출력 예 설명
입출력 예 #1
x에 2를 2번 곱하면 40이 되고 이때가 최소 횟수입니다.

입출력 예 #2
x에 n인 30을 1번 더하면 40이 되고 이때가 최소 횟수입니다.

입출력 예 #3
x를 y로 변환할 수 없기 때문에 -1을 return합니다.

"""


"""
문제의 핵심 자료구조 유추하기

1. "최소 횟수","최소 단계"라는 키워드
    최소한의 연산으로, 가장 짧은 경로
2. "한 상태에서 여러 가지 연산을 선택할 수 있다"
    x에 n을 더하거나, 곱하거나 등
    한 노드에서 여러 방향으로 뻡어 나가는 구조면 그래프 탐색 문젝. BFS/DFS 떨올리기
"""

def solution1(x, y, n):
    answer = [-1,-1,-1]
    
    if (y-x)//n: 
        answer[0] = (y-x)//n

    if y%2 == 0:
        answer[1] = int((y//x)**0.5)

    if y%3 == 0:
        answer[2] = int((y//x)**0.5)
    
    if max(answer) == -1:
            return -1
    result = max(answer)
    for i in answer:
        if i > 0 and result > i :
            result = i
        
    return result


def solution(x,y,n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer
        ns = set()

        for i in s:
            if i+n <= y:
                ns.add(i+n)

            if i*2 <= y:
                ns.add(i*2)

            if i*2 <= y:
                ns.add(i*3)
        print(s, ns)
        s = ns
        answer += 1

    return -1





print(solution(10,40,5))
print(solution(10,40,30))
print(solution(2,5,4))

