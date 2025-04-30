"""
요세푸스 순열

1번부터 N 번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K 번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

예시

입력: 7, 3
출력: [3, 6, 2, 7, 5, 1, 4]

"""

# 나의 풀이
# 큐에 1~N 번까지 수를 넣는다.
# 큐를 돌며 K번째 값인 경우 삭제
# 아니면 값을 제거하고 다시 마지막에 넣기
# 큐가 사라질떄 까지 반본복
def solution1(n:int, k:int) -> list[int]:
    answer: list[int] = []
    q = [i for i in range(1, n+1)] # 1~N+1 까지 수를 큐에 저장 
    count:int = 1 # k 번째 값이므로 1부터 시작 
    while q: # 큐값이 사라질때 까지 반복
        if count == k: 
            answer.append(q.pop(0)) 
            count = 1
        else: 
            q.append(q.pop(0))
            count += 1
    return answer

print(solution1(7,3))
print(solution1(10,7))


# 정답 풀이
def solution2(n:int, k:int) -> list[int]:
    answer: list[int] = []
    q = [i for i in range(1, n+1)]
    while len(q) != 1: # 큐에 자료가 하나만 있을 때 불필요하게 반복하지 않기 위해
        for _ in range(k-1): # k번째까지 반복
            q.append(q.pop(0)) # front값을 rear에 저장
        answer.append(q.pop(0)) # k번쨰 값 제거
    answer.append(q.pop(0)) 
    return answer


print(solution2(7,3))
print(solution2(10,7))