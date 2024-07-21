class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line

class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows >= num:
                self.__num_arrows -= num
        else:
                raise Exception("not enough arrows")

class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name,num_arrows)

    def triple_shot(self, target):
        super().use_arrows(3)
        return (f"{target.get_name()} was shot by 3 crossbow bolts")
