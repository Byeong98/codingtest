"""
괄호의 짝이 맞는지 확인하기

문제 설명
괄호의 짝이 바르면 True, 바르지 않으면 False를 반환하는 함수를 작성하라.
예를 들어 ((a*(b+c))-d) / e는 괄호의 짝이 올바르지만, (((a*(b+c))-d) / e 는 괄호의 짝이 맞지 않는다. 괄호는 소괄호(())만 사용한다.


왼쪽 괄호를 만나면 스텍세 하나씩 넣고 오른쪽 괄호를 만나면 하나씩 뺀다.
"""

def solution(data: str) -> bool:
    s = []
    for i in data:
        if i == "(":
            s.append(i)
        elif i == ")":
            if not s.pop():
                return False

    if not s:
        return True
    else:
        return False
    

print(solution("((a * (b + c)) - d) / e"))
print(solution("(((a * (b + c)) - d) / e"))


"""
소괄호, 중괄호, 대괄호의 짝이 맞는지 검사하기

brakets을 만들어 해당 값이 있는 경우에는 삭제를 하고 pop한 값이 다른 경우 Fasle를 반환 한다.
"""

def solution2(data:str) -> bool:
    s = []
    brakets: dict[str, str] = {")":"(","]":"[","}":"{"}
    for i in data:
        if i in brakets.values():
            s.append(i)
        elif i in brakets:
            pop_braket = s.pop()
            if not pop_braket or brakets[i] != pop_braket:
                return False
    if s:
        return False
    else:
        return True
    
print(solution2("[{a * (b + c)} - d] / e"))
print(solution2("[{a * (b + c)] - d] / e"))


"""
짝지어 제거하기 

짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다.

예를 들어, 문자열 S = baabaa라면, **b aa baa → bb aa → aa → ** 의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다. 제거할 수 없으면 0을 반환합니다.

입출력 예

s = baabaa, result = 1
s = cdcd, result = 0
"""

def solution3(data:str) -> bool:
    s = []
    for i in data:
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)
        
    return 0 if s else 1


print(solution3("baabaa"))
print(solution3("cdcd"))