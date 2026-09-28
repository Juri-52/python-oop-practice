"""課題3：銀行口座。条件はREADME.mdを確認してください。"""


class BankAccount:
    def __init__(self,owner,email,password,balance=0):
        # TODO: 口座名義人・メールアドレス・パスワード・残高を保存する。
        if balance <= 0:
            balance = 0
        self.owner = owner
        self.email = email
        self.owner = owner
        self.email = email
        self.password = password
        self.balance = balance
        print(f"口座名義人：{self.owner} / EMail：{self.email} 残高：{self.balance}")
        pass

    def check_balance(self):
        # TODO: 現在の残高を返す。
        return self.balance

    def deposit(self,amount):
        print(f"<入金> {self.owner} ← {amount}円")
        # TODO: 金額を確認して入金する。
        if amount <= 0:
            print("エラー：入金額を確認してください")
            return
        self.balance += amount
        pass

    def withdraw(self,amount):
        # TODO: 金額と残高を確認して出金する。
        print(f"<出金> {self.owner} → {amount}円")
        if amount <= 0:
            print("エラー：出金額を確認してください")
            return
        if amount > self.balance:
            print("エラー：残高不足")
            return
        self.balance -= amount
        pass

    def transfer(self,other_account,amount):
        # TODO: READMEのルールに従い、相手の口座へ送金する。
        print(f"<送金> {other_account.owner} ← {amount}円 ← {self.owner}")
        if other_account.owner == self.owner:
            print("エラー：この口座には送金できません")
            return
        if amount <= 0:
            print("エラー：送金額を確認してください")
            return
        if amount > self.balance:
            print("エラー：残高不足")
            return
        self.balance -= amount
        other_account.balance += amount
        pass


if __name__ == "__main__":
    # TODO: 口座を2つ作成し、残高確認・入金・出金・送金を確認する。
    account1 = BankAccount("A","J**@**.com","12345",1000)
    account2 = BankAccount("B","C**@**.com","67890",500)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.deposit(300)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.withdraw(200)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.transfer(account2,400)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.withdraw(800)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.transfer(account2,800)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.deposit(0)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.deposit(-100)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.transfer(account2,0)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.transfer(account1,100)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account2.transfer(account1,900)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    account1.withdraw(1600)
    print(f"口座{account1.owner}の残高：{account1.check_balance()}")
    print(f"口座{account2.owner}の残高：{account2.check_balance()}")

    pass
