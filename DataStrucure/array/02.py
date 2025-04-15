"""
회문 찾기 

주어진 문자열이 회문이면 True, 회문이 아니면 False를 반환하라.
입력: madam, 출력: True
입력: tomato, 출력: False
"""


# 문자열 슬라이싱 이용하기 
def solution(word:str):
    if word == word[::-1]:
        return True
    return False


# 두 포인터를 이용하는 방법
def is_palindrome(word: str) -> bool:
    lift , right = 0, len(word)-1

    while lift <= right: # lift 가 right 보다 큰경우 정지.
        if word[lift] != word[right]: # 양쪽 끝 문자를 비교, 다른 경우 false
            return False
        # 양끝점 가운데로 이동
        lift += 1 
        right -= 1
    return True


words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]
for word in words:
    print(f"Is '{word}' palindrome?  {is_palindrome(word)}")