"""課題1：学生クラス。条件はREADME.mdを確認してください。"""


class Student:
    def __init__(self, name, age, department, score):
        # TODO: 受け取った値を4つの属性に保存する。
        self.name = name
        self.age = age
        self.department = department
        self.score = score
        pass

    def is_passed(self):
        # TODO: 合否を表す真偽値を返す。
        if self.score >= 60:
            return True
        else:
            return False

    def info(self):
        # TODO: 学生の情報を表示する。
        print(f"氏名：{self.name} / 年齢：{self.age} 学科：{self.department} 点数：{self.score}")
        pass


if __name__ == "__main__":
    # TODO: 学生を2人作成し、両方のメソッドと属性の独立性を確認する。
    Mary = Student("Mary",18,"IT",60)
    John = Student("John",19,"SE",59)
    Mary.info()
    John.info()
    print(f"氏名：{Mary.name} / 合否：{Mary.is_passed()}")
    print(f"氏名：{John.name} / 合否：{John.is_passed()}")
    Mary.score = 0
    Mary.info()
    John.info()
    pass
