"""
배열의 특징 

배열은 같은 자료형을 연속한 메모리에 저장한다.
- 인덕스로 인덱스에 접근 가능.
- 원소를 추가하거나 삭제할 때 전체 배열 구조를 변경해야 한다.
- 큐, 힙, 해시, 테이들, 행령 등 다양한 자료구조의 기본이다.
- 배열은 정혈 알고리즘을 구현시 자주 사용한다.

Python에서는 리스트와 차이 크기가 가변적이며 다양한 자료형 저장 가능. (슬라이싱 )
- 단일 자료형만 가용하면 array 클래스 사용 가능.

튜플과 리스트의 차이
- 한번 생성되면 크기와 변소 변경 불가.
- 데이터 저장에만 적합

정수 배열에서 가장 큰 두 수를 찾기

정수로 이루어진 배열이 주어질 때, 가장 큰 두 수를 찾아 [가장 큰 값, 둘째로 큰 값]을 반환하는 함수를 완성하라.
입력: [3, -1, 5, 0, 7, 4, 9, 1], 출력: [9, 7]
입력: [7], 출력: [7]
"""


def solution(numbers:list):
    """
    python의 내장 함수를 이용해 문제를 풀어봤다. 
    list.sort() : 원본데이터 정렬.
    sorted(list) : 복사본을 만들어 정렬. 
    """
    numbers.sort(reverse = True)
    return numbers[:2]


"""
배열을 순회하면서 직접비교해 값을 찾는 방식.
"""
def find_max_tow(arr:list):
    if len(arr) < 2: # arr리스트다 2보다 작은 경우 반환
        return arr    
    max1, max2 = arr[:2] # 리스트를 순차적으로 비교하기 위해 인덱스 0,1번 석택.
    if max1 < max2:
        max1 , max2 = max2, max1
    for n in arr[2:]: # 리스트 인덱스 2번 부터 마지막까지 반복
        if n > max1: 
            max1, max2 = n, max1
        elif n > max2: # n > max1이 거짓인 경우에만 실행 
            max2 = n
    return [max1, max2]


print(solution([3, -1, 5, 0, 7, 4, 9, 1]))
print(find_max_tow([3, -1, 5, 0, 7, 4, 9, 1]))


