# ex15_oop.py 객체지향

# 기본 사용법(실제로 이렇게 사용 안 함)
class Dog:
    pass

if __name__ == '__main__':
    poppy = Dog()   # 클래스 인스턴스 객체 생성
    poppy.name = '뽀삐'
    poppy.age = 3

print(f'강아지 이름 : {poppy.name}({poppy.age}살)')
