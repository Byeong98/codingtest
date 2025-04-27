"""
후위 표기법 02

소괄호만 사용하기
"""


def solution1(data:str) -> str:
    op: dict[str,int] = {"+":1, "-":1, "*":2, "/":2} 
    answer:str = "" 
    s: list[str] = [] 
    for i in data: 
        if i.isnumeric():  
            answer += i
        elif i == "(": # 왼쪽 소괄호를 만나면 저장
            s.append(i)
        elif i == ")": # 오른쪽 소괄호를 만나면 지금 까지 값들 제거하며 넣기
            while s[-1] != "(":
                answer += s.pop()
            s.pop() # ( 제거 
        elif i in op:
            if s and s[-1] != "(" and op[i] <= op[s[-1]]:
                answer += s.pop()
            s.append(i)

    while s:
        answer += s.pop()
    return answer


print(solution1("(3+5)*2"))
print(solution1("((1 + 2) * 3) / 4 + 5 * (6 - 7)"))

# 후위 표기법 숫자 계산하기 

def solution2(data:str) -> int:
    s: list[int] = [] 
    for i in data: 
        if i.isnumeric():  
            s.append(int(i))
        elif i != " ":
            n2 = s.pop()
            n1 = s.pop()
            if i == "+":
                res = n1 + n2
            elif i == "-":
                res = n1 - n2
            elif i == "*":
                res = n1*n2
            elif i == "/":
                res = n1/n2
            s.append(res)
    return s[0]



for expr in ("35+2*", "12+3*4/567-*+"):
    print(solution2(expr))