"""
둘만의 암호 

문제 설명
두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.

문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
skip에 있는 알파벳은 제외하고 건너뜁니다.
예를 들어 s = "aukks", skip = "wbqd", index = 5일 때, a에서 5만큼 뒤에 있는 알파벳은 f지만 [b, c, d, e, f]에서 'b'와 'd'는 skip에 포함되므로 세지 않습니다. 따라서 'b', 'd'를 제외하고 'a'에서 5만큼 뒤에 있는 알파벳은 [c, e, f, g, h] 순서에 의해 'h'가 됩니다. 나머지 "ukks" 또한 위 규칙대로 바꾸면 "appy"가 되며 결과는 "happy"가 됩니다.

두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때 위 규칙대로 s를 변환한 결과를 return하도록 solution 함수를 완성해주세요.

제한사항
5 ≤ s의 길이 ≤ 50
1 ≤ skip의 길이 ≤ 10
s와 skip은 알파벳 소문자로만 이루어져 있습니다.
skip에 포함되는 알파벳은 s에 포함되지 않습니다.
1 ≤ index ≤ 20
입출력 예
s	skip	index	result
"aukks"	"wbqd"	5	"happy"
입출력 예 설명
입출력 예 #1
본문 내용과 일치합니다.

"""

"""
풀이 

1. s의 아스기 코드 값으로 변경하여 index 만큼 증가 시긴다. 
2. 증가 시키는 값에 skip의 아스키 값이 포함된 경우는 제외
3. Z 이상의 값으로 변경시 a값으로 변홤
"""

def solution1(s, skip, index):
    answer = ''
    skip_set = set(skip)
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip_set]
    for char in s:
        char_index = alphabet.index(char)
        new_index = (char_index + index) % len(alphabet)
        answer += alphabet[new_index]
    return answer




# 다른 사람 풀이 
def solution(s, skip, index):
    answer = ''

    a_to_z = set([chr(i) for i in range(97, 123)])
    print(a_to_z)
    a_to_z -= set(skip)

    print(a_to_z)
    a_to_z = sorted(a_to_z)
    print(a_to_z)



print(solution("aukks","wbqd",5))
