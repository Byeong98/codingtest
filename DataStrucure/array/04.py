"""
제시된 합을 가진 부분 배열 찾기

참조: Subarray with given sum
정렬되지 않은 양의 정수로 이루어진 배열 A가 있다. 연속된 원소를 더한 값이 제시된 값 S와 같은 부분 배열을 찾아라. (인덱스 기준은 1이다.)

입력: arr = [1, 2, 3, 7, 5], s = 12, 출력: [2, 4]
인덱스 2부터 4까지의 합: 2 + 3 + 7 = 12
입력: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], s = 15, 출력: [1, 5]
"""


# 이중 반복문 풀이
def solution(arr:list[int], s:int) -> list[int]:
    for i in range(len(arr)):
        arr_s = arr[i]
        for j in range(i+1, len(arr)):
            arr_s += arr[j]
            if arr_s == s:
                return [i+1, j+1]
            if arr_s > s:
                break
    return [-1]

print(solution([1, 2, 3, 7, 5],12))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],15))

# 정답 풀이
def solution2(arr:list[int], s:int) -> list[int]:
    for i in range(len(arr)):
        arr_s = 0
        for j in range(i, len(arr)):
            arr_s += arr[j]
            if arr_s == s:
                return [i+1, j+1]
    return [-1]

print("solution2",solution2([1, 2, 3, 7, 5],12))
print("solution2",solution2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],15))


# 두포인터 이용 풀이
def find_sub_array(arr: list[int], s: int) -> list[int]:
    x = 0
    answer = 0

    for y in range(len(arr)): # y는 0부터 마지막 인덱스 까지 반복.
        answer += arr[y] # 0~ len(arr) 까지 더 한다.
        while x < y and answer > s: # answer이 s 보다 큰 경우 arr[x]를 뺀다. x가 y보다 큰경우에도 정지
            answer -= arr[x]
            x+=1
        if answer == s: # answer과 s가 같으면 x,y 값을 반환
            return [x+1,y+1]

    return [-1] # len(arr)를 반복했지만 반환된 값이 없는 경우.

print("find_sub_array",find_sub_array([1, 2, 3, 7, 5],12))
print("find_sub_array",find_sub_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],15))
print("find_sub_array",find_sub_array([1, 2, 3, 4], 0))