"""
해시 테이블은 검색, 저장, 삭제를 자주 하거나, 중복을 확인하거나 개수를 셀 때 사용하면 편하다.


문자열의 가장 먼저 나오는 유일한 문자 찾기

주어진 문자열에서 반복되지 않는 문자 중 가장 먼저 나오는 문자의 인덱스를 출력하라. 모든 문자가 중복되면, -1을 출력하라.

예시

입력: leetcode, 출력: 0
입력: loveleetcode, 출력: 2
입력: aabb, 출력 -1
"""

#  출현 빈도를 이용하여 해결할 수 있는 것이라면, 사전을 이용하면 된다.
def solution1(s:str) -> int:
    count:dict[str,int] = {}
    for i in s: # 각 문자수를 count에 저장
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    for i,v in enumerate(s): 
        if count[v] == 1: # 문자열 순서대로 돌며 한번만 나온 문자열 출력
            return i
    return -1



print(solution1('leetcode'))
print(solution1('loveleetcode'))
print(solution1('aabb'))


# collections를 이용하는 방법
from collections import Counter
def solution2(s:str) -> int:
    count = Counter(s)
    for i, v in enumerate(s):
        if count[v] == 1:
            return i
    return -1

print(solution2('leetcode'))
print(solution2('loveleetcode'))
print(solution2('aabb'))

# 리스트를 이용하는 방법
def solution3(s:str) -> int:
    n:int = len(s)
    chek:list[int] = [0]*n
    for i, v in enumerate(s): # 문자열을 반복
        if chek[i]: # 이미 확인 한 경우 0 -> 1로 변경
            continue
        chek[i] = 1 # 이미 확인으로 변경
        is_unique = True 
        for j in range(i+1, n): # i 번째 이외의 리스트를 확인
            if v == s[j]: # 같은 값이 있으면 정지
                chek[j] = 1 # chek 리스트의 값을 1로 변경
                is_unique = False
                break
        if is_unique: # 같은 값이 없으면 i를 반환
            return i
    return -1


print(solution3('leetcode'))
print(solution3('loveleetcode'))
print(solution3('aabb'))