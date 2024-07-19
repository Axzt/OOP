class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return (self.__pos_x, self.__pos_y)
