"""
문자열 나누기

문제 설명
문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.

먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 
처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.

s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.
만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.

제한사항
1 ≤ s의 길이 ≤ 10,000
s는 영어 소문자로만 이루어져 있습니다.
입출력 예
s	result
"banana"	3
"abracadabra"	6
"aaabbaccccabba"	3
입출력 예 설명
입출력 예 #1
s="banana"인 경우 ba - na - na와 같이 분해됩니다.

입출력 예 #2
s="abracadabra"인 경우 ab - ra - ca - da - br - a와 같이 분해됩니다.

입출력 예 #3
s="aaabbaccccabba"인 경우 aaabbacc - ccab - ba와 같이 분해됩니다.
"""


"""
첫 풀이 
마지막에 남아있는 문자 열을 추가하지 못하는 문제가 발생 했다.
x = s[0]으로 문제를 풀며 접근했다. 
1. s의 길이 만큼 돌며 x와 같으면 cx에 추가한다.
2. x와 같지 않으면 cy 에 값을 추가 한다.
3. cx == cy 가 같은 경우 x는 i+1 번째 변수와 변경
4. 나머지 cx, cy가 있는 경우 즉 나머지가 있는 경우 count 수 증가
"""
def solution1(s):
    x = s[0]
    cx = 0
    cy = 0
    count = 0

    for i in range(len(s)):
        if s[i] == x:
            cx += 1
        else:
            cy += 1

        if cx == cy:
            count += 1
            if i < len(s) -1:
                x = s[i+1]
            cx = 0
            cy = 0
    
    if cx > 0 or cy > 0:
        count +=1 
    
    return count


"""
2차 풀이 

이 문제에서 중요한 것은 "s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다." 이 부분인거 같다. 
처음 만나는 글자가 나오면 새로운 덩어리의 시작 반복 되는 작업을 통해 처음 부터 s를 새로 시작하는 문자열로 보고 
answer += 1 을 한다면 쉽게 풀이기 가능하다.

"""
def solution2(s):
    answer = 0
    x,y = 0, 0
    for i in s:
        if x == y:
            answer += 1
            k = i
        if k == i:
            x += 1
        else:
            y +=1

    return answer





def solution3(s):
    cx, cy  = 0, 0
    count = 0 
    for i in s:
        if cx == cy:
            count += 1
            x = i
        if x == i:
            cx += 1
        else: 
            cy += 1
    
    return count


print(solution3("banana"))
print(solution3("abracadabra"))
print(solution3("aaabbaccccabba"))