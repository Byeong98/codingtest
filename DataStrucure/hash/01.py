"""
해쉬 함수

key : value로 수성되 자료 구조로 데이터를 빠르게 검색하고 저장 할 수 있다.

해시 테이블에서는 서로 다른 키가 동일한 해시 값을 가질 때 충돌이 발생한다. 충돌을 해결하는 방법은 두 가지가 있다. 파이썬은 개방 주소법을 사용한다.

분리 연결법(Separate Chaining): 충돌한 데이터를 연결 리스트로 관리
개방 주소법(Open Addressing): 충돌 시 다음 빈 자리를 찾아 데이터를 저장

"""

# 해시테이블 클래스 만들기
#__init__ 메서드: 해시 테이블의 크기를 설정하고, 빈 리스트를 만든다.
#_hash 메서드: 키를 문자열로 바꿔서 각 문자의 아스키코드를 더한 후에 해시 테이블의 크기로 나눈 나머지를 구한다.
#set 메서드: 키와 값을 받는다. 키를 해시 함수에 넣어서 해시 값을 얻는다. 해시 테이블에 (키, 값)을 추가한다.
#get 메서드: 해시 테이블에서 키를 검색하여 값을 반환한다.

class HashTable:
    def __init__(self, length = 5):
        self.max_len = length
        self.table = [[] for _ in range(self.max_len)]

    # def _hash(self, key):
    #     res = sum([ord(s) for s in key])
    #     return res % self.max_len
    
    # def set(self, key, value):
    #     index = hash(key) % self.max_len
    #     self.table[index].append((key,value))

    # 같은 키값 존제시 덮어쓰기
    def set(self, key, value):
        index = hash(key) % self.max_len
        for i, (k,v) in enumerate(self.table[index]):
            if k == key: # 기존 키의 값을 갱신
                self.table[index][i] = (key,value)
                return
        self.table[index].append((key,index)) # 새 키-값 쌍 추가

    def get(self, key):
        index = hash(key) % self.max_len
        value = self.table[index]
        if not value:
            return None
        for v in value:
            if v[0] == key:
                return v[1]
        return None
    

if __name__ == "__main__":
    capital = HashTable()
    country = ["Korea", "America", "China", "England", "Türkiye"]
    city = ["Seoul", "Washington", "Beijing", "London", "Ankara"]
    for co, ci in zip(country, city):
        capital.set(co, ci)

    print("해시 테이블의 상태")
    print("===============")
    for i, v in enumerate(capital.table):
        print(i, v)
    print()
    print("해시 테이블의 검색 결과")
    print("====================")
    print(f"Captial of America = {capital.get('America')}")
    print(f"Captial of Korea = {capital.get('Korea')}")
    print(f"Captial of England = {capital.get('England')}")
    print(f"Captial of China = {capital.get('China')}")
    print(f"Captial of Japan = {capital.get('Japan')}")
    print(f"Captial of Türkiye = {capital.get('Türkiye')}")