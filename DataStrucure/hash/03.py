"""
합이 0인 부분 배열 중 가장 긴 것을 찾아라.

양의 정수와 음의 정수의 배열이 있다. 합이 0인 부분 배열 중 가장 긴 배열의 길이를 구하라.

예시

입력: A = [15, -2, 2, -8, 1, 7, 10, 23]
출력: 5 (합이 0인 부분 배열은 -2 2 -8 1 7)
"""

# 나의 풀이
# 투 포인트를 이용해서 문제풀기 
def solution1(arr:list[int]) -> int:
    answer:int = 0 
    for i, v in enumerate(arr): 
        left:int = i # 왼쪽 포인트
        right:int = i + 1 # 오른쪽 포인트 
        s:int = v # 왼쪽 포인트와 오른쪽 포인트 값을 저장 
        while right < len(arr): # right가 리스트 마지막까지 실행 
            s += arr[right] # 순차적으로 저장 
            if s == 0 and answer < right-left+1: # 합이 0과 길이가 긴경우 저장
                answer = right-left+1 
            right += 1 # right 점차 증가 
    return answer

print(solution1([15, -2, 2, -8, 1, 7, 10, 23]))


# 교제 풀이 
def maxLen(arr: list[int]) -> int:
    n: int = len(arr)
    answer: int = 0
    for i in range(n):
        total: int = 0
        left: int = 1
        right: int = i
        for j in range(i, n):
            total += arr[j]
            if total == 0:
                right = j
                answer = max(answer, right-left+1)
    return answer


# dict 사전 풀이 : 누적합 이용
# 누적합이 같은 두 인덱스가 있다면, 그 사이의 합은 무조건 0
"""
dict[0] = -1을 넣는 이유
1. 시작 인덱스가 0인 경우도 처리할 수 있게 하기 위해
2. 누적합이 0이 되는 첫 순간을 잡아내기 위해
3. 인덱스를 빼서 길이를 구할 수 있도록 -1을 넣는 것
"""
def maxLen_dic2(arr: list[int]) -> int:
    dic: dict[int, int] = {0: -1}  # 합이 0이 처음 나올 때는 아무것도 더하지 않았을 때니까 위치는 -1.
    ans: int = 0  # 가장 긴 길이를 저장하는 곳
    total: int = 0  # 지금까지 숫자들을 더한 합

    for i in range(len(arr)):
        total += arr[i]  # 숫자를 하나씩 더해가면서 전체 합을 만들기

        if total in dic:
            # 이전에 이 합이 나온 적 있으면 그때 위치부터 지금까지의 합이 0이라는 뜻.
            ans = max(ans, i - dic[total])  # 길이를 계산하고 지금까지 중 제일 긴 걸 저장해
        else:
            # 이 합이 처음 나왔다면, 그 위치를 저장해둬
            dic[total] = i

    return ans
