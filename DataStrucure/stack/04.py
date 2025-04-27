"""
후위 표기법

문자열 수식을 받아서 후위 표기법으로 바꾸는 함수를 작성하라. (단, 피연산자는 10 미만의 수이다.)
입력: "3+5*2", 출력: "352*+"
입력: “3*5+2”, 출력: “35*2+”
"""

def solution1(data:str) -> str:
    op: dict[str,int] = {"+":1, "-":1, "*":2, "/":2} # 연산자 우선 순위를 부여한다. 
    answer:str = "" # 출력할 값
    s: list[str] = [] # 스텍 연산자 값을 저장한다.
    for i in data: # 문자열을 순회 한다. 
        if i.isnumeric(): # 숫자일 경우 answer에 저장 
            answer += i
        elif i in op: # 연산자일 경우. 
            if s and op[i] <= op[s[-1]]: # 연산자가 스텍에 마지막 연산자보다 우선 순위가 낮은 경우.
                answer += s.pop() # 스텍의 마지막 값을 제거하여 answer에 더한다.
            s.append(i) # 연산자를 스텍에 저장한다.


    while s: # 스텍에 있는 모든 값을 answer에 저장 한다.
        answer += s.pop()
    return answer


print(solution1("3+5*2"))
print(solution1("3*5+2"))

