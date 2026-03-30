### ex13_datastruct.py 리스트 외 자료구조

## List(리스트) - 대괄호
arr = [1, 2, 3, 4]

arr.append(5)
print(f'리스트 값 = {arr}')

## Tuple(튜플) - 소괄호
# 변경이 불가능한 리스트, const형 리스트
# 튜플 -> DB에서 한 줄을 의미하는 단어
# 속도가 빠르고, 데이터를 함부로 못 고치게 고정 역할
tup = (1, 2, 3, 4)

# tup[2] = 9  # 오류 발생
print(f'튜플 값 = {tup}')

## Dictionary(딕셔너리) - 중괄호
# 사전형식, 빠른 검색이 가능한 hash기반
# 키로 접근 (key:value 항상 쌍)
# 키(key)는 통일(보통 문자열), 값(value)은 여러타입 사용 가능
# json과 구조가 동일.
spiderman = {
    'name' : '스파이더맨',
    'age' : 21,
    'real_name' : 'Peater Parker'
}

print(spiderman['real_name'])

## Set(집합) - 중괄호
# 중복제거, 순서 없음
# 집합연산(교집합, 차집합 등) 사용
st = {1, 3, 5, 7, 9, 3, 2, 1}
print(st)
