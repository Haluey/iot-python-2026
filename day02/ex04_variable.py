# ex04_variable.py 변수/자료형

# 여러줄 주석은 여러줄 문자열로 대체 사용
'''
여러줄 문자열을
주석처럼 사용

**자료형**
- 정수(int) : 10
- 실수(float) : 3.141592
- 문자열(str) : "Hello", 'Hello'
- 불린(bool) : True/False
- None(NoneType) : None
- 그 외 클래스 타입
'''

val = 10
print(type(val))

val = 3.141592
print(type(val))

val = "'Hello'" # 특수문자 \n, \t, \', \" 지원
print(val)
print(type(val))

val = False
print(type(val))

# NoneType
val = None
print(type(val))

# 그 외
val = [1, 2, 3, 4]
print(type(val))

# val = ... 변수에는 뭐든지 들어감

# 메모리 제한이 없음
val = 99999999999999999999999999999999999999999999999999999999999999
print(val)

age = 20    # int
# print('나이는 ' + age)    # 이건 불가
print('나이는 ' * age)  # 문자열을 age의 값 만큼 반복
print('나이는 ' + str(age)) # 문자열을 다른 변수와 합치기(concatnate)
print('나이는', age, '입니다')  # 여러값을 자동으로 합쳐서 출력하라

# 한글로 변수명 지정해도 됨. C/C++ 동일
이름 = input('이름 > ')
나이 = int(input('나이 > '))    # 예외처리 필요
키 = float(input('키 > '))

print('이름 :', 이름, ', 나이 :', 나이, ', 키 :', 키)
