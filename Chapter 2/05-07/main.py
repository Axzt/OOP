fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target):
        if fireball_cost > self.mana:
            raise Exception(f"{self.name} cannot cast fireball")
        else:
            self.mana -= fireball_cost
            target.get_fireballed()
        
    def __is_alive(self):
        if self.health > 0:
            return True
        print(f"{self.name} is dead")
        return False

    def get_fireballed(self):
        self.health -= fireball_damage

    def drink_mana_potion(self):
        self.mana += potion_mana


# don't touch below this line


def main():
    merlin = Wizard("Merlin", 15, 10)
    morgana = Wizard("Morgana", 17, 5)
    print_wizard_stats(merlin)
    print_wizard_stats(morgana)

    while merlin._Wizard__is_alive() and morgana._Wizard__is_alive():
        test_cast(merlin, morgana)
        test_cast(morgana, merlin)

    print(" -- Done! --")


def test_cast(caster, target):
    print(f"  >  {caster.name} casts fireball at {target.name}")
    try:
        caster.cast_fireball(target)
    except Exception as e:
        print(f"    >  !!!{e}!!!")
        test_drink_potion(caster)
    print_wizard_stats(caster)
    print_wizard_stats(target)


def test_drink_potion(caster):
    print(f"  >  {caster.name} drinks mana potion")
    caster.drink_mana_potion()


def print_wizard_stats(wizard):
    print(f"{wizard.name}: health={wizard.health}, mana={wizard.mana}")


main()