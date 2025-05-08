"""
영어 끝말 잇기

1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해 주세요.

예시

n = 3, words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
result = [3, 3]
n = 5, words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
result = [0, 0]
"""

def solution1(n:int, words:list[int]) -> list[int]:
    s:set[str] =  set()
    tail:str = words[0][0]
    for i, word in enumerate(words):
        if word in s or tail != word[0]:
            return [i%n+1, i//n+1]
        s.add(word)
        tail = word[-1]

    return [0,0]

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution1(n, words))