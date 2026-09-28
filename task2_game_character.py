"""課題2：ゲームキャラクター。条件はREADME.mdを確認してください。"""


class GameCharacter:
    def __init__(self,name,hp,mp):
        # TODO: 名前・HP・MPを設定し、初期値の範囲を確認する。
        if hp <= 0:
            hp = 0
        if mp <= 0:
            mp = 0
        if hp > 100:
            hp = 100
        if mp > 100:
            mp = 100
        self.name = name
        self.hp = hp
        self.mp = mp
        print(f"名前：{self.name} / HP：{self.hp} MP：{self.mp}")
        if self.hp == 0:
            print("Game Over")
        pass

    def take_damage(self,amount):
        # TODO: READMEのルールに従い、ダメージを処理する。
        print(f"<敵からの攻撃> ダメージ:{amount}")
        if self.hp == 0:
            print("エラー：行動不能")
            amount = 0
        if amount <= 0:
            print("エラー：ノーダメージ")
            amount = 0
        self.hp = max(0,self.hp-amount)
        print(f"名前：{self.name} / ダメージ：{amount}　現在HP：{self.hp}　現在MP：{self.mp}")
        if self.hp == 0:
            print("Game Over")
        pass

    def heal(self,amount):
        # TODO: READMEのルールに従い、回復とMP消費を処理する。
        print(f"<回復> 回復量：{amount}")
        if self.hp == 0:
            print("エラー：行動不能")
            amount = 0
        if self.hp == 100:
            print("エラー：体力最大")
            amount = 0
        if amount > self.mp:
            print(f"エラー：MP不足による回復力低下（{amount}→{self.mp}）")
            amount = self.mp
        if amount <= 0:
            print("エラー：回復不能")
            amount = 0
        if self.hp + amount > 100:
            amount = 100 - self.hp
            self.hp = 100
        else:
            self.hp += amount
        self.mp -= amount
        print(f"名前：{self.name} / 回復量：{amount}　現在HP：{self.hp}　現在MP：{self.mp}")
        pass


if __name__ == "__main__":
    # TODO: キャラクターを1体作成し、READMEの順番で動作を確認する。
    hero = GameCharacter("HERO",80,30)
    hero.heal(50)
    hero.heal(10)
    hero.take_damage(40)
    hero.heal(30)
    hero.heal(10)
    hero.take_damage(0)
    hero.heal(-10)
    hero.take_damage(200)
    hero.heal(20)

    hero2 = GameCharacter("HERO2",800,-30)
    hero3 = GameCharacter("HERO3",-80,300)

    pass
