class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        in_y = False
        in_x = False
        for i in range(x_1, x_2+1):
            if self.pos_x == i:
                in_x = True
        for i in range(y_1, y_2+1):
            if self.pos_y == i:
                in_y = True
        if in_y & in_x:
            return True
        return False

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        units_hit = []
        x_1, y_1, x_2, y_2 = self.calculate_breath_aoe(x,y)
        for unit in units:
            if unit.in_area(x_1, y_1, x_2, y_2):
                units_hit.append(unit)
        return units_hit

    def calculate_breath_aoe(self,x,y):
        x_1 = x - self.__fire_range
        y_1 = y - self.__fire_range
        x_2 = x + self.__fire_range
        y_2 = y + self.__fire_range
        return (x_1, y_1, x_2, y_2)