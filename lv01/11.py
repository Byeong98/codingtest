"""
삼총사 

문제 설명
한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다. 예를 들어, 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때, 첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사입니다. 또한, 두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 더해도 0이므로 세 학생도 삼총사입니다. 따라서 이 경우 한국중학교에서는 두 가지 방법으로 삼총사를 만들 수 있습니다.

한국중학교 학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때, 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.

제한사항
3 ≤ number의 길이 ≤ 13
-1,000 ≤ number의 각 원소 ≤ 1,000
서로 다른 학생의 정수 번호가 같을 수 있습니다.
입출력 예
number	result
[-2, 3, 0, 2, -5]	2
[-3, -2, -1, 0, 1, 2, 3]	5
[-1, 1, -1, 1]	0
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.
입출력 예 #2

학생들의 정수 번호 쌍 (-3, 0, 3), (-2, 0, 2), (-1, 0, 1), (-2, -1, 3), (-3, 1, 2) 이 삼총사가 될 수 있으므로, 5를 return 합니다.
입출력 예 #3

삼총사가 될 수 있는 방법이 없습니다.

"""

"""
풀이

리스트에서 각각의 숫자에 포인터를 만들어 값을 더하는 방식으로 진행했다.
하지만 다른 사람풀이를 보면 for 문을 3번 상용하거나 combinations 함수를 이용해서 문제를 풀었다.
가장 직관적인 방법을 찾도록 노력해야 갰다.
"""

def solution(number):
    answer = 0
    x,y,z = 0, 1, 2
    while x <= len(number)-3:
        if number[x]+number[y]+number[z] == 0:
            answer +=1

        z+=1
        if z >= len(number):
            y+=1
            z=y+1
        if y >= len(number)-1:
            x += 1
            y = x+1
            z = y+1

    return answer



print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))



# 다른 사람풀이 

from itertools import combinations

def solution2(number):
    return sum(1 for comb in combinations(number, 3) if sum(comb) == 0)


def solution3(number):
    answer = 0
    l = len(number)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                # print(number[i],number[j],number[k])
                if number[i]+number[j]+number[k] == 0:
                    answer += 1           
    return answer