class Account: # k = Account("Kim", 1000) 값 받음
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # = Account.account_count

    def deposit(self, amount): # 입금이 일어날 때마다 리스트로 저장된다.
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount


    def withdraw(self, amount): # 출금이 일어날 때마다 리스트로 저장된다.
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def withdraw_history(self): # 출금 내역
        for amount in self.withdraw_log:
            print(amount) # 지정된 출금액을 가져와 출력한다.

    def deposit_history(self): # 입금 내역
        for amount in self.deposit_log:
            print(amount) # 지정된 입금액을 가져와 출력한다.

k = Account("Kim", 1000)
k.deposit(100) # 입금
k.deposit(200) # 입금
k.deposit(300) # 입금
k.deposit_history() # 위에서 입금한 금액 차례대로 출력

k.withdraw(100) # 출금
k.withdraw(200) # 출금
k.withdraw_history() # 위에서 출금한 금액 차례대로 출력