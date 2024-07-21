class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name,health)
        self.__mana = mana

    def cast(self, target):
        mana_cost = 25
        spell_damage = 25
        if self.__mana >= mana_cost:
            self.__mana -= mana_cost
            target.take_damage(spell_damage)
        else:
            raise Exception("not enough mana")
