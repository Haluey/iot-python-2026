# ex18_encapsule.py 캡슐화

class Account:
    def __init__(self, money):
        # self.balance = money    # self.balance 는 public 접근과 동일
        self.__balance = money  # __는 private과 동일

    def deposit(self, money):  # 계좌입금
        self.__balance += money

    def get_balance(self):  # 계좌조회 getter
        return self.__balance

if __name__ == '__main__':
    myacc = Account(1000000)
    print(f'계좌 금액은 {myacc.get_balance():,}원')
    # print(f'계좌 금액 : {myacc.__balance:,}달러') # __ 변수는 외부에서 접근불가

    myacc.deposit(100_000)  # 정수 사용 시 _로 1000단위 구분가능
    print(f'계좌 금액은 {myacc.get_balance():,}원')

    # myacc.balance = -100000000 # 멤버 변수에 직접 접근가능
    print(f'계좌 금액은 {myacc.get_balance():,}원')
