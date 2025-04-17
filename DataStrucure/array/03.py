"""
0과 1로 구성된 배열을 정렬하기

참조: Binary Array Sorting
0과 1로 이루어진 배열이 있다. 배열 자체를 오름차순으로 정렬하라.

입력: [1, 0, 1, 1, 1, 1, 1, 0, 0, 0], 출력: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
입력: [1, 1], 출력: [1, 1]


"""


# sirted를 정령 함수를 이용해서 푸는 방법
#  sort, sorted 함수 설명   https://docs.python.org/3/howto/sorting.html
def solution(arr:list) -> list:
    return sorted(arr)


print("solution",solution([1, 0, 1, 1, 1, 1, 1, 0, 0, 0]))

# count를 사용하는 방식
def bin_array_sort(arr: list[int]) -> list[int]:
    # arr 변수 자체를 새로운 리스트로 할당하는 방식이다. 즉, 원래 리스트와의 참조가 끊김.
    # arr = [0] * arr.count(0) + [1]* arr.count(1) 
    arr[:] = [0] * arr.count(0) + [1]* arr.count(1) # 기존 리스트 객체 자체는 유지하면서 내용만 바뀜.
    
    return arr

print("bin_array_sort",bin_array_sort([1, 0, 1, 1, 1, 1, 1, 0, 0, 0]))
print("bin_array_sort",bin_array_sort([1,1]))


# 두개의 포인트를 사용하는 방식
def bin_array_point(arr:list[int]) -> list[int]:
    x, y = 0, len(arr)-1
    count = 0
    while x < y:
        count +=1
        if not arr[x]:
            x+=1
        if arr[y]:
            y -= 1
        if arr[x] > arr[y]:
            arr[x], arr[y] = arr[y], arr[x]
    print(count)
    return arr

# 총 반복문을 7번 움직인다. 
print(bin_array_point([1, 0, 1, 1, 1, 1, 1, 0, 0, 0]))


def bin_array_point2(arr: list[int]) -> None:
    """0과 1로 이루어진 배열 arr를 오름차순으로 정렬한다.
    Arguments:
        arr (list[int]): 0과 1로 이루어진 배열
    Return:
        None: 배열 arr 자체를 정렬한다.
    """
    left: int = 0
    right: int = len(arr) - 1
    count = 0
    while left < right:
        count +=1
        while left < len(arr) and arr[left] == 0: # left 가 배열 arr 길 보다 작은 경우와 1인 경우 까지 작동한다.
            left += 1
        while right >= 0 and arr[right] == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = 0, 1
            left, right = left + 1, right - 1
    print(count)

# 총 반복문을 4번 움직인다.
for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1]):  
    bin_array_point2(arr)  
    print(arr)