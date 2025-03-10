"""
달리기 경주 

문제 설명
얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

제한사항
5 ≤ players의 길이 ≤ 50,000
players[i]는 i번째 선수의 이름을 의미합니다.
players의 원소들은 알파벳 소문자로만 이루어져 있습니다.
players에는 중복된 값이 들어가 있지 않습니다.
3 ≤ players[i]의 길이 ≤ 10
2 ≤ callings의 길이 ≤ 1,000,000
callings는 players의 원소들로만 이루어져 있습니다.
경주 진행중 1등인 선수의 이름은 불리지 않습니다.
입출력 예
players	callings	result
["mumu", "soe", "poe", "kai", "mine"]	["kai", "kai", "mine", "mine"]	["mumu", "kai", "mine", "soe", "poe"]
입출력 예 설명
입출력 예 #1

4등인 "kai" 선수가 2번 추월하여 2등이 되고 앞서 3등, 2등인 "poe", "soe" 선수는 4등, 3등이 됩니다. 5등인 "mine" 선수가 2번 추월하여 4등, 3등인 "poe", "soe" 선수가 5등, 4등이 되고 경주가 끝납니다. 1등부터 배열에 담으면 ["mumu", "kai", "mine", "soe", "poe"]이 됩니다.

"""

# def solution(players, callings):
#     for i in callings:
#         ind = players.index(i)
#         players[ind], players[ind-1] = players[ind-1], players[ind]
#     return players
"""
인덱스를 활용한 방법은 시간초과발생 
리스트 안에서 인덱스를 이용해 변경시 시간이 너무 많이 걸린다.
"""


# def solution(players, callings):
#     for i in callings:
#         ind =players.index(i)
#         players = players[:ind-1]+[players[ind]]+[players[ind-1]]+players[ind+1:]
#     return players
"""
시간 초과
"""

# def solution(players, callings):
#     for i in callings:
#         list = []
#         ind =players.index(i)
#         list += players[:ind-1]
#         for j in range(ind, len(players)):
#             if j == ind:
#                 list.append(players[j])
#                 list.append(players[j-1])
#             else:
#                 list.append(players[j])
#         players = list
#     return players


# def solution(players, callings):
#     for i in callings:
#         list = []
#         for j in range(len(players)):
#             if players[j] == i:
#                 list.pop()
#                 list.append(players[j])
#                 list.append(players[j-1])
#             else: 
#                 list.append(players[j])
#         players = list
#     return players


# def solution(players, callings):
#     rank = {player : i for i, player in enumerate(players)}

#     for call in callings:
#         #불린 선수의 등수
#         call_rank = rank[call]

#         front_player = players[call_rank-1]
        
#         rank[front_player], rank[call] = call_rank, call_rank-1
#         players[call_rank], players[call_rank-1] = front_player, players[call_rank]
#     return players


def solution(players, callings):
    rank = {player : i for i, player in enumerate(players)}

    for call in callings:
        c = rank[call]
        rank[call] -= 1

        rank[players[c-1]]+=1
        players[c-1], players[c] = players[c], players[c-1]

    return players



def solution(players, callings):
    rank = {player : i for i, player in enumerate(players)}

    for call in callings:
        rank[call] -= 1
        rank[players[rank[call]-1]]+=1
        players[rank[call]-1], players[rank[call]] = players[rank[call]], players[rank[call]-1]
    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))