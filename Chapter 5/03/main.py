class Rectangle:
    def overlaps(self, rect):
        overlap, c_1, c_2, c_3, c_4 = False, False, False, False, False

        if self.get_left_x() <= rect.get_right_x():
            c_1 = True
        if self.get_right_x() >= rect.get_left_x():
            c_2 = True
        if self.get_top_y() >= rect.get_bottom_y():
            c_3 = True
        if self.get_bottom_y() <= rect.get_top_y():
            c_4 = True
        
        if (c_1 & c_2) & (c_3 & c_4):
            overlap = True
        return overlap

    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
