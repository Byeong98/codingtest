"""
나머지가 1이 되는 수 찾기

문제 설명
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

제한사항
3 ≤ n ≤ 1,000,000
입출력 예
n	result
10	3
12	11
입출력 예 설명
입출력 예 #1

10을 3으로 나눈 나머지가 1이고, 3보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 3을 return 해야 합니다.
입출력 예 #2

12를 11로 나눈 나머지가 1이고, 11보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 11을 return 해야 합니다.

"""

def solution1(n):
    for i in range(2, n):
        if n % i == 1:
            return i    


# 다른 사람 풀이
def solution(n):
    answer = 0
    for divisior in range(2, int(n**1/2) +1) :# 2부터 루트(n)까지 검사
        if (n-1) % divisior == 0: # (n - 1)이 어떤 숫자로 나누어 떨어지면
            answer = divisior 
            break #탈출
        else: 
            answer = n-1 # 나누어 떨어지는 숫자가 없다면 (n-1)이 정답
    return answer


print(solution(10))