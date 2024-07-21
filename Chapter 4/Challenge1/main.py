class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        area = self.__width * self.__length
        return area
    
    def get_perimeter(self):
        set_1 = self.__width * 2
        set_2 = self.__length * 2
        return set_1 + set_2

class Square(Rectangle):
    def __init__(self, length):
        self.__width = length
        super().__init__(length,self.__width)
